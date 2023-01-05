<?php
$app->post('/api/DiscordBot/createGuild', function ($request, $response, $args) {
    $settings = $this->settings;

    //checking properly formed json
    $checkRequest = $this->validation;
    $validateRes = $checkRequest->validate($request, ['accessToken', 'guildName']);
    if (!empty($validateRes) && isset($validateRes['callback']) && $validateRes['callback'] == 'error') {
        return $response->withHeader('Content-type', 'application/json')->withStatus(200)->withJson($validateRes);
    } else {
        $post_data = $validateRes;
    }
    //forming request to vendor API
    $query_str = $settings['api_url'] . 'guilds';
    $body = array();
    $body['name'] = $post_data['args']['guildName'];

    if (isset($post_data['args']['guildRegion']) && strlen($post_data['args']['guildRegion']) > 0) {
        $body['region'] = $post_data['args']['guildRegion'];
    }
    if (isset($post_data['args']['guildIcon']) && strlen($post_data['args']['guildIcon']) > 0) {
        $body['icon'] = base64_encode(file_get_contents($post_data['args']['guildIcon']));
    }
    if (isset($post_data['args']['guildVerificationLevel']) && strlen($post_data['args']['guildVerificationLevel']) > 0) {
        $body['verification_level'] = $post_data['args']['guildVerificationLevel'];
    }
    if (isset($post_data['args']['guildDefaultMessageNotifications']) && strlen($post_data['args']['guildDefaultMessageNotifications']) > 0) {
        $body['default_message_notifications'] = $post_data['args']['guildDefaultMessageNotifications'];
    }
    if (isset($post_data['args']['guildRoles']) && strlen($post_data['args']['guildRoles']) > 0) {
        $body['roles'] = $post_data['args']['guildRoles'];
    }
    if (isset($post_data['args']['guildChannels']) && strlen($post_data['args']['guildChannels']) > 0) {
        $body['channels'] = $post_data['args']['guildChannels'];
    }

    //requesting remote API
    $client = new GuzzleHttp\Client();

    try {

        $resp = $client->request('POST', $query_str, [
            'headers' => [
                'Authorization' => 'Bot ' . $post_data['args']['accessToken']
            ],
            'json' => $body
        ]);

        $responseBody = $resp->getBody()->getContents();
        $rawBody = json_decode($resp->getBody());

        $all_data[] = $rawBody;
        if ($response->getStatusCode() == '200') {
            $result['callback'] = 'success';
            $result['contextWrites']['to'] = is_array($all_data) ? $all_data : json_decode($all_data);
        } else {
            $result['callback'] = 'error';
            $result['contextWrites']['to']['status_code'] = 'API_ERROR';
            $result['contextWrites']['to']['status_msg'] = is_array($responseBody) ? $responseBody : json_decode($responseBody);
        }

    } catch (\GuzzleHttp\Exception\ClientException $exception) {
        $responseBody = $exception->getResponse()->getReasonPhrase();
        $result['callback'] = 'error';
        $result['contextWrites']['to']['status_code'] = 'API_ERROR';
        $result['contextWrites']['to']['status_msg'] = $responseBody;

    } catch (GuzzleHttp\Exception\ServerException $exception) {

        $responseBody = $exception->getResponse()->getBody(true);
        $result['callback'] = 'error';
        $result['contextWrites']['to'] = json_decode($responseBody);

    } catch (GuzzleHttp\Exception\BadResponseException $exception) {

        $responseBody = $exception->getResponse()->getBody(true);
        $result['callback'] = 'error';
        $result['contextWrites']['to'] = json_decode($responseBody);

    }


    return $response->withHeader('Content-type', 'application/json')->withStatus(200)->withJson($result);

});