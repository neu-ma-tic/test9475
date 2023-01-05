<?php
$app->post('/api/DiscordBot/executeWebhookContent', function ($request, $response, $args) {
    $settings = $this->settings;

    //checking properly formed json
    $checkRequest = $this->validation;
    $validateRes = $checkRequest->validate($request, ['webhookToken', 'webhookId', 'content']);
    if (!empty($validateRes) && isset($validateRes['callback']) && $validateRes['callback'] == 'error') {
        return $response->withHeader('Content-type', 'application/json')->withStatus(200)->withJson($validateRes);
    } else {
        $post_data = $validateRes;
    }
    //forming request to vendor API
    $query_str = $settings['api_url'] . 'webhooks/' . $post_data['args']['webhookId'] . '/' . $post_data['args']['webhookToken'];
    if (isset($post_data['args']['wait']) && strlen($post_data['args']['wait']) > 0) {
       $query_str .= '/wait='.$post_data['args']['wait'];
    }

    $body['content'] = $post_data['args']['content'];

    if (isset($post_data['args']['webhookUsername']) && strlen($post_data['args']['webhookUsername']) > 0) {
        $body['username'] = $post_data['args']['webhookUsername'];
    }
    if (isset($post_data['args']['webhookAvatarUrl']) && strlen($post_data['args']['webhookAvatarUrl']) > 0) {
        $body['avatar_url'] = $post_data['args']['webhookAvatarUrl'];
    }
    if (isset($post_data['args']['tts']) && strlen($post_data['args']['tts']) > 0) {
        $body['tts'] = $post_data['args']['tts'];
    }
    //requesting remote API
    $client = new GuzzleHttp\Client();

    try {

        $resp = $client->request('POST', $query_str, [
            'headers' => [
                'Authorization' => 'Bot ' . $post_data['args']['accessToken']
            ], 'json' => $body
        ]);

        $responseBody = $resp->getBody()->getContents();
        $rawBody = json_decode($resp->getBody());

        $all_data[] = $rawBody;
        if ($response->getStatusCode() == '200') {
            $result['callback'] = 'success';
            $result['contextWrites']['to'] = 'success';
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