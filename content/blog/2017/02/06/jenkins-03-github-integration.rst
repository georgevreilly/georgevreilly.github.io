---
title: "Jenkins #3: GitHub Integration"
date: "2017-02-06"
permalink: "/blog/2017/02/06/Jenkins03-GitHubIntegration.html"
tags: [jenkins, metabrite]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/

Much of our code is in one large GitHub repository,
from which several different applications are built.
When changes are pushed to the *master* branch,
we want only the applications in affected directories to be built.
This was not easy to get right with “Pipeline script from SCM” builds.

`#3 in a series on Jenkins Pipelines 
</blog/2017/02/04/Jenkins01-MigratingToPipelines.html>`_

Configuration
~~~~~~~~~~~~~

* To get builds to trigger upon a push to GitHub,
  you need to `configure a webhook`__ pointing to your Jenkins Master.
* `Create an SSH key`__ for Jenkins/GitHub.
  A passphrase is recommended.

  - *Public Key*: Upload the `SSH public key to GitHub`__
  - *Private Key*: Go to Jenkins > Credentials > SSH Username with Private Key.
    Add the private key with a meaningful ID
  - In your AMI__, make sure that you've run
    ``ssh-keyscan -H github.com >> ~/.ssh/known_hosts``
    to prevent Git from asking about the authenticity of github.com
  - Do not install the SSH private key into your AMI

* In your Jenkins job configuration:
  
  - Build Trigger > Build when a change is pushed to GitHub
  - Pipeline > Definition > Pipeline script from SCM
  - Repository URL: ``git@github.com:ORGANIZATION/REPOSITORY.git``
    (the SSH form of the URL, not the HTTPS)
  - Credentials: the ID of your GitHub SSH credential
  - To build only when changes affect the ``/foo`` and ``/bar`` directories of your repository:
    Additional Behaviors > Polling ignores commits in certain paths > Included Regions::

      ^foo/.*
      ^bar/.*

  - Script Path: path-to-your-Jenkinsfile

Pipeline (Jenkinsfile)
~~~~~~~~~~~~~~~~~~~~~~

* Use the ``checkout scm`` step, not the ``git`` step.
  The former plays well with GitHub polling; the latter doesn't.
* If you need to clean up your workspace, do not remove the ``.git`` directory.
  Otherwise, you are likely to have unnecessary builds as the Git Plugin
  doesn't do polling well without a persistent workspace.
* Do not use ``sshagent`` to check out code from GitHub.
  The SSH credential configured on the Repository URL will be used during ``checkout scm``.

__ https://support.cloudbees.com/hc/en-us/articles/224543927-GitHub-webhook-configuration
__ https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
__ https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
__ /blog/2017/02/05/Jenkins02-EC2Slaves.html

.. _permalink:
    /blog/2017/02/06/Jenkins03-GitHubIntegration.html
