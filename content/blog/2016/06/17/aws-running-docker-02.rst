---
title: "Deploying Docker Containers on AWS, part 2"
date: "2016-06-17"
permalink: "/blog/2016/06/17/DeployingDockerContainersOnAWSPart2.html"
tags: [docker, aws]
---



I complained `a few weeks ago`_ about how hard it was to deploy Docker containers on AWS.

This week has been nothing but container-related frustration.
We have two apps running in Kubernetes clusters on top of AWS.
This is not a well-supported scenario and we have a fragile script
that spends a lot of time sitting in polling loops,
waiting for various things to happen like DNS updates taking effect,
the new cluster being available, and so on.
One of the apps has decided to stop deploying.
I do not know why.

I've been trying to get a new app deployed on ECS, the EC2 Container Service.
The way to deploy an updated app is to take an existing Task Definition,
update the tag on the image name, and create a new revision.
I have not figured out the right incantation to get the cluster service
to start running the new task consistently,
much less how to do this without any downtime.
It's insanely difficult to bring up a new cluster,
or, more specifically, to configure an EC2 instance for the new cluster.
There's a huge list of non-obvious pieces that need to be configured.
I discovered that you could append ``#/firstRun`` to the URL
to get the first-run wizard to reappear.
That causes no less than 15 pieces of AWS infrastructure to start up,
which is significantly more than you get when you create an ECS cluster the other way.
However, the ELB Load Balancer is not configured correctly.

I tried going back to ElasticBeanstalk,
since we've successfully deployed a Docker container on EB for the last two years.
I realized that the way to bootstrap a new environment is to upload ``Dockerrun.aws.json``.
However, I have yet to get the new environment to start up correctly.
I SSHed into the EC2 instance and found that the Docker daemon wasn't running
and refuses to start.

UPDATE: `fixed some problems with ElasticBeanstalk
<../18/DeployingDockerContainersOnAWSPart3.html>`_.

I am very, very unhappy with AWS this week.

.. _a few weeks ago:
    /blog/2016/05/24/DeployingADockerContainerOnAWS.html

.. _permalink:
    /blog/2016/06/17/DeployingDockerContainersOnAWSPart2.html
