module.exports.execute = async (
    client,
    message,
    locale
) => {
    if (!message.data.arg[0]) {
        message.reply(locale.error.usage(message.data.cmd, message.data.prefix))
    }
    var Inko = require('inko')
    var inko = new Inko()
    var content = message.data.args
    message.delete()
    message.channel.send(`${message.author} : ${inko.en2ko(content)}`)
}

module.exports.props = {
    name: 'ko',
    perms: 'general',
    alias: ['한글로'],
    args: [
        {
            name: 'text',
            type: 'text',
            required: true
        }
    ]
}
