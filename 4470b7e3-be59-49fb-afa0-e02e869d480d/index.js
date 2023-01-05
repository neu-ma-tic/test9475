const { Client, Intents, MessageAttachment } = require("discord.js");
const Canvas = require('canvas');

Canvas.registerFont('./touche.ttf', { family: 'rational' });

const client = new Client({
    intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES]
  });

const prefix = '!';

client.once('ready', () => {
    console.log('Ready')
});

client.on('messageCreate', async message => {
    if (message.author.bot || !message.content.startsWith(prefix)) {
        return;
    }

    const args = message.content.slice(prefix.length).split(/ +/);
    const cmd = args.shift().toLowerCase();

    if (cmd === '!') {

        const d = new Date();
        let month;
        let day;
        let month_num = d.getMonth() + 1;
        let day_num = d.getDate();
        if (month_num < 10) {
            month = String('0' + month_num);
        }
        else {
            month = String(month_num);
        }
        if (day_num < 10) {
            day = String('0' + day_num);
        }
        else {
            day = String(day_num);
        }
        let year = String(d.getFullYear());
        let date = month + '/' + day + '/' + year;

        const canvas = Canvas.createCanvas(521, 1129);
        const context = canvas.getContext('2d');

        const background = await Canvas.loadImage('https://cdn.discordapp.com/attachments/902603223058231326/972932529239752744/image.png');
        context.drawImage(background, 0, 0, canvas.width, canvas.height);

        context.fillStyle = "white";
        context.fillRect(canvas.width / 4.5, canvas.height / 3 - 20, 350, 60);
        
        context.font = '48px "rational"';
	    context.fillStyle = 'black';
        context.fillText(date, canvas.width / 4.5 + 8, canvas.height / 3 + 32);

        const attachment = new MessageAttachment(canvas.toBuffer(), 'profile-image.png');

        messprocess.env['token']in('OTcyOTA1NDY1MjIwNTgzNTM1.Ynf20g.jog5TqXCU4xkgbX3Ep7D1p18S1w');
