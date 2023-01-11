---
title: "DockerCon 2016"
date: "2016-06-21"
permalink: "/blog/2016/06/21/DockerCon2016.html"
tags: [docker, metabrite]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

I attended `DockerCon 2016`_ in Seattle
over the last two days and I learned a lot.
It was a well-run conference with an enthusiastic audience.

I'm astounded at the growth of Docker.
Three-and-a-quarter years ago,
Docker was revealed to the public for the first time,
in a `five-minute lightning talk`_ at PyCon 2013.
In January 2016, Docker Hub had received `1.6 billion image pulls`_;
by this month, that number had jumped to over 4 billion pulls!
DockerCon had over 4,000 attendees and nearly 100 exhibitors,
who clearly believe there's a multi-billion dollar market for containers.
DataDog concurs, in a report on `Docker adoption`_.

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/
.. _DockerCon 2016:
    http://web.archive.org/web/20161121204237/http://2016.dockercon.com/
.. _five-minute lightning talk:
    https://www.youtube.com/watch?v=wW9CAH9nSLs
.. _1.6 billion image pulls:
    https://blog.docker.com/2016/02/docker-hub-two-billion-pulls/
.. _Docker adoption:
    https://www.datadoghq.com/docker-adoption/

The Sad State of Clustering
---------------------------

I've become pretty good at building Docker images,
thanks to my work on `FlyingCloud`_,
a tool that MetaBrite open-sourced earlier this year.
FlyingCloud helps you build Docker images using `SaltStack`_
and makes it easy to run tests inside the container.

I'm generally happy with running containers
but I've had less luck with deploying them in clusters.
In fact, I spent last week fighting with deployments
of various kinds of clusters on AWS:
`ECS`_, `Kubernetes`_, and `Elastic Beanstalk`_.
Everything seems very immature.

I like the theory of Kubernetes;
in practice, it's been very painful for us on AWS.
We have a couple of apps that we've deployed as Kubernetes clusters,
using a homegrown script that uses `kubectl`_, `kube-aws`_, and `boto3`_
to spin up a new cluster, provision load balancers, and so on.
Both apps required heroic effort to bootstrap into working Kubernetes clusters.
Worse, our deployment script has grown increasingly temperamental,
failing to detect if the newly deployed cluster is ready.
I talked to someone from the Kubernetes team yesterday,
who promised some relief in a few months when 1.4 ships.
He mentioned `Terraform`_ in passing.

.. _FlyingCloud:
    https://github.com/xbrite/flyingcloud
.. _SaltStack:
    https://saltstack.com/
.. _ECS:
    https://aws.amazon.com/ecs/
.. _Kubernetes:
    https://kubernetes.io/
.. _Elastic Beanstalk:
    https://aws.amazon.com/elasticbeanstalk/
.. _kubectl:
    https://kubernetes.io/docs/user-guide/kubectl-overview/
.. _kube-aws:
    https://coreos.com/kubernetes/docs/latest/kubernetes-on-aws.html
.. _boto3:
    https://github.com/boto/boto3
.. _Terraform:
    https://www.terraform.io/

I tried setting up a new app on ECS,
but eventually I gave up.
The very first time you create an ECS cluster,
it configures 15 obscure pieces of AWS infrastructure.
If you create another cluster,
you have to jump through a series of non-obvious hoops
to correctly configure your EC2 instances.
I have not discovered a reliable way to update the cluster with a new image—\
sometimes the new container runs, sometimes not—\
much less a zero-downtime update.

I fell back to using Elastic Beanstalk,
which is working fine for a Single-Container Docker app.
Multi-Container Docker utterly failed—trying to start up ECS.

Keynotes
--------

Therefore, I was very happy at yesterday's keynote to hear all the announcements
about Orchestration, Services, and Docker Swarm for AWS:
`Docker 1.12\: Now with Built-in Orchestration!`_,
`Docker for AWS and Azure Beta`_,
`Distributed Application Bundles`_,
`More Microservices Bliss with Docker 1.12 and Swarm only`_
`Running Services in Docker 1.12`_, and
`DockerCon 2016 - What is new in Docker 1.12`_.
The demos were very slick and very compelling.
Docker for AWS has just entered private beta.
As a DockerCon attendee, I should receive an invitation soon.
Although it has been out for some time,
I have yet to try `Docker Compose`_.
It looks like it simplifies multi-container apps.

