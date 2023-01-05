const Bot = require('./src/structures/Bot');

(async () => await new Bot().start(process.env['botToken']))()
