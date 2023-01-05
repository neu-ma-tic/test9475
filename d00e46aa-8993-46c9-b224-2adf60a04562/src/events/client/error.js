
module.exports.run = (client, error) => {
    return client.logger.error(`Discord client's websocket encountered a connection error: ${error}`)
}