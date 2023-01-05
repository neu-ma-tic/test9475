const Dlang = require('discordbot-script');
const keepAlive = require('./server');

const bot = new Dlang({
	token: process.env.token,
	prefix: ['a/']
});

bot.Command({
	name: 'ping',
	code: `
	Pong!🏓
**$ping** ms
  `
});
bot.Command({
	name: 'imp',
	code: `
	ඞ <== Sus
	`
});
keepAlive();