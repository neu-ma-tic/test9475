module.exports = {
    bot: {
        season: 'WONDER',
        timezone: 'Los Angeles'
    },
    webhook: {
        error: {
            // Webhook
            id: '',
            token: ''
        }
    },
    github: 'https://api.github.com/repos/wonderlandpark/wonderbot/commits',
    app: {
        messageCacheMaxSize: 50,
        presence: { activity: { name: 'GAME' } }
    },
    shard: {
        totalShards: 2,
        respawn: true,
        token: ''
    },
    token: '',
    prefix: '.',
    owners: ['285185716240252929'],
    secrets: {
        seoul: 'sample', // data.seoul.go.kr
        mainapi: ''
    }
}
