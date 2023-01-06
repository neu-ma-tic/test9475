.. pm2 service guide

==============================================
Setting up auto-restart using pm2 on Linux
==============================================

.. note:: This guide is for setting up PM2 on a Linux environment. This guide assumes that you already have a working Red instance.

--------------
Installing PM2
--------------

Start by installing Node.JS and NPM via your favorite package distributor. From there run the following command:

:code:`npm install pm2 -g`

After PM2 is installed, run the following command to enable your Red instance to be managed by PM2. Replace the brackets with the required information.
You can add additional Red based arguments after the instance, such as :code:`--dev`.

.. code-block:: none

    pm2 start redbot --name "<Insert a name here>" --interpreter "<Location to your Python Interpreter>" --interpreter-args "-O" -- <Red Instance> --no-prompt

.. code-block:: none

    Arguments to replace.

    <Insert a name here>
    A name to identify the bot within pm2, this is not your Red instance.

    <Location to your Python Interpreter>
    The location of your Python interpreter, to find out where that is use the following command inside activated venv:
    which python

    <Red Instance>
    The name of your Red instance.

------------------------------
Ensuring that PM2 stays online
------------------------------

To make sure that PM2 stays online and persistence between machine restarts, run the following commands:

:code:`pm2 save` & :code:`pm2 startup`
