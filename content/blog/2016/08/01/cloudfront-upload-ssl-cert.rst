---
title: "Creating External SSL Certificates for CloudFront"
date: "2016-08-01"
permalink: "/blog/2016/08/01/CreatingExternalSSLCertificatesForCloudFront.html"
tags: [tech, ssl, aws, til]
---



I needed to create a wildcard SSL certificate and upload it to `AWS CloudFront`__ today.

First, generate a 2048-bit private key. This will prompt you for a passphrase:

.. code-block:: bash

    $ openssl genrsa -des3 -out example.key 2048

Check which signature algorithm was used (SHA-256 is recommended):

.. code-block:: bash

    $ openssl req -in example.csr -noout -text

Transform the private key to PEM format:

.. code-block:: bash

    $ openssl rsa -outform PEM -in example.key -out example.pem

Generate a Certificate Signing Request. Note the ``*`` in the server FQDN:

.. code-block:: bash

    $ openssl req -new -key example.key -out example.csr

    Country Name (2 letter code) [AU]:US
    State or Province Name (full name) [Some-State]:Washington
    Locality Name (eg, city) []:Seattle
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:Example GmbH
    Organizational Unit Name (eg, section) []:
    Common Name (e.g. server FQDN or YOUR name) []:*.example.com
    Email Address []:

    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:

Upload the CSR to your Certificate Authority and generate a signed certificate.
We used SSL.com__.

Be sure to save the keys and certificates in a secure place.
The private key is a *secret*: treat it as such.

Finally, `upload the certificate to IAM (AWS Identity and Access Management)`__:

.. code-block:: bash

    $ aws iam upload-server-certificate \
        --server-certificate-name 'Example_Wildcard_Cert' \
        --certificate-body file://STAR_example_com.crt \
        --private-key file://example.pem \
        --certificate-chain file://ca-chain-amazon.crt \
        --path /cloudfront/production/

Note the ``--path`` argument, which is required for CloudFront distributions.

Bryce Fisher-Fleig has more__.
(I wish I had discovered his post this morning.)

__ https://aws.amazon.com/cloudfront/
__ https://www.ssl.com/
__ http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs_manage.html#UploadSignedCert
__ https://bryce.fisher-fleig.org/blog/setting-up-ssl-on-aws-cloudfront-and-s3/

.. _permalink:
    /blog/2016/08/01/CreatingExternalSSLCertificatesForCloudFront.html
