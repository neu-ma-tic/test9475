.. _windows-install-guide:

=========================
Installing Red on Windows
=========================

-------------------------------
Installing the pre-requirements
-------------------------------

Please install the pre-requirements by following instructions from one of the following subsections.

The pre-requirements are:
 - Python 3.8.1 or greater
 - Pip 18.1 or greater
 - Git 2.11+
 - Java Runtime Environment 11 (for audio support)

We also recommend installing some basic compiler tools, in case our dependencies don't provide
pre-built "wheels" for your architecture.

.. contents:: Choose a method of installing pre-requirements:
    :local:

----

*********************************************
Using PowerShell and Chocolatey (recommended)
*********************************************

To install via PowerShell, search "powershell" in the Windows start menu,
right-click on it and then click "Run as administrator".

Then run each of the following commands:

.. code-block:: none

    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    choco upgrade git --params "/GitOnlyOnPath /WindowsTerminal" -y
    choco upgrade visualstudio2019-workload-vctools -y
    choco upgrade python3 -y

For Audio support, you should also run the following command before exiting:

.. code-block:: none

    choco upgrade adoptopenjdk11jre -y


From here, exit the prompt then continue onto `creating-venv-windows`.

----

********************************
Manually installing dependencies
********************************

.. attention:: There are additional configuration steps required which are
               not documented for installing dependencies manually.
               These dependencies are only listed seperately here for
               reference purposes.

* `MSVC Build tools <https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2019>`_

* `Python 3.8.1 or greater <https://www.python.org/downloads/>`_

.. attention:: Please make sure that the box to add Python to PATH is CHECKED, otherwise
               you may run into issues when trying to run Red.

* `Git 2.11+ <https://git-scm.com/download/win>`_

.. attention:: Please choose the option to "Git from the command line and also from 3rd-party software" in Git's setup.

* `Java 11 <https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot>`_ - needed for Audio

From here, continue onto `creating-venv-windows`.

----

.. _creating-venv-windows:

------------------------------
Creating a Virtual Environment
------------------------------

.. tip::

    If you want to learn more about virtual environments, see page: `about-venvs`.

We require installing Red into a virtual environment. Don't be scared, it's very
straightforward.

First, choose a directory where you would like to create your virtual environment. It's a good idea
to keep it in a location which is easy to type out the path to. From now, we'll call it
``redenv`` and it will be located in your home directory.

Start with opening a command prompt (open Start, search for "command prompt", then click it).

.. note:: 

    You shouldn't run command prompt as administrator when creating your virtual environment, or
    running Red.

.. warning::

    These commands will not work in PowerShell - you have to use command prompt as said above.

Then create your virtual environment with the following command

.. code-block:: none

    py -3.8 -m venv "%userprofile%\redenv"

And activate it with the following command

.. code-block:: none

    "%userprofile%\redenv\Scripts\activate.bat"

.. important::

    You must activate the virtual environment with the above command every time you open a new
    Command Prompt to run, install or update Red.


.. _installing-red-windows:

--------------
Installing Red
--------------

.. attention:: You may need to restart your computer after installing dependencies
               for the PATH changes to take effect.

Run **one** of the following set of commands, depending on what extras you want installed

  * Normal installation:

    .. code-block:: none

        python -m pip install -U pip setuptools wheel
        python -m pip install -U Red-DiscordBot

  * With PostgreSQL support:

    .. code-block:: none

        python -m pip install -U pip setuptools wheel
        python -m pip install -U Red-DiscordBot[postgres]

--------------------------
Setting Up and Running Red
--------------------------

After installation, set up your instance with the following command:

.. code-block:: none

    redbot-setup

This will set the location where data will be stored, as well as your
storage backend and the name of the instance (which will be used for
running the bot).

Once done setting up the instance, run the following command to run Red:

.. code-block:: none

    redbot <your instance name>

It will walk through the initial setup, asking for your token and a prefix.
You can find out how to obtain a token with
:dpy_docs:`this guide <discord.html#creating-a-bot-account>`,
section "Creating a Bot Account".

.. tip::
   If it's the first time you're using Red, you should check our `getting-started` guide
   that will walk you through all essential information on how to interact with Red.
