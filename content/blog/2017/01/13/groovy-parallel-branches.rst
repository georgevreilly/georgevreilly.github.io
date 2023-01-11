---
title: "Computed Parallel Branches in Jenkins Pipeline"
date: "2017-01-13"
permalink: "/blog/2017/01/13/ComputedParallelBranchesInJenkinsPipeline.html"
tags: [jenkins, til]
---



I've been using Jenkins lately,
setting up Pipeline__ builds.
I have mixed feelings about that,
but I'm quite liking Groovy.

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
The values in the ``branches`` map are themselves closures,
where ``arg`` is bound to ``"--dev"`` or ``"--prod"``.

The ``branches`` map is passed to Pipeline's ``parallel`` command,
which causes the two ``run_tests`` closures to be executed
on two different executors—eventually.

I figured out the above syntax myself, then found a `similar example`__.

.. code-block:: groovy

    stage("Deploy to Dev") { deploy "dev" }
    stage("Dev Tests") { acceptance_integration_tests "dev" }

    stage("Deploy to Prod") { deploy "prod" }
    stage("Prod Tests") { acceptance_integration_tests "prod" }

The ``acceptance_integration_tests`` closure is used in two different ``stage``\ s.
Each ``stage`` is passed an anonymous closure,
which invokes the parallel tests at a suitable time.

The use of closures and Groovy's DSL__ facilities
is powerful, terse, and expressive.


__ https://jenkins.io/solutions/pipeline/
__ https://jenkins.io/doc/pipeline/examples/#jobs-in-parallel
__ http://docs.groovy-lang.org/docs/latest/html/documentation/core-domain-specific-languages.html

.. _permalink:
    /blog/2017/01/13/ComputedParallelBranchesInJenkinsPipeline.html
