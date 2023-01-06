.. _economy:

=======
Economy
=======

This is the cog guide for the economy cog. You will
find detailed docs about usage and commands.

``[p]`` is considered as your prefix.

.. note:: To use this cog, load it by typing this::

        [p]load economy

.. _economy-usage:

-----
Usage
-----

Get rich and have fun with imaginary currency!


.. _economy-commands:

--------
Commands
--------

.. _economy-command-bank:

^^^^
bank
^^^^

**Syntax**

.. code-block:: none

    [p]bank 

**Description**

Base command to manage the bank.

.. _economy-command-bank-balance:

""""""""""""
bank balance
""""""""""""

**Syntax**

.. code-block:: none

    [p]bank balance [user]

**Description**

Show the user's account balance.

Example:
    - ``[p]bank balance``
    - ``[p]bank balance @Twentysix``

**Arguments**

- ``<user>`` The user to check the balance of. If omitted, defaults to your own balance.

.. _economy-command-bank-set:

""""""""
bank set
""""""""

.. note:: |admin-lock|

**Syntax**

.. code-block:: none

    [p]bank set <to> <creds>

**Description**

Set the balance of a user's bank account.

Putting + or - signs before the amount will add/remove currency on the user's bank account instead.

Examples:
    - ``[p]bank set @Twentysix 26`` - Sets balance to 26
    - ``[p]bank set @Twentysix +2`` - Increases balance by 2
    - ``[p]bank set @Twentysix -6`` - Decreases balance by 6

**Arguments**

- ``<to>`` The user to set the currency of.
- ``<creds>`` The amount of currency to set their balance to.

.. _economy-command-bank-transfer:

"""""""""""""
bank transfer
"""""""""""""

**Syntax**

.. code-block:: none

    [p]bank transfer <to> <amount>

**Description**

Transfer currency to other users.

This will come out of your balance, so make sure you have enough.

Example:
    - ``[p]bank transfer @Twentysix 500``

**Arguments**

- ``<to>`` The user to give currency to.
- ``<amount>`` The amount of currency to give.

.. _economy-command-economyset:

^^^^^^^^^^
economyset
^^^^^^^^^^

.. note:: |admin-lock|

**Syntax**

.. code-block:: none

    [p]economyset 

**Description**

Base command to manage Economy settings.

.. _economy-command-economyset-paydayamount:

"""""""""""""""""""""""
economyset paydayamount
"""""""""""""""""""""""

**Syntax**

.. code-block:: none

    [p]economyset paydayamount <creds>

**Description**

Set the amount earned each payday.

Example:
    - ``[p]economyset paydayamount 400``

**Arguments**

- ``<creds>`` The new amount to give when using the payday command. Default is 120.

.. _economy-command-economyset-paydaytime:

"""""""""""""""""""""
economyset paydaytime
"""""""""""""""""""""

**Syntax**

.. code-block:: none

    [p]economyset paydaytime <duration>

**Description**

Set the cooldown for the payday command.

Examples:
    - ``[p]economyset paydaytime 86400``
    - ``[p]economyset paydaytime 1d``

**Arguments**

- | ``<duration>`` The new duration to wait in between uses of payday. Default is 5 minutes.
  | Accepts: seconds, minutes, hours, days, weeks (if no unit is specified, the duration is assumed to be given in seconds)

.. _economy-command-economyset-rolepaydayamount:

"""""""""""""""""""""""""""
economyset rolepaydayamount
"""""""""""""""""""""""""""

**Syntax**

.. code-block:: none

    [p]economyset rolepaydayamount <role> <creds>

**Description**

Set the amount earned each payday for a role.

Set to 0 will remove the custom payday for that role instead.

Only available when not using a global bank.

Example:
    - ``[p]economyset rolepaydayamount @Members 400``

**Arguments**

- ``<role>`` The role to assign a custom payday amount to.
- ``<creds>`` The new amount to give when using the payday command.

.. _economy-command-economyset-showsettings:

"""""""""""""""""""""""
economyset showsettings
"""""""""""""""""""""""

**Syntax**

.. code-block:: none

    [p]economyset showsettings 

**Description**

Shows the current economy settings

.. _economy-command-economyset-slotmax:

""""""""""""""""""
economyset slotmax
""""""""""""""""""

**Syntax**

.. code-block:: none

    [p]economyset slotmax <bid>

**Description**

Set the maximum slot machine bid.

Example:
    - ``[p]economyset slotmax 50``

**Arguments**

- ``<bid>`` The new maximum bid for using the slot machine. Default is 100.

.. _economy-command-economyset-slotmin:

""""""""""""""""""
economyset slotmin
""""""""""""""""""

**Syntax**

.. code-block:: none

    [p]economyset slotmin <bid>

**Description**

Set the minimum slot machine bid.

Example:
    - ``[p]economyset slotmin 10``

**Arguments**

- ``<bid>`` The new minimum bid for using the slot machine. Default is 5.

.. _economy-command-economyset-slottime:

"""""""""""""""""""
economyset slottime
"""""""""""""""""""

**Syntax**

.. code-block:: none

    [p]economyset slottime <duration>

**Description**

Set the cooldown for the slot machine.

Examples:
    - ``[p]economyset slottime 10``
    - ``[p]economyset slottime 10m``

**Arguments**

- | ``<duration>`` The new duration to wait in between uses of the slot machine. Default is 5 seconds.
  | Accepts: seconds, minutes, hours, days, weeks (if no unit is specified, the duration is assumed to be given in seconds)

.. _economy-command-leaderboard:

^^^^^^^^^^^
leaderboard
^^^^^^^^^^^

**Syntax**

.. code-block:: none

    [p]leaderboard [top=10] [show_global=False]

**Description**

Print the leaderboard.

Defaults to top 10.

Examples:
    - ``[p]leaderboard``
    - ``[p]leaderboard 50`` - Shows the top 50 instead of top 10.
    - ``[p]leaderboard 100 yes`` - Shows the top 100 from all servers.

**Arguments**

- ``<top>`` How many positions on the leaderboard to show. Defaults to 10 if omitted.
- ``<show_global>`` Whether to include results from all servers. This will default to false unless specified.

.. _economy-command-payday:

^^^^^^
payday
^^^^^^

**Syntax**

.. code-block:: none

    [p]payday 

**Description**

Get some free currency.

The amount awarded and frequency can be configured.

.. _economy-command-payouts:

^^^^^^^
payouts
^^^^^^^

**Syntax**

.. code-block:: none

    [p]payouts 

**Description**

Show the payouts for the slot machine.

.. _economy-command-slot:

^^^^
slot
^^^^

**Syntax**

.. code-block:: none

    [p]slot <bid>

**Description**

Use the slot machine.

Example:
    - ``[p]slot 50``

**Arguments**

- ``<bid>`` The amount to bet on the slot machine. Winning payouts are higher when you bet more.
