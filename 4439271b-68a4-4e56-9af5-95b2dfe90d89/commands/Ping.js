module.exports = {
	name: 'ping',
	description: 'Ping!',
	execute(message, args) {
		message.channel.send('Pong.');
    console.log('ping used' )
	},
};
