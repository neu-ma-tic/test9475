<?php
$app->post('/api/DiscordBot/createGuildRole', function ($request, $response, $args) {
    $settings = $this->settings;

    //checking properly formed json
    $checkRequest = $this->validation;
    $validateRes = $checkRequest->validate($request, ['accessToken', 'guildId']);
    if (!empty($validateRes) && isset($validateRes['callback']) && $validateRes['callback'] == 'error') {
        return $response->withHeader('Content-type', 'application/json')->withStatus(200)->withJson($validateRes);
    } else {
        $post_data = $validateRes;
    }
    //forming request to vendor API
    $query_str = $settings['api_url'] . 'guilds/' . $post_data['args']['guildId'] . '/roles';
    $body = array();

    if (isset($post_data['args']['roleName']) && strlen($post_data['args']['roleName']) > 0) {
        $body['name'] = $post_data['args']['roleName'];
    }
    if (isset($post_data['args']['rolePermissions']) && strlen($post_data['args']['rolePermissions']) > 0) {
        $body['permissions'] = $post_data['args']['rolePermissions'];
    }
    if (isset($post_data['args']['roleColor']) && strlen($post_data['args']['roleColor']) > 0) {
        $body['color'] = $post_data['args']['roleColor'];
    }
    if (isset($post_data['args']['hoist']) && strlen($post_data['args']['hoist']) > 0) {
        $body['hoist'] = $post_data['args']['hoist'];
    }
    if (isset($post_data['args']['mentionable']) && strlen($post_data['args']['mentionable']) > 0) {
        $body['mentionable'] = $post_data['args']['mentionable'];
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