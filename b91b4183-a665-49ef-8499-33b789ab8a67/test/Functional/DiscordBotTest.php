<?php

namespace Test\Functional;

require_once(__DIR__ . '/../../src/Models/checkRequest.php');

class DiscordBotTest extends BaseTestCase
{

    public function testListMetrics()
    {

        $routes = [
            'bulkDeleteMessages',
            'deleteMessage',
            'removeGuildMember',
            'removeRecipientFromGroupDm',
            'addRecipientToGroupDm',
            'executeWebhookFile',
            'executeWebhookEmbed',
            'executeWebhookContent',
            'deleteWebhookWithToken',
            'deleteWebhook',
            'updateWebhookWithToken',
            'updateWebhook',
            'getWebhookWithToken',
            'getSingleWebhook',
            'getGuildWebhooks',
            'getChannelWebhooks',
            'createWebhook',
            'getVoiceRegions',
            'getUsersConnections',
            'createGroupDm',
            'createDm',
            'getUserDms',
            'leaveGuild',
            'getCurrentUserGuilds',
            'updateCurrentUser',
            'getUser',
            'getCurrentUser',
            'deleteInvite',
            'getInvite',
            'updateGuildEmbed',
            'getGuildEmbed',
            'deleteGuildIntegration',
            'syncGuildIntegration',
            'updateGuildIntegration',
            'createGuildIntegration',
            'getGuildIntegrations',
            'getGuildInvites',
            'getGuildVoiceRegions',
            'startGuildPrune',
            'getGuildPruneCount',
            'deleteGuildRole',
            'deleteGuild',
            'removeGuildBan',
            'createGuildBan',
            'getGuildBans',
            'updateGuildRole',
            'updateGuildRolePositions',
            'createGuildRole',
            'removeGuildMemberRole',
            'getGuildRoles',
            'addGuildMemberRole',
            'addGuildMember',
            'updateGuildMember',
            'getGuildMember',
            'getGuildMembers',
            'updateGuildChannelPositions',
            'createGuildChannel',
            'getGuildChannels',
            'updateGuild',
            'getGuild',
            'createGuild',
            'deletePinnedChannelMessage',
            'getPinnedMessages',
            'addPinnedChannelMessage',
            'createTriggerTypingIndicator',
            'deleteRoleChannelPermission',
            'deleteUserChannelPermission',
            'updateRoleChannelPermissions',
            'updateUserChannelPermissions',
            'createChannelInvite',
            'getChannelInvites',
            'deleteAllReactions',
            'deleteUserReaction',
            'deleteOwnReaction',
            'getReactions',
            'createReaction',
            'getChannelSingleMessage',
            'getChannelMessages',
            'deleteChannel',
            'updateChannel',
            'getSingleChannel',
            'getAppInfo',
            'getAccessToken'
        ];

        foreach ($routes as $file) {
            $var = '{  
                    }';
            $post_data = json_decode($var, true);

            $response = $this->runApp('POST', '/api/DiscordBot/' . $file, $post_data);

            $this->assertEquals(200, $response->getStatusCode(), 'Error in ' . $file . ' method');
        }
    }

}
