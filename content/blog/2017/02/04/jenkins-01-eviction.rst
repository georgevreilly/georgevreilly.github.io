---
title: "Jenkins #1: Migrating to Pipelines"
date: "2017-02-04"
permalink: "/blog/2017/02/04/Jenkins01-MigratingToPipelines.html"
tags: [jenkins, metabrite]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/

The MetaBrite dev team migrated most of their builds
from Atlassian's Bamboo Cloud to Jenkins Pipelines in late 2016/early 2017.
This is a series of blog posts about that experience.

Jenkins Pipeline Series
^^^^^^^^^^^^^^^^^^^^^^^

The series so far:

- `Jenkins #1: Migrating to Pipelines </blog/2017/02/04/Jenkins01-MigratingToPipelines.html>`_
- `Jenkins #2: EC2 Slaves </blog/2017/02/05/Jenkins02-EC2Slaves.html>`_
- `Jenkins #3: GitHub Integration </blog/2017/02/06/Jenkins03-GitHubIntegration.html>`_
- `Jenkins #4: The sh step </blog/2017/02/07/Jenkins04-shStep.html>`_
- `Jenkins #5: Groovy </blog/2017/02/08/Jenkins05-Groovy.html>`_
- `Jenkins #6: Miscellenea </blog/2017/02/09/Jenkins06-Miscellenea.html>`_


Eviction
^^^^^^^^

For three years, we used Atlassian's hosted `Bamboo Cloud`__ service
to build and deploy most of our code.
In the summer of 2016,
Atlassian announced that they were
going to discontinue Bamboo Cloud on January 31st, 2017.

We looked around for a suitable replacement.
We did not find anything would work well for us.
We had requirements that were—surprisingly—hard to satisfy.
Much of our code is in one large GitHub repository,
from which we build several very different applications.
Many of the CI systems that we rejected
were designed to build only one project per repository.
Another hard requirement was that a push to the *master* branch in this repo
should not trigger a build of every application;
only the applications in the affected directories should be built.
We also didn't want to host our own build system,
preferring to pay for a service that considered hosting CI
to be one of their core competencies.
We liked some of the systems that we evaluated,
but none of them satisfied our needs.

Failing to find a new system that we liked,
we reluctantly experimented with hosting Bamboo Server ourselves,
reasoning that it should be fairly easy
to get our Bamboo Cloud builds working on Bamboo Server.
It wasn't.
Getting Bamboo Server even half working was painful and unsatisfactory.
Time for Plan C.

We took a closer look at Jenkins;
more specifically, at CloudBees__' hosted offering.
Some of us had previously used `Jenkins Free-Style Builds`__
at other jobs in the past and were unenthusiastic about doing so again.
In fact, we had already been customers of CloudBees for a couple of years,
as most of our Android builds were built there.

We initially experimented with Free-Style builds
and found them no more pleasing than we remembered.
Hesitantly, we tried the Pipeline__ builds (formerly the Workflow Plugin)
that formed the heart of last year's `Jenkins 2.0 release`__.

With Jenkins Pipelines, we finally found something that made us happy.
But there was a long, steep learning curve and we haven't reached the summit yet.
This series of posts describes much of our hard-won knowledge.
Had we found similar posts written by someone else before we started,
we would have saved ourselves considerable time.


__ https://confluence.atlassian.com/bamboocloud/
__ https://www.cloudbees.com/
__ https://wiki.jenkins-ci.org/display/JENKINS/Building+a+software+project
__ https://jenkins.io/2.0/
__ https://jenkins.io/blog/2016/04/26/jenkins-20-is-here/


Pipelines
~~~~~~~~~

The Pipeline is the heart of Jenkins 2.0.
The traditional Free-Style build has been supplanted by a more powerful mechanism
that supports a rich `Domain-Specific Language (DSL)`__
and a variety of other features.

Having our build system be under source control was almost enough to sell us on Pipeline.
After Bamboo, where a build had to be configured across multiple screens, tabs, and forms,
having everything in a single Groovy file was appealing.
(A few settings do still need to be configured in a Jenkins webform.)
Being able to use an expressive language like Groovy as the basis of the DSL
leads to compact, terse, maintainable, and reusable functionality.

This series of posts is *not* intended to be a comprehensive introduction to Pipelines.
These resources may help:

* `Pipeline Tutorial`__
* `Wilson Mar`__
* `SysAdvent`__
* `DZone RefCard #218`__
* `Top 10 Best Practices for Jenkins Pipeline Plugin`__
* `Best Practices`__
* `Best Practices for Scalable Pipeline Code`__
* `Introducing CloudBees Jenkins Enterprise`__


The Pipeline documentation is, bluntly, not very good.
It's frequently confusing and often incomplete.
You need to search and to be willing to paw through Java code in GitHub repositories.

__ https://en.wikipedia.org/wiki/Domain-specific_language
__ https://github.com/jenkinsci/pipeline-plugin/blob/master/TUTORIAL.md
__ https://wilsonmar.github.io/jenkins2-pipeline/
__ https://sysadvent.blogspot.com/2016/12/day-8-building-robust-jenkins-pipelines.html
__ https://dzone.com/refcardz/continuous-delivery-with-jenkins-workflow
__ https://www.cloudbees.com/blog/top-10-best-practices-jenkins-pipeline-plugin
__ https://github.com/jenkinsci/pipeline-examples/blob/master/docs/BEST_PRACTICES.md
__ https://jenkins.io/blog/2017/02/01/pipeline-scalability-best-practice/
__ https://go.cloudbees.com/docs/cloudbees-documentation/cje-user-guide/

Acknowledgements
~~~~~~~~~~~~~~~~

The work on which this series is based was jointly done with Adam Porad.
Several of CloudBees' support engineers were very helpful,
including Owen Wood, Allan Burdajewicz, Travis Sweet, and Adrien Lecharpentier.

.. _permalink:
    /blog/2017/02/04/Jenkins01-MigratingToPipelines.html
