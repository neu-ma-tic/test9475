const express = require('express');
const app = express();
const port = 3000;
let pingsNum = 0;
let isReady = 'No';

app.get('/', (req, res) => res.send(`Hello World!<br>Is client ready? ${isReady}<br>How many pings? ${pingsNum}`));

app.listen(port, () => console.log(`App listening at http://localhost:${port}`));


// ================= START BOT CODE ===================
const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

const activities_list = [
    { type: 'PLAYING',  message: 'joelheath․net'  },
    { type: 'WATCHING', message: 'joelheath24 videos' },
    { type: 'LISTENING', message: 'JRAJYM Theme' },
    { type: 'STREAMING', message: 'joelheath24 videos' }
];

let ratelimitMessage = "Great, no rate limit";
let errorMessage = "Great, no errors";

app.get('/error', (req, res) => res.send(`${errorMessage}. ${ratelimitMessage}`));

client.on('ratelimit', r => rateLimitMessage = `I got rate limited ${r.timeout} after ${r.number} requests` );
client.on('error', e => errorMessage = `I got an error ${e.message}`);



client.on('ready', () => { isReady = 'Yes'; console.log("Client is ready!");
    setInterval(() => {
        const index = Math.floor(Math.random() * (activities_list.length - 1));
        pingsNum++;
        client.user.setActivity(activities_list[index].message, { type: activities_list[index].type });
    }, 10000);
});

client.on('message', msg => {
  switch(msg.content) {
    case 'ping':
      msg.reply('pong!'); break;
    case 'Who is joelheath25?':
      msg.reply('The amazing and incredible personal assistant of joelheath24! Try asking: Who is Herobrine?'); break;
    case 'Who is joelheath24?':
      msg.reply('The best content creator out there!'); break;
    case 'Who is joelheath23?':
      msg.reply(`He is surely joelheath24's arch-nemesis.`); break;
    case 'Who is Herobrine?':
      msg.reply(`Little is known on the origins of Herobrine but currently he seems to be working alongside joelheath23.`); break;
    case 'Who is joelinaheath24?':
      msg.reply(`As late as 23 Oct 2020 joelinaheath24 has been joelheath24's girlfriend, though she is yet to make another appearance in joelheath24's videos, so little is known on their current relationship status. However what is known is that the two are not married, and joelinaheath24 'got hasty' with changing her sirname.`); break;
  }
});

const mySecret = process.env['TOKEN']
let loginResult = client.login(mySecret);

/*
loginResult
  .then((value) => { console.log(value); })
  .catch((error) => { console.log(error); })
  .finally((finalmente) => { console.log(`FINISHED, ${finalmente}`); })
*/


console.log("Line 69 of code");