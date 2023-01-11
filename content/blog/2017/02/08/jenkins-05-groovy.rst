---
title: "Jenkins #5: Groovy"
date: "2017-02-08"
permalink: "/blog/2017/02/08/Jenkins05-Groovy.html"
tags: [jenkins, metabrite]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/

Jenkins Pipelines are written in a Groovy DSL.
This is a good choice but there are surprises.

`#5 in a series on Jenkins Pipelines 
</blog/2017/02/04/Jenkins01-MigratingToPipelines.html>`_

Groovy as a DSL
^^^^^^^^^^^^^^^

Groovy lends__ itself to writing__ DSLs (`Domain-Specific Languages`__)
with a minimum of syntactic overhead.
You can frequently omit the parentheses, commas, and semicolons that litter other languages.

Groovy has `interpolated GStrings`__, lists, maps, functions, and closures.

__ https://docs.groovy-lang.org/docs/latest/html/documentation/core-domain-specific-languages.html
__ https://dzone.com/articles/groovy-dsl-simple-example
__ https://en.wikipedia.org/wiki/Domain-specific_language
__ https://groovy-lang.org/syntax.html#_string_interpolation

Closures
~~~~~~~~

Closures__ are anonymous functions where state can be captured at declaration time
to be executed later.
The blocks that follow many Pipeline steps (``node``, ``stage``, etc) are closures.

Here's an example of a ``Closure`` called ``acceptance_integration_tests``,
where the ``release_level`` parameter is a ``String``
which must be either ``"dev"`` or ``"prod"``.

.. code-block:: groovy

    def acceptance_integration_tests = { String release_level ->
        assert release_level =~ /^(dev|prod)$/
        String arg = "--${release_level}"

        def branches = [
            "${release_level}_acceptance_tests": {
                run_tests("ci_acceptance_test", arg, '**/*nosetests.xml')
            },
            "${release_level}_integration_tests": {
                run_tests("ci_integration_test", arg, '**/*nosetests.xml')
            }
        ]
        parallel branches
    }

We create a ``Map`` called ``branches`` with dynamically named keys,
such as ``"prod_integration_tests"``,
thanks to ``GString`` interpolation.
The values in the ``branches`` map are in turn also closures,
where ``arg`` is bound to ``"--dev"`` or ``"--prod"``.

The ``branches`` map is passed to Pipeline's ``parallel`` command,
which causes the two ``run_tests`` closures to be executed
on two different executors—eventually.

.. code-block:: groovy

    stage("Deploy to Dev") { deploy "dev" }
    stage("Dev Tests") { acceptance_integration_tests "dev" }

    stage("Deploy to Prod") { deploy "prod" }
    stage("Prod Tests") { acceptance_integration_tests "prod" }

The ``acceptance_integration_tests`` closure is used in two different ``stage``\ s.
Each ``stage`` is passed an anonymous closure,
which invokes the parallel tests at a suitable time.

__ https://groovy-lang.org/closures.html

Not So Groovy
~~~~~~~~~~~~~

**Fiction**: Jenkins Pipeline scripts are written in Groovy.

**Fact**: Pipeline scripts are written in a *sandboxed subset* of Groovy
and you need to be aware of the differences.

The Pipeline plugin presents the illusion
that a Groovy program is executing on your agent node.
It's more complicated__ than that.
The Pipeline script compiles the script into a series of steps on the `master node`__,
where they are executed in a flyweight executor.
Many steps actually result in the corresponding code being executed in an agent node.
These steps execute in a restricted sandbox.
Many steps are asynchronous and the complete state of the build is persisted
each time such a step is executed.
Jenkins may be restarted during a build and will resume executing.
A lot of this magic__ is achieved through rewriting the Groovy program
using a `continuation-passing style transformation`__.

The combination of the sandbox and serialization imposes restrictions
on the Groovy code that you can write.
Many Java and Groovy classes and methods are not allowlisted
and cannot be executed at all.
Some may be used only in restricted circumstances.
Essentially, you're limited to strings, numbers,
and lists and maps built out of strings and numbers.

You can work around this to some extent
by decorating a Groovy function with ``@NonCPS``
and operating on otherwise forbidden objects as local variables.
You must, however, return serializable objects from such a function.