.. _Docker 1.12\: Now with Built-in Orchestration!:
    https://blog.docker.com/2016/06/docker-1-12-built-in-orchestration/
.. _Running Services in Docker 1.12:
    https://blog.codeship.com/running-services-docker-1-12/
.. _Introducing the Docker for AWS and Azure Beta:
.. _Docker for AWS and Azure Beta:
    https://blog.docker.com/2016/06/azure-aws-beta/
.. _Introducing Experimental Distributed Application Bundles:
.. _Distributed Application Bundles:
    https://blog.docker.com/2016/06/docker-app-bundle/
.. _DockerCon 2016 - What is new in Docker 1.12:
    https://ordina-jworks.github.io/conference/2016/06/20/whats-new-in-docker-112.html
.. _More Microservices Bliss with Docker 1.12 and Swarm only:
    https://blog.hypriot.com/post/more-microservice-bliss-with-docker-1-12/
.. _Docker Compose:
    https://docs.docker.com/compose/

I was also happy to hear about the `Docker for Mac and Windows Public Beta`_.
I've been a satisfied user of Docker for Mac for a couple of months,
and now it's available to everyone.
I saw several demos where people were `Developing Inside Docker Containers with OS X`_.
They were able to edit and debug in `Visual Studio Code`_
with the source code shared between a Mac host and a Docker container.
I should rethink some of my development workflow
and stop installing so much in my host operating system.

.. _Docker for Mac and Windows Public Beta:
    https://blog.docker.com/2016/06/docker-mac-windows-public-beta/
.. _Developing Inside Docker Containers with OS X:
    https://hharnisc.github.io/2016/06/16/developing-inside-docker-containers-with-osx-2016.html
.. _Visual Studio Code:
    https://blog.ctaggart.com/2016/05/visual-studio-code-served-from-docker.html

Tuesday's Keynote was about `Democratizing Docker for Enterprise`_.
Docker are touting *Incremental Revolution*.
Certainly, containers are something that even big stodgy IT shops can no longer ignore.

.. _Democratizing Docker for Enterprise:
    https://blog.codeship.com/docker-enterprise/

Talks
-----

All the talks that I attended were good.
They were all recorded and videos should be available later.

`High Security Microservices`_ dove deep into hitherto obscure areas.
More at `Stop Buying Bad Security Prescriptions`_
and `Understanding and Hardening Linux Containers`_.

.. _High Security Microservices:
    https://dockercon2016.sched.org/event/70Ni/the-golden-ticket-docker-and-high-security-microservices
.. _Stop Buying Bad Security Prescriptions:
    https://medium.com/@justin.schuh/stop-buying-bad-security-prescriptions-f18e4f61ba9e#.dls917gbl
.. _Understanding and Hardening Linux Containers:
    https://www.nccgroup.trust/us/about-us/newsroom-and-events/blog/2016/april/understanding-and-hardening-linux-containers/

`Microservices + Events + Docker = A Perfect Trio`_
made an interesting case for `Event-driven microservices`_.
More at `LearnMicroservices.io`_
and `A decade of DDD, CQRS and Event Sourcing`_.

.. _Microservices + Events + Docker = A Perfect Trio:
    https://dockercon2016.sched.org/event/70OP/microservices-events-docker-a-perfect-trio 
.. _Event-driven microservices:
    https://eventuate.io/whyeventdriven.html
.. _LearnMicroservices.io:
    https://learnmicroservices.io
.. _A decade of DDD, CQRS and Event Sourcing:
    https://ordina-jworks.github.io/domain-driven%20design/2016/02/02/A-Decade-Of-DDD-CQRS-And-Event-Sourcing.html

`The Dockerfile Explosion and the Need for Higher Level Tools`_
was very close to my heart, as I had written such a tool,
the afore-mentioned FlyingCloud_.
Dockerfiles are not good for building complex images,
as you tend to end up with a mess of imperative Bash scripts.
The speaker covered several tools that I hadn't previously known about,
such as `Dockramp`_ and `Rocker`_.
Two new tools have been announced in the last week,
Chef's `Habitat`_ and `Ansible Container`_.
Both do far more than FlyingCloud,
as they not only build but deploy and manage containers.

