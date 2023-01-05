.. _install-debian-11:

====================================
Installing Red on Debian 11 Bullseye
====================================

.. include:: _includes/supported-arch-x64+aarch64+armv7l.rst

.. include:: _includes/linux-preamble.rst

-------------------------------
Installing the pre-requirements
-------------------------------

Debian 11 "Bullseye" has all required packages available in official repositories. Install them
with apt:

.. prompt:: bash

    sudo apt update
    sudo apt -y install python3 python3-dev python3-venv python3-pip git openjdk-11-jre-headless build-essential nano

.. Include common instructions:

.. include:: _includes/create-env-with-venv.rst

.. include:: _includes/install-and-setup-red-unix.rst
