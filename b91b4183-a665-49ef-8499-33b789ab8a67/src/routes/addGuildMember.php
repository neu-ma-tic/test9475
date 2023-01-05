<?php
$app->post('/api/DiscordBot/addGuildMember', function ($request, $response, $args) {
    $settings = $this->settings;

    //checking properly formed json
    $checkRequest = $this->validation;
    $validateRes = $checkRequest->validate($request, ['accessToken', 'guildId', 'userId', 'userToken']);
    if (!empty($validateRes) && isset($validateRes['callback']) && $validateRes['callback'] == 'error') {
        return $response->withHeader('Content-type', 'application/json')->withStatus(200)->withJson($validateRes);
    } else {
        $post_data = $validateRes;
    }
    //forming request to vendor API
    $query_str = $settings['api_url'] . "guilds/" . $post_data['args']['guildId'] . '/members/' . $post_data['args']['userId'];
    $body = array();
    $body['access_token'] = $post_data['args']['userToken'];

    if (isset($post_data['args']['memberNick']) && strlen($post_data['args']['memberNick']) > 0) {
        $body['nick'] = $post_data['args']['memberNick'];
    }
    if (isset($post_data['args']['memberRoles']) && strlen($post_data['args']['memberRoles']) > 0) {
        $body['roles'] = $post_data['args']['memberRoles'];
    }
    if (isset($post_data['args']['mute']) && strlen($post_data['args']['mute']) > 0) {
        $body['mute'] = $post_data['args']['mute'];
    }
    if (isset($post_data['args']['deaf']) && strlen($post_data['args']['deaf']) > 0) {
        $body['deaf'] = $post_data['args']['deaf'];
    }
    //requesting remote API
    $client = new GuzzleHttp\Client();
    try {

        $resp = $client->request('PUT', $query_str, [
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