.. _The Dockerfile Explosion and the Need for Higher Level Tools:
    https://dockercon2016.sched.org/event/70Ng/the-dockerfile-explosion-and-the-need-for-higher-lehellip
.. _Dockramp:
    https://github.com/jlhawn/dockramp
.. _Rocker:
    https://tech.grammarly.com/blog/posts/Making-Docker-Rock-at-Grammarly.html
.. _Ansible Container:
    https://www.ansible.com/ansible-container
.. _Habitat:
    https://www.habitat.sh/

`Immutable Awesomeness`_ was a reprise of an earlier presentation at `DOES15`_
about reducing operational pain.
See also:
Docker and the Three Ways of DevOps:
`Systems Thinking`_, `Amplify Feedback Loops`_, and
`Culture of Continuous Experimentation and Learning`_.

.. _Immutable Awesomeness:
    https://dockercon2016.sched.org/event/70OV/immutable-awesomeness
.. _DOES15:
    https://devops.com/2015/11/13/does-2015-josh-corman-john-willis-on-immutable-awesomeness/
.. _Docker and the Three Ways of DevOps Part 1\: The First Way – Systems Thinking:
.. _Systems Thinking:
    https://blog.docker.com/2015/05/docker-three-ways-devops/
.. _Docker and the Three Ways of DevOps Part 2\: The Second Way – Amplify Feedback Loops:
.. _Amplify Feedback Loops:
    https://blog.docker.com/2015/06/docker-three-ways-devops-2/
.. _Docker and the Three Ways of DevOps Part 3\: The Third Way – Culture of Continuous Experimentation and Learning:
.. _Culture of Continuous Experimentation and Learning:
    https://blog.docker.com/2015/07/docker-three-ways-devops-3/

`Efficient Parallel Testing with Docker`_
discussed Codeship's approach to testing using a suite of Docker containers
in a series of parallel stages.
The `Jet CLI`_ can run your CI/CD pipeline on your local machine.

.. _Efficient Parallel Testing with Docker:
    https://dockercon2016.sched.org/event/70Nn/efficient-parallel-testing-with-docker
.. _Jet CLI:
    https://codeship.com/documentation/docker/installation/

I was only able to attend one talk on the second day,
`Sharding Containers\: Make Go Apps Computer-Friendly Again`_.
The speaker's `Tesson`_ uses the principles of Sharding,
local Load Balancing, and Hardware Locality
to pin Docker containers to processor cores,
reducing Go garbage collection and CPU cache thrashing.
The sharding (partitioning) and cache friendliness
reminded me of my own `LKRhash, a highly scalable hashtable`_.

.. _Sharding Containers\: Make Go Apps Computer-Friendly Again:
    https://dockercon2016.sched.org/event/70O6/sharding-containers-make-go-apps-computer-friendlyhellip
.. _Tesson:
    https://github.com/kobolog/tesson
.. _LKRhash, a highly scalable hashtable:
    https://nwcpp.org/june-2012.html

I missed `Microservices Best Practices`_.

.. _Microservices Best Practices:
    https://blog.codeship.com/microservices-best-practices/

The best hacks talks were also good.
"`Entropy`_ is a failure orchestration microservice for Docker platforms."
`Building serverless apps with Docker`_ was an experiment
in spinning up containers on-demand to handle incoming requests.

.. _Entropy:
    https://github.com/buildertools/entropy
.. _Building serverless apps with Docker:
    https://blog.docker.com/2016/06/building-serverless-apps-with-docker/

Exhibition Hall
---------------

Most of the dozens of `sponsors and exhibitors`_ had booths in the Exhibition Hall.
There were an awful lot of people
selling monitoring, hosting, storage, networking, and security.

.. _sponsors and exhibitors:
    http://web.archive.org/web/20161121204237/http://2016.dockercon.com/sponsors

.. _permalink:
    /blog/2016/06/21/DockerCon2016.html
