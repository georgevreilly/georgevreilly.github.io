---
title: "Deploying a Docker Container on AWS"
date: "2016-05-24"
permalink: "/blog/2016/05/24/DeployingADockerContainerOnAWS.html"
tags: [docker, aws]
---



.. image:: https://www.ybrikman.com/assets/img/blog/aws-docker/docker-on-aws.png
    :alt: Docker + AWS
    :target: http://www.ybrikman.com/writing/2015/11/11/running-docker-aws-ground-up/
    :class: right-float

I spent a couple of frustrating hours this evening
trying to figure out an easy way to deploy a Docker container on AWS.
I tried out the `EC2 Container Service`_ and got lost
in a sea of Clusters, Tasks, and Services.
I couldn't connect to the EC2 instance where my container supposedly lived.

I tried `Elastic Beanstalk`_ and gave up in exasperation.
When you create a new Docker environment,
there's no way to pull an existing image from an external repo
that I could see.
We have some tools for deploying a Docker image to Elastic Beanstalk,
but they were so cryptic that I didn't want to pursue that.

Eventually I went old school.
I created a new EC2 instance,
SSHed in,
installed Docker,
logged into the Docker repository,
pulled the image,
and started the container.
Admittedly, redeployment will be a pain
and I don't get autoscaling or other AWS goodness,
but I got the container working in 10 minutes.

.. _EC2 Container Service:
    https://aws.amazon.com/ecs/
.. _Elastic Beanstalk:
    https://aws.amazon.com/elasticbeanstalk/

.. _permalink:
    /blog/2016/05/24/DeployingADockerContainerOnAWS.html
