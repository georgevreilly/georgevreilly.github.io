---
title: "Jenkins #2: EC2 Slaves"
date: "2017-02-05"
permalink: "/blog/2017/02/05/Jenkins02-EC2Slaves.html"
tags: [jenkins, metabrite]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/

The “slave” terminology is unfortunate,
but the utility of running a Jenkins build on a node that you've configured
at Amazon's EC2 is undeniable.

`#2 in a series on Jenkins Pipelines 
</blog/2017/02/04/Jenkins01-MigratingToPipelines.html>`_

We needed to install system packages on our build nodes,
such as Docker or Postgres.
For obvious reasons,
CloudBees—our Jenkins hosting provider—won't let you do that on their systems.
You must provide your own build nodes,
where you are free to install whatever you like.

We already use Amazon Web Services,
so we chose to configure our CloudBees account with EC2 slaves.
We had a long and fruitless detour through `On-Premise Executors`__,
which I will not detail here.

Ultimately, it turns out to be straightforward to `create and manage EC2 slaves`__.

Create an AMI
~~~~~~~~~~~~~

First, build a custom Amazon Machine Image (AMI).

* Launch a new Instance from the EC2 Console and choose a base AMI.
* We used ‘Ubuntu Server 16.04 LTS (HVM), SSD Volume Type’ as our base.
* Choose a suitable `instance type`__, such as ``m4.large``.
* Pick the right amount of storage; e.g., 12GB SSD.
  This can be overridden later.
* Configure the Security Group.

  - You *must* open up SSH on port 22 for the Jenkins Master to control the node.
  - You should lock down the Source to known IP addresses so that you're not open to the world.

* Launch your new Instance and install whatever software you want baked in.

__ https://go.cloudbees.com/docs/cloudbees-documentation/dev-at-cloud/index.html#_on_premise_executors
__ https://www.cloudbees.com/blog/setting-jenkins-ec2-slaves
__ https://aws.amazon.com/ec2/instance-types/

Here's the script we use to provision Ubuntu 16.04.
We SSH into the instance, then run this script.

.. code-block:: bash

    #!/bin/bash
    # Provision an Ubuntu 16.04 AMI for MetaBrite CI and Jenkins

    echo "Adding PPAs"
    # jo: JSON output from shell: https://github.com/jpmens/jo
    sudo apt-add-repository ppa:duggan/jo --yes

    echo "Updating package list"
    sudo apt-get update -q

    echo "Install Docker"
    curl -sSL https://get.docker.com/ | sh                      ➊ 

    echo "Installing Ubuntu packages"
    sudo apt-get --yes install \
        build-essential default-jre \                           ➋ 
        git vim wget \
        paperkey gnupg \                                        ➌ 
        libffi-dev libpq-dev libxslt1-dev libyaml-dev \
        python libpython2.7-dev python-dev python-lxml  \
        postgresql python-psycopg2 \
        jo jq \
        unzip zip

    echo "Installing Python packages"                           ➍ 
    curl -sSL --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo -H python2.7
    sudo -H pip install --upgrade virtualenvwrapper setuptools  ➎ 

    KNOWN_HOSTS=~/.ssh/known_hosts
    echo "Adding GitHub to $KNOWN_HOSTS"
    mkdir -p ~/.ssh/                                            ➏ 
    touch $KNOWN_HOSTS
    ssh-keyscan -H github.com >> $KNOWN_HOSTS                   ➐ 
    chmod 600 $KNOWN_HOSTS

1. This installs the latest stable Docker package,
   which is more recent than the packages supplied in the Ubuntu LTS.
2. The ``default-jre`` package is needed to run the Jenkins Slave JAR.
   We work a lot with Python 2.7;
   the packages that you need are probably different.
3. We'll have more to say about handling secrets at build time with Paperkey__ in a future post.
4. We also want the latest Pip__ for managing Python packages,
   in preference to the older system ``python-pip`` package.
   The ``-H`` argument to ``sudo`` sets ``$HOME`` to the `target user (root)`__.
5. We install up-to-date system-level virtualenv__ (via virtualenvwrapper__) and setuptools__.
   We have all that we need to install all other Python packages
   into virtual environments at build time.
