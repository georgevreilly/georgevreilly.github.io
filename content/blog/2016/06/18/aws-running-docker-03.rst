---
title: "Deploying Docker Containers on AWS, part 3"
date: "2016-06-18"
permalink: "/blog/2016/06/18/DeployingDockerContainersOnAWSPart3.html"
tags: [docker, aws]
---



I complained yesterday_ about my difficulties in deploying Docker containers on AWS.
I have since succeeded in getting my app to deploy on ElasticBeanstalk,
though I have not quite ironed out all the problems.

I found several problems:

    * I had to revert from a Multi-Container Docker environment
      to a Single-Container Docker environment
      because ECS wasn't starting in the multi-container environment.
      That meant I had to revert to a v1 ``Dockerrun.aws.json``.
    * I had to ensure that the Instance Profile had the
      AmazonEC2ContainerRegistryReadOnly policy attached,
      so that I could pull from the EC2 Container Repository.

.. _yesterday:
    ../17/DeployingDockerContainersOnAWSPart2.html

.. _permalink:
    /blog/2016/06/18/DeployingDockerContainersOnAWSPart3.html
