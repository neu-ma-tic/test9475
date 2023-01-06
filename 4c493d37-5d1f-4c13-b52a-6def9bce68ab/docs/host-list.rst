.. source: https://gist.github.com/Twentysix26/cb4401c6e507782aa6698e9e470243ed

.. _host-list:

=============
VPS providers
=============

.. note::
    This doc is written for the :ref:`hosting section <getting-started-hosting>`
    of the :ref:`getting started <getting-started>` guide. Please take a look
    if you don't know how to host Red on a VPS.

This is a list of the recommended VPS providers.

.. warning::
    Please be aware that a Linux server is controlled through a command line.
    If you don't know Unix basics, please take a look at `this guide
    <https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-basics>`_
    from DigitalOcean which will introduce you to the Linux basics.

-------------
Linux hosting
-------------

+------------------------------------+------------------------------------------------------+
|Link                                |Description                                           |
+====================================+======================================================+
|`Scaleway                           |Incredibly cheap but powerful VPSes, owned by         |
|<https://www.scaleway.com/>`_       |`<https://online.net/>`_, based in Europe.            |
+------------------------------------+------------------------------------------------------+
|`DigitalOcean                       |US-based cheap VPSes. The gold standard. Locations    |
|<https://www.digitalocean.com/>`_   |available world wide.                                 |
+------------------------------------+------------------------------------------------------+
|`OVH <https://www.ovh.co.uk/>`_     |Cheap VPSes, used by many people. French and Canadian |
|                                    |locations available.                                  |
+------------------------------------+------------------------------------------------------+
|`Time4VPS                           |Cheap VPSes, seemingly based in Lithuania.            |
|<https://www.time4vps.eu/>`_        |                                                      |
+------------------------------------+------------------------------------------------------+
|`Linode <https://www.linode.com/>`_ |More cheap VPSes!                                     |
+------------------------------------+------------------------------------------------------+
|`Vultr <https://www.vultr.com/>`_   |US-based, DigitalOcean-like.                          |
+------------------------------------+------------------------------------------------------+

------
Others
------

+-------------------------------------+-----------------------------------------------------+
|Link                                 |                                                     |
+=====================================+=====================================================+
|`AWS <https://aws.amazon.com/>`_     |Amazon Web Services. Free for a year (with certain   |
|                                     |limits), but very pricey after that.                 |
+-------------------------------------+-----------------------------------------------------+
|`Google Cloud                        |Same as AWS, but it's Google.                        |
|<https://cloud.google.com/compute/>`_|                                                     |
+-------------------------------------+-----------------------------------------------------+
|`Microsoft Azure                     |Same as AWS, but it's Microsoft.                     |
|<https://azure.microsoft.com>`_      |                                                     |
+-------------------------------------+-----------------------------------------------------+
|`Oracle Cloud                        |Same as AWS, but it's Oracle.                        |
|<https://oracle.com/cloud/>`_        |                                                     |
+-------------------------------------+-----------------------------------------------------+
|`LowEndBox <http://lowendbox.com/>`_ |A curator for lower specced servers.                 |
+-------------------------------------+-----------------------------------------------------+

------------
Self-hosting
------------

You can always self-host on your own hardware.
A Raspberry Pi 3 will be more than sufficient for small to medium sized bots.

For bigger bots, you can build your own server PC for usage, or buy a rack
server. Any modern hardware should work 100% fine.

------------
Free hosting
------------

| `Google Cloud Compute Engine <https://cloud.google.com/free/docs/gcp-free-tier>`_,
  `Oracle Cloud Compute <https://oracle.com/cloud/free/#always-free>`_ and
  `AWS EC2 <https://aws.amazon.com/free/>`_ have free tier VPSes suitable for small bots.

| **Note:** AWS EC2's free tier does not last forever - it's a 12 month trial.
| Additionally, new Google Cloud customers get a $300 credit which is valid
  for 12 months.

Other than that... no. There is no good free VPS hoster, outside of
persuading somebody to host for you, which is incredibly unlikely.
