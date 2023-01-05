[![](https://scdn.rapidapi.com/RapidAPI_banner.png)](https://rapidapi.com/package/DiscordBot/functions?utm_source=RapidAPIGitHub_DiscordBotFunctions&utm_medium=button&utm_content=RapidAPI_GitHub)

# DiscordBot Package
DiscordBot
* Domain: [DiscordBot](http://http:/discordapp.com)
* Credentials: clientId, clientSecret, accessToken

## How to get credentials: 
0. Go to [Discord website](http:/discordapp.com)
1. Log in or create a new account
2. [Register an app](https://discordapp.com/developers/applications/me)
3. After creation your app you will see Client ID and Client Secret
4. "Create A Bot User" for your application and provide this bot proper privileges
5. Get Bot access token from you [Application page](https://discordapp.com/developers/applications/me)

## Custom datatypes: 
 |Datatype|Description|Example
 |--------|-----------|----------
 |Datepicker|String which includes date and time|```2016-05-28 00:00:00```
 |Map|String which includes latitude and longitude coma separated|```50.37, 26.56```
 |List|Simple array|```["123", "sample"]``` 
 |Select|String with predefined values|```sample```
 |Array|Array of objects|```[{"Second name":"123","Age":"12","Photo":"sdf","Draft":"sdfsdf"},{"name":"adi","Second name":"bla","Age":"4","Photo":"asfserwe","Draft":"sdfsdf"}] ```
 

## DiscordBot.getAccessToken
Get access token

| Field       | Type       | Description
|-------------|------------|----------
| clientId    | credentials| Client Id obtained from Discord
| clientSecret| credentials| Client secret obtained from Discord
| code        | String     | Code provided by the user
| redirectUri | String     | Redirect uri for your application

## DiscordBot.getAppInfo
Returns the bot's OAuth2 application info.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord

## DiscordBot.getSingleChannel
Guild channels represent an isolated set of users and messages within a Guild.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel

## DiscordBot.updateChannel
Update a channels settings.

| Field           | Type       | Description
|-----------------|------------|----------
| accessToken     | credentials| Access token for your bot received from Discord
| channelId       | Number     | Id of the guild channel
| channelName     | String     | 2-100 character channel name
| channelPosition | Number     | The position of the channel in the left-hand listing
| channelTopic    | String     | 0-1024 character channel topic
| channelBitrate  | Number     | The bitrate (in bits) of the voice channel; 8000 to 96000 (128000 for VIP servers)
| channelUserLimit| Number     | The user limit of the voice channel; 0 refers to no limit, 1 to 99 refers to a user limit

## DiscordBot.deleteChannel
Delete a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel

## DiscordBot.getChannelMessages
Returns the messages for a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| aroundId   | Number     | Get messages around this message ID
| beforeId   | Number     | Get messages before this message ID
| afterId    | Number     | Get messages after this message ID
| limit      | Number     | Max number of messages to return (1-100)

## DiscordBot.getChannelSingleMessage
Returns the message from a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| messageId  | Number     | Id of the message

## DiscordBot.createReaction
Create a reaction for the message.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| messageId  | Number     | Id of the message
| emoji      | String     | Emoji

## DiscordBot.deleteOwnReaction
Delete a reaction the current user has made for the message.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| messageId  | Number     | Id of the message
| emoji      | String     | Emoji

## DiscordBot.getReactions
Get a list of users that reacted with this emoji.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| messageId  | Number     | Id of the message
| emoji      | String     | Emoji

## DiscordBot.deleteUserReaction
Delete a reaction the user with provided userId has made for the message.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| messageId  | Number     | Id of the message
| emoji      | String     | Emoji
| userId     | Number     | Id of the user

## DiscordBot.deleteAllReactions
Delete all reactions for the message.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| messageId  | Number     | Id of the message

## DiscordBot.getChannelInvites
Returns a list of invite objects (with invite metadata) for the channel. 

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel

## DiscordBot.createChannelInvite
Create a new invite object for the channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| maxAge     | Number     | Duration of invite in seconds before expiry, or 0 for never
| maxUses    | Number     | Max number of uses or 0 for unlimited
| temporary  | Boolean    | Whether this invite only grants temporary membership. Default: false
| unique     | Boolean    | If true, don't try to reuse a similar invite (useful for creating many unique one time use invites) Default: false

## DiscordBot.updateUserChannelPermissions
Edit the channel permission overwrites for a user in a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| userId     | Number     | Id of the user
| allow      | Number     | The bitwise value of all allowed permissions
| deny       | Number     | The bitwise value of all disallowed permissions

## DiscordBot.updateRoleChannelPermissions
Edit the channel permission overwrites for a role in a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| roleId     | Number     | Id of the role
| allow      | Number     | The bitwise value of all allowed permissions
| deny       | Number     | The bitwise value of all disallowed permissions

## DiscordBot.deleteUserChannelPermission
Delete the channel permission overwrites for a user in a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| userId     | Number     | Id of the user

## DiscordBot.deleteRoleChannelPermission
Delete the channel permission overwrites for a role in a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| roleId     | Number     | Id of the role

## DiscordBot.createTriggerTypingIndicator
Post a typing indicator for the specified channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel

## DiscordBot.addPinnedChannelMessage
Pin a message in a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| messageId  | Number     | Id of the message in channel

## DiscordBot.getPinnedMessages
Get pinned messages in a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel

## DiscordBot.deletePinnedChannelMessage
Delete a pinned message in a channel.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the guild channel
| messageId  | Number     | Id of the message in channel

## DiscordBot.createGuild
Create a new guild.

| Field                           | Type       | Description
|---------------------------------|------------|----------
| accessToken                     | credentials| Access token for your bot received from Discord
| guildName                       | String     | Name of the guild (2-100 characters)
| guildRegion                     | String     | {voice_region.id} for voice
| guildIcon                       | File       | jpeg image for the guild icon
| guildVerificationLevel          | Number     | Guild verification level
| guildDefaultMessageNotifications| Number     | Default message notifications setting
| guildRoles                      | Array      | New guild roles
| guildChannels                   | Array      | New guild's channels

## DiscordBot.getGuild
Returns the new guild object for the given id.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.updateGuild
Updating existing guild.

| Field                           | Type       | Description
|---------------------------------|------------|----------
| accessToken                     | credentials| Access token for your bot received from Discord
| guildId                         | Number     | Id of the guild
| guildName                       | String     | Name of the guild (2-100 characters)
| guildRegion                     | String     | {voice_region.id} for voice
| guildIcon                       | File       | jpeg image for the guild icon
| guildVerificationLevel          | Number     | Guild verification level
| guildDefaultMessageNotifications| Number     | Default message notifications setting
| guildAfkTimeout                 | Number     | Afk timeout in seconds
| guildAfkChannelId               | String     | Id for afk channel
| guildSplash                     | File       | 128x128 jpeg image for the guild splash (VIP only)

## DiscordBot.getGuildChannels
Returns a list of guild channel objects.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.createGuildChannel
Returns a list of guild channel objects.

| Field                      | Type       | Description
|----------------------------|------------|----------
| accessToken                | credentials| Access token for your bot received from Discord
| guildId                    | Number     | Id of the guild
| channelName                | String     | Channel name (2-100 characters)
| channelType                | String     | voice or text(default)
| voiceChannelBitrate        | Number     | The bitrate (in bits) of the voice channel (voice only)
| voiceChannelUserLimit      | Number     | The user limit of the voice channel (voice only)
| channelPermissionsOverwrite| List       | The channel's permission overwrites

## DiscordBot.updateGuildChannelPositions
Modify the positions of a set of channel objects for the guild.

| Field         | Type       | Description
|---------------|------------|----------
| accessToken   | credentials| Access token for your bot received from Discord
| guildId       | Number     | Id of the guild
| channelId     | Number     | Id of the channel
| positionNumber| Number     | Sorting position of the channel

## DiscordBot.getGuildMembers
Returns a list of guild member objects that are members of the guild.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.getGuildMember
Returns a guild member object for the specified user.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| userId     | Number     | Id of the user

## DiscordBot.updateGuildMember
Modify attributes of a guild member.

| Field          | Type       | Description
|----------------|------------|----------
| accessToken    | credentials| Access token for your bot received from Discord
| guildId        | Number     | Id of the guild
| userId         | Number     | Id of the user
| memberNick     | String     | Value to set users nickname to
| memberRoles    | List       | Array of roles the member is assigned
| mute           | Boolean    | If the user is muted
| deaf           | Boolean    | If the user is deafened
| moveToChannelId| String     | Id of channel to move user to (if they are connected to voice)

## DiscordBot.addGuildMemberRole
Adds a role to a guild member.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| userId     | Number     | Id of the user
| roleId     | Number     | Id of the role

## DiscordBot.getGuildRoles
Returns a list of role objects for the guild.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.removeGuildMemberRole
removes added role to a guild member.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| userId     | Number     | Id of the user
| roleId     | Number     | Id of the role

## DiscordBot.createGuildRole
Create a new role for the guild.

| Field          | Type       | Description
|----------------|------------|----------
| accessToken    | credentials| Access token for your bot received from Discord
| guildId        | Number     | Id of the guild
| roleName       | String     | Name of the role
| rolePermissions| Number     | Bitwise of the enabled/disabled permissions
| roleColor      | Number     | RGB color value
| hoist          | Boolean    | Whether the role should be displayed separately in the sidebar
| mentionable    | Boolean    | Whether the role should be mentionable

## DiscordBot.updateGuildRolePositions
Modify the positions of a set of role objects for the guild.

| Field       | Type       | Description
|-------------|------------|----------
| accessToken | credentials| Access token for your bot received from Discord
| guildId     | Number     | Id of the guild
| roleId      | Number     | Id of the role
| rolePosition| Number     | sorting position of the role

## DiscordBot.updateGuildRole
Update existing role for the guild.

| Field          | Type       | Description
|----------------|------------|----------
| accessToken    | credentials| Access token for your bot received from Discord
| guildId        | Number     | Id of the guild
| roleId         | Number     | Id of the role
| roleName       | String     | Name of the role
| rolePermissions| Number     | Bitwise of the enabled/disabled permissions
| roleColor      | Number     | RGB color value
| hoist          | Boolean    | Whether the role should be displayed separately in the sidebar
| mentionable    | Boolean    | Whether the role should be mentionable

## DiscordBot.getGuildBans
Returns a list of user objects that are banned from this guild. 

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.createGuildBan
Create a guild ban, and optionally delete previous messages sent by the banned user.

| Field            | Type       | Description
|------------------|------------|----------
| accessToken      | credentials| Access token for your bot received from Discord
| guildId          | Number     | Id of the guild
| userId           | Number     | Id of the user
| deleteMessageDays| Number     | Number of days to delete messages for (0-7)

## DiscordBot.removeGuildBan
Remove a guild ban of the banned user.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| userId     | Number     | Id of the user

## DiscordBot.deleteGuildRole
Delete a guild role.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| roleId     | Number     | Id of the role

## DiscordBot.deleteGuild
Delete a guild permanently. User must be owner.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.getGuildPruneCount
Returns an object with one 'pruned' key indicating the number of members that would be removed in a prune operation. 

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| countDays  | Number     | Number of days to count prune for (1 or more)

## DiscordBot.startGuildPrune
Begin a prune operation.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| countDays  | Number     | Number of days to prune (1 or more)

## DiscordBot.getGuildVoiceRegions
Returns a list of voice region objects for the guild.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.getGuildInvites
Returns a list of invite objects (with invite metadata) for the guild. 

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.getGuildIntegrations
Returns a list of integration objects for the guild. 

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.createGuildIntegration
Attach an integration object from the current user to the guild.

| Field          | Type       | Description
|----------------|------------|----------
| accessToken    | credentials| Access token for your bot received from Discord
| guildId        | Number     | Id of the guild
| integrationType| String     | The integration type
| integrationId  | Number     | Id of the integration.

## DiscordBot.updateGuildIntegration
Modify the behavior and settings of a integration object for the guild.

| Field            | Type       | Description
|------------------|------------|----------
| accessToken      | credentials| Access token for your bot received from Discord
| guildId          | Number     | Id of the guild
| integrationId    | Number     | Id of the integration.
| expireBehavior   | Number     | The behavior when an integration subscription lapses
| expireGracePeriod| Number     | Period (in seconds) where the integration will ignore lapsed subscriptions
| enableEmoticons  | Boolean    | Whether emoticons should be synced for this integration (twitch only currently)

## DiscordBot.syncGuildIntegration
Sync an integration.

| Field        | Type       | Description
|--------------|------------|----------
| accessToken  | credentials| Access token for your bot received from Discord
| guildId      | Number     | Id of the guild
| integrationId| Number     | Id of the integration.

## DiscordBot.deleteGuildIntegration
Delete an integration.

| Field        | Type       | Description
|--------------|------------|----------
| accessToken  | credentials| Access token for your bot received from Discord
| guildId      | Number     | Id of the guild
| integrationId| Number     | Id of the integration.

## DiscordBot.getGuildEmbed
Returns the guild embed object.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.getInvite
Returns the invite object.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| inviteCode | String     | Code of the invite

## DiscordBot.deleteInvite
Delete the invite.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| inviteCode | String     | Code of the invite

## DiscordBot.getCurrentUser
Returns the user object of the requester's account.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord

## DiscordBot.getUser
Returns a user for a given user ID.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| userId     | Number     | Id of the user

## DiscordBot.updateCurrentUser
Returns the user object of the requester's account.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| username   | String     | New username
| avatar     | File       | JPEG avatar image

## DiscordBot.getCurrentUserGuilds
Returns a list of user guild objects the current user is a member of.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| beforeId   | Number     | Get guilds before this guild ID
| afterId    | Number     | Get guilds after this guild ID
| limit      | Number     | Max number of guilds to return (1-100)

## DiscordBot.leaveGuild
Leave a guild.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.getUserDms
Returns a list of DM channel objects.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord

## DiscordBot.createDm
Create a new DM channel with a user.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| recipientId| Number     | Id of the recipient

## DiscordBot.createGroupDm
Create a new DM channel with a user.

| Field       | Type       | Description
|-------------|------------|----------
| accessToken | credentials| Access token for your bot received from Discord
| accessTokens| List       | Access tokens of users that have granted your app the gdm.join scope
| nicks       | JSON       | Dictionary of user ids to their respective nicknames

## DiscordBot.getUsersConnections
Returns a list of connection objects.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord

## DiscordBot.getVoiceRegions
Returns an array of voice region objects that can be used when creating servers.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord

## DiscordBot.createWebhook
Create a new webhook. 

| Field        | Type       | Description
|--------------|------------|----------
| accessToken  | credentials| Access token for your bot received from Discord
| channelId    | Number     | Id of the channel
| webhookName  | String     | Name of the webhook (2-100 characters)
| webhookAvatar| File       | 128x128 jpeg image for the default webhook avatar

## DiscordBot.getChannelWebhooks
Returns a list of channel webhook objects.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the channel

## DiscordBot.getGuildWebhooks
Returns a list of guild webhook objects.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild

## DiscordBot.getSingleWebhook
Returns the new webhook object for the given id.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| webhookId  | Number     | Id of the webhook

## DiscordBot.getWebhookWithToken
Same as above, except this call does not require authentication and returns no user in the webhook object.

| Field       | Type  | Description
|-------------|-------|----------
| webhookToken| String| Token of the webhook
| webhookId   | Number| Id of the webhook

## DiscordBot.updateWebhook
Update a webhook. 

| Field        | Type       | Description
|--------------|------------|----------
| accessToken  | credentials| Access token for your bot received from Discord
| webhookId    | Number     | Id of the webhook
| webhookName  | String     | Name of the webhook (2-100 characters)
| webhookAvatar| File       | 128x128 jpeg image for the default webhook avatar

## DiscordBot.updateWebhookWithToken
Update a webhook.

| Field        | Type  | Description
|--------------|-------|----------
| webhookToken | String| Access token for ywebhook
| webhookId    | Number| Id of the webhook
| webhookName  | String| Name of the webhook (2-100 characters)
| webhookAvatar| File  | 128x128 jpeg image for the default webhook avatar

## DiscordBot.deleteWebhook
Delete a webhook. 

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| webhookId  | Number     | Id of the webhook

## DiscordBot.deleteWebhookWithToken
Delete a webhook. 

| Field       | Type  | Description
|-------------|-------|----------
| webhookToken| String| Access token for webhook
| webhookId   | Number| Id of the webhook

## DiscordBot.executeWebhookContent
Execute a webhook with text content

| Field           | Type   | Description
|-----------------|--------|----------
| webhookToken    | String | Access token for webhook
| webhookId       | Number | Id of the webhook
| content         | String | The message contents (up to 2000 characters)
| webhookUsername | String | Override the default username of the webhook
| webhookAvatarUrl| String | Override the default avatar of the webhook
| tts             | Boolean| true if this is a TTS message

## DiscordBot.executeWebhookEmbed
Execute a webhook with ebmed content

| Field           | Type   | Description
|-----------------|--------|----------
| webhookToken    | String | Access token for webhook
| webhookId       | Number | Id of the webhook
| embed           | List   | Array of embed objects
| webhookUsername | String | Override the default username of the webhook
| webhookAvatarUrl| String | Override the default avatar of the webhook
| tts             | Boolean| true if this is a TTS message

## DiscordBot.executeWebhookFile
Execute a webhook with file content

| Field           | Type   | Description
|-----------------|--------|----------
| webhookToken    | String | Access token for webhook
| webhookId       | Number | Id of the webhook
| file            | File   | File
| webhookUsername | String | Override the default username of the webhook
| webhookAvatarUrl| String | Override the default avatar of the webhook
| tts             | Boolean| true if this is a TTS message

## DiscordBot.addRecipientToGroupDm
Adds a recipient to a Group DM using their access token

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| userToken  | String     | access token of a user that has granted your app the gdm.join scope
| channelId  | Number     | Id of the Group DM channel
| userId     | Number     | Id of the user
| userNick   | String     | Nickname of the user being added

## DiscordBot.removeRecipientFromGroupDm
Remove a recipient from a Group DM

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the Group DM channel
| userId     | Number     | Id of the user

## DiscordBot.addGuildMember
Adds a user to the guild, provided you have a valid oauth2 access token for the user with the guilds.join scope.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| userId     | Number     | Id of the user
| userToken  | String     | An oauth2 access token granted with the guilds.join to the bot's application for the user you want to add to the guild

## DiscordBot.removeGuildMember
Remove a member from a guild.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| guildId    | Number     | Id of the guild
| userId     | Number     | Id of the user

## DiscordBot.deleteMessage
Delete a message. 

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the channel
| messageId  | Number     | Id of the message

## DiscordBot.bulkDeleteMessages
Delete multiple messages in a single request.

| Field      | Type       | Description
|------------|------------|----------
| accessToken| credentials| Access token for your bot received from Discord
| channelId  | Number     | Id of the channel
| messageIds | List       | Ids of the messages

