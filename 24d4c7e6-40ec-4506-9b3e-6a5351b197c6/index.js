const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send('Hello World!'));

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`));


// ================= START BOT CODE ===================
const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

const activities_list = [
    { type: 'PLAYING',  message: 'wildberrylillet'  },
    { type: 'watching',  message: 'youtube'  },
    { type: 'sleeping',  message: 'now'  },
    { type: 'eating',  message: 'food'  }
];

client.on('ready', () => {
    setInterval(() => {
        const index = Math.floor(Math.random() * (activities_list.length - 1) + 1);

        client.user.setActivity(activities_list[index].message, { type: activities_list[index].type });
    }, 10000);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('pong!');
     permissionOverwrites: [
        {
            id: guild.me.roles.highest,
            allow: ['VIEW_CHANNEL', 'MANAGE_CHANNELS', 'MANAGE_ROLES']
        }
    ]
  }
});
// You really don't want your token here since your repl's code
// is publically available. We'll take advantage of a Repl.it 
// feature to hide the token we got earlier. 


client.login(process.env.TOKEN)
