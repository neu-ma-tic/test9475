<?php
$app->post('/api/DiscordBot/createGuildChannel', function ($request, $response, $args) {
    $settings = $this->settings;

    //checking properly formed json
    $checkRequest = $this->validation;
    $validateRes = $checkRequest->validate($request, ['accessToken', 'guildId', 'channelName']);
    if (!empty($validateRes) && isset($validateRes['callback']) && $validateRes['callback'] == 'error') {
        return $response->withHeader('Content-type', 'application/json')->withStatus(200)->withJson($validateRes);
    } else {
        $post_data = $validateRes;
    }
    //forming request to vendor API
    $query_str = $settings['api_url'] . 'guilds/' . $post_data['args']['guildId'] . '/channels';
    $body = array();
    $body['name'] = $post_data['args']['channelName'];

    if (isset($post_data['args']['channelType']) && strlen($post_data['args']['channelType']) > 0) {
        $body['type'] = $post_data['args']['channelType'];
    }

    if (isset($post_data['args']['voiceChannelBitrate']) && strlen($post_data['args']['voiceChannelBitrate']) > 0) {
        $body['bitrate'] = $post_data['args']['voiceChannelBitrate'];
    }
    if (isset($post_data['args']['voiceChannelUserLimit']) && strlen($post_data['args']['voiceChannelUserLimit']) > 0) {
        $body['user_limit'] = $post_data['args']['voiceChannelUserLimit'];
    }
    if (isset($post_data['args']['channelPermissionsOverwrite']) && count($post_data['args']['channelPermissionsOverwrite']) > 0) {
        $body['permission_overwrites'] = $post_data['args']['channelPermissionsOverwrite'];
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