If you control your Jenkins master, you can allowlist JVM classes that you may need.
CloudBees hosts our Jenkins builds, so this was not available to us.

__ https://github.com/jenkinsci/workflow-cps-plugin/blob/master/README.md
__ https://jenkins.io/blog/2017/02/01/pipeline-scalability-best-practice/
__ https://github.com/jenkinsci/workflow-cps-plugin/blob/master/README.md
__ https://en.wikipedia.org/wiki/Continuation-passing_style

I spent a ridiculous amount of time
trying to get this apparently straightforward code to work:

.. code-block:: groovy

    def label = compute_build_label(
        new Date(), env.GIT_LOCAL_BRANCH, env.BUILD_NUMBER, env.GIT_COMMIT)

    def compute_build_label(
        Date build_date, String branch_name, Integer build_number, String git_sha)
    {
        String date = build_date.format("yyyyMMdd't'HHmm'z'", TimeZone.getTimeZone('UTC'))
        String branch = branch_name.replaceAll("/", "-")
        String number = String.format("%05d", build_number)
        String sha = git_sha.substring(0, 7)
        return "${date}-${branch}-b${number}-${sha}"
    }

Here are just some of the reasons why this didn't work:

* ``org.jenkinsci.plugins.scriptsecurity.sandbox.RejectedAccessException:
  Scripts not permitted to use new java.util.Date``: you can't use ``new Date()``.
  I ended up shelling out to the system ``date`` command.
* ``java.lang.NoSuchMethodError:
  No such DSL method 'compute_build_label' found among steps […]``:
  This very unhelpful error means that the function signature didn't match its use,
  as ``env.BUILD_NUMBER`` is a ``String``, not an ``Integer``.
* ``org.jenkinsci.plugins.scriptsecurity.sandbox.RejectedAccessException:
  Scripts not permitted to use staticMethod java.lang.String format``:
  I was attempting to use ``String.format("%05s", build_number)``.
* I switched to ``"0000${build_number}"[-5..-1]`` to take the last five digits and got
  ``org.jenkinsci.plugins.scriptsecurity.sandbox.RejectedAccessException:
  Scripts not permitted to use staticMethod org.codehaus.groovy.runtime.ScriptBytecodeAdapter
  createRange``.
* Despite my `reading of GitSCM.java`__,
  ``env.GIT_LOCAL_BRANCH`` and ``env.GIT_COMMIT`` did not contain useful values.

I ended up with this:

.. code-block:: groovy

    String label = compute_build_label(
        sh(script: 'date --utc +%Y%m%dt%H%Mz', returnStdout: true).trim(),
        GIT_BRANCH,
        env.BUILD_NUMBER,
        sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
    )

    String compute_build_label(
        String date, String branch_name, String build_number, String git_sha)
    {
        String branch = branch_name.replaceAll("/", "-")
        String number = "00000".substring(0, 5 - build_number.length()) + build_number
        String sha = git_sha.substring(0, 7)
        return "${date}-${branch}-b${number}-${sha}"
    }

__ https://github.com/jenkinsci/git-plugin/blob/master/src/main/java/hudson/plugins/git/GitSCM.java#L1237

I would have been better off writing an external script.

Tips
^^^^

Line Numbers
~~~~~~~~~~~~

If you see a callstack like this::

    …
    at WorkflowScript.run(WorkflowScript:39)
    at ___cps.transform___(Native Method)
    at com.cloudbees.groovy.cps.impl.ContinuationGroup.methodCall(ContinuationGroup.java:48)
    …

Look in your Pipeline Script at the line number specified in the ``WorkflowScript`` entry
(here, line ``39``).

Install Groovy
~~~~~~~~~~~~~~

For debugging some Groovy syntax issues,
it can be much faster to try them out in a local Groovy script.

I installed Groovy using Brew__ on my Mac.
I found that I had to set the ``$JAVA_HOME`` and ``$GROOVY_HOME`` environment variables
before it worked properly for me.

* ``export JAVA_HOME="$(/usr/libexec/java_home)"``
* ``export GROOVY_HOME="$(brew --prefix)/opt/groovy/libexec"``

__ https://brew.sh/

.. _permalink:
    /blog/2017/02/08/Jenkins05-Groovy.html