6. We do *not* install a private SSH key for GitHub.
   (We did at first, but there's a better way to handle this.)
7. We `establish GitHub as a known host`__ using ``ssh-keyscan``.
   This is needed to prevent Git+SSH saying that the authenticity of the host
   can't be established and asking if we want to continue.
   This would be a major problem in a non-interactive build.
   Note: `GitHub's SSH key fingerprints`__ are not being verified here.

__ https://www.jabberwocky.com/software/paperkey/
__ https://pip.pypa.io/
__ https://stackoverflow.com/questions/27870003/pip-install-please-check-the-permissions-and-owner-of-that-directory
__ https://virtualenv.pypa.io/
__ https://virtualenvwrapper.readthedocs.io/
__ https://setuptools.readthedocs.io/en/latest/
__ https://github.com/wercker/step-add-to-known_hosts
__ https://help.github.com/articles/github-s-ssh-key-fingerprints/

After you've installed everything you need in this EC2 instance,
you need to `create a new AMI from the instance`__.

__ https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html

Configure the Amazon EC2 Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your AMI is available at AWS, you can configure Jenkins.
Go to Manage Jenkins > Configure System, then scroll down to Cloud > Amazon EC2.
(You may need to install the `Amazon EC2 plugin`__.)

You'll need an AWS Access Key/Secret Key pair from IAM.
You'll also need an SSH keypair so that Jenkins can SSH into your EC2 instance;
don't lose this or you'll never be able to SSH into your instance to debug it.

The `Setting Up Jenkins EC2 Slaves`_ article covers most of this.
The other pieces that you need to know:

* AMI Type > *Root command prefix*: ``sudo``
* *Labels*: whatever makes sense for you. We use ``ubuntu`` for our AMI.
* (Advanced) *Number of Executors*: 1 executor per vCPU seems to work well.
* (Advanced): *Block device mapping*: if you run out of disk space, you can increase it here.
  It's the number immediately after the snapshot name.
* *Init script*: use the following:

.. code-block:: bash

    #!/bin/bash
    # based on https://github.com/jenkinsci/ec2-plugin/blob/master/src/main/webapp/AMI-Scripts/ubuntu-ami-setup.sh

    echo "Downloading boot script"                              ➊ 
    sudo curl https://<JENKINS_MASTER>/plugin/ec2/AMI-Scripts/ubuntu-init.py -o /usr/bin/userdata
    sudo chmod +x /usr/bin/userdata

    echo "Adding boot script to run after boot is complete"     ➋ 
    sudo sed -i '/^[^#]/ s/exit 0/python \/usr\/bin\/userdata\n&/' /etc/rc.local

1. Adjust ``<JENKINS_MASTER>``. You may need to change ``https`` to ``http``.
2. The Init Script is run once, installing ``ubuntu-init.py``
   as a boot script at ``/etc/rc.local``.

Let's examine the `ubuntu-init.py`__ boot script.
You don't need to copy this, as it's available from your Jenkins Master.

.. code-block:: python

    #!/usr/bin/python
    import os
    import httplib
    import string

    # To install run:
    # sudo wget http://$JENKINS_URL/plugin/ec2/AMI-Scripts/ubuntu-init.py -O /usr/bin/userdata
    # sudo chmod +x /etc/init.d/userdata
    # add the following line to /etc/rc.local "python /usr/bin/userdata"

    # If java is installed it will be zero
    # If java is not installed it will be non-zero
    hasJava = os.system("java -version")

    if hasJava != 0:
        os.system("sudo apt-get update")
        os.system("sudo apt-get install openjdk-7-jre -y")      ➊ 

    conn = httplib.HTTPConnection("169.254.169.254")            ➋ 
    conn.request("GET", "/latest/user-data")
    response = conn.getresponse()
    userdata = response.read()

    args = string.split(userdata, "&")
    jenkinsUrl = ""
    slaveName = ""

    for arg in args:
        if arg.split("=")[0] == "JENKINS_URL":
            jenkinsUrl = arg.split("=")[1]
        if arg.split("=")[0] == "SLAVE_NAME":
            slaveName = arg.split("=")[1]

    os.system("wget " + jenkinsUrl + "jnlpJars/slave.jar -O slave.jar")     ➌ 
    os.system("java -jar slave.jar -jnlpUrl " + jenkinsUrl + "computer/" + slaveName + "/slave-agent.jnlp")
    ➍ 

1. Note that installing ``openjdk-7-jre`` will not work on stock Ubuntu 16.04,
   as ``openjdk-8-jre`` is now current.
   This is why we provisioned the AMI with ``default-jre``.
2. This script reads the `instance metadata`__ to discover its configuration.
   The Jenkins Master supplied this when it started the instance.
3. Download ``slave.jar`` from the Jenkins Master;
   run it pointing back to the Master node.
4. This boot process never exits.
   The slave code will continue running until the EC2 instance is stopped.

.. _Setting Up Jenkins EC2 Slaves:
    https://www.cloudbees.com/blog/setting-jenkins-ec2-slaves
__ https://wiki.jenkins-ci.org/display/JENKINS/Amazon+EC2+Plugin
__ https://github.com/jenkinsci/ec2-plugin/blob/master/src/main/webapp/AMI-Scripts/ubuntu-init.py
__ https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

In your Pipeline scripts, be sure to use the *label* you configured above
in your ``node`` blocks:

.. code-block:: groovy

    node('ubuntu') {                        ➊ 
        timestamps {
            ansiColor('xterm') {
                stage("Source Checkout") {
                    checkout scm
                    // …

Jenkins will automatically start up an EC2 instance running your AMI,
or use an existing one if it has enough capacity.

.. _permalink:
    /blog/2017/02/05/Jenkins02-EC2Slaves.html
