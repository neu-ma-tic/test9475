.. V3 Shared API Key Reference

===============
Shared API Keys
===============

Red has a central API key storage utilising the core bots config. This allows cog creators to add a single location to store API keys for their cogs which may be shared between other cogs.

There needs to be some consistency between cog creators when using shared API keys between cogs. To help make this easier service should be all **lowercase** and the key names should match the naming convention of the API being accessed.

Example:

Twitch has a client ID and client secret so a user should be asked to input

``[p]set api twitch client_id,1234ksdjf client_secret,1234aldlfkd``

and when accessed in the code it should be done by 

.. code-block:: python

    await self.bot.get_shared_api_tokens("twitch")

Each service has its own dict of key, value pairs for each required key type. If there's only one key required then a name for the key is still required for storing and accessing.

Example:

``[p]set api youtube api_key,1234ksdjf``

and when accessed in the code it should be done by 

.. code-block:: python

    await self.bot.get_shared_api_tokens("youtube")


***********
Basic Usage
***********

.. code-block:: python

    class MyCog:
        @commands.command()
        async def youtube(self, ctx, user: str):
            youtube_keys = await self.bot.get_shared_api_tokens("youtube")
            if youtube_keys.get("api_key") is None:
                return await ctx.send("The YouTube API key has not been set.")
            # Use the API key to access content as you normally would


***************
Event Reference
***************

.. function:: on_red_api_tokens_update(service_name, api_tokens)

    Dispatched when service's api keys are updated.

    :param service_name: Name of the service.
    :type service_name: :class:`str`
    :param api_tokens: New Mapping of token names to tokens. This contains api tokens that weren't changed too.
    :type api_tokens: Mapping[:class:`str`, :class:`str`]


*********************
Additional References
*********************

.. py:currentmodule:: redbot.core.bot

.. automethod:: Red.get_shared_api_tokens

.. automethod:: Red.set_shared_api_tokens

.. automethod:: Red.remove_shared_api_tokens

.. automethod:: Red.remove_shared_api_services
