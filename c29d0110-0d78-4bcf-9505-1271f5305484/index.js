
/**
 * Module Imports
 */

const Pagein = require('discord-paginationembed');

require('events').EventEmitter.prototype._maxListeners = 100;

const Discord = require('discord.js');

const Canvas = require('canvas');

const { registerFont } = require('canvas');

const { MessageEmbed } = require("discord.js");





const http = require("http");








const fs = require('fs')

const getDirName = require('path').dirname;

const { Client, Collection } = require("discord.js");

const { readdirSync } = require("fs");

const { join } = require("path");

const { TOKEN, PREFIX } = require("./util/EvobotUtil");

const client = new Client({ disableMentions: "everyone" });

const prefux = '&';
/**
 * login
 */
client.login(TOKEN);
client.commands = new Collection();
client.prefix = PREFIX;
client.queue = new Map();
const cooldowns = new Collection();
const escapeRegex = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");


/**
 * instalingSite
 */




/**
 * embeds
 */








client.on('message', async msg => {
  if (msg.content.toLowerCase().startsWith(prefux + " ")) {
    msg.channel.send("شما پرفیکس من رو به کار بردید ولی دستوری که وارد کردید نادرست بود ")
    msg.channel.send('لطفا از دستور ```&help``` برای کسب اطلاعات بیشتر استفاده کنید')

  }
});












client.on('message', message => {
    if (message.content.toLowerCase().startsWith(prefux + 'post')) {
        const MyMessage = message.content.slice(6).trim();
        const TestEmbed = new Discord.MessageEmbed()
            .setColor('#b700ff')
            .setTitle(MyMessage)

      message.delete();
      message.channel.send(TestEmbed)
    }
});

/**
 * Client my cmds
 */


client.on("ready", () => {
   function randomStatus() {
const status = ["بات موزیک","بات چت","بات امنیتی",`${client.guilds.cache.size}Servers`,"&play","&help",]

let rstatus = status[Math.floor(Math.random() * status.length)]

client.user.setPresence({
        status: 'dnd',
        activity: {
            name: `${rstatus}`,
            type: 'WATCHING',
        }
})
}; setInterval(randomStatus, 3000)

console.log('Ready for playing music')
});


client.on("ready", () => {




    

    setTimeout(function() {
        console.log('opening ports . . .')

       }, 1000);
      
       setTimeout(function() {
         http.createServer((_, res)=>res.end("Windwalker Studio Status : READY")).listen(8080);
         console.log('Port Is Open On 8080')

       }, 3000);

       setTimeout(function() {
         console.log('Site is ready')

       }, 6000);

    
});



client.on("warn", (info) => console.log(info));
client.on("error", console.error);



/**
 * Import all commands
 */
const commandFiles = readdirSync(join(__dirname, "commands")).filter((file) => file.endsWith(".js"));
for (const file of commandFiles) {
  const command = require(join(__dirname, "commands", `${file}`));
  client.commands.set(command.name, command);
}

client.on('message', msg => {
  if (msg.content === '&hello') {
    msg.reply('سلام خوبی');
  }
});


































client.on('message', msg => {
  if (msg.content === '&games') {
    msg.reply('Best Games Is Here');
    msg.channel.send("https://ptb.discordapp.com/store/skus/494959992483348480/warframe");
    msg.channel.send('https://ptb.discord.com/store/skus/550277544025522176/heroes-generals-wwii');
    msg.channel.send('https://ptb.discordapp.com/store/skus/528145079819436043/paladins');
    msg.channel.send('https://ptb.discord.com/store/skus/518088627234930688/realm-royale');
    msg.channel.send('https://ptb.discord.com/store/skus/488607666231443456/minion-masters');
    msg.channel.send('https://ptb.discord.com/store/skus/594073512906588179/light-from-the-butt');
    msg.channel.send('https://ptb.discord.com/store/skus/565994833953554432/it-s-hard-being-a-dog');
    

   
    msg.channel.send('پایان لیست');

    
  }
});

client.on('message', msg => {
	if (msg.content === '&server') {
	
	 msg.reply("من به");
   msg.channel.send(`${client.guilds.cache.size}`);
   msg.channel.send("تا سرور اد شدم");
  }
});



client.on('message', message => {
  if (message.content === '&info') {
    if (message.channel.type == "dm") 
     return message.channel.send('این کامند نمی تواند در DM استفاده شود');
    const serinfo = new Discord.MessageEmbed()
        .setColor("ffffff")
        .setTitle("اطلاعات سرور")
        .addFields(
          { name: 'نام سرور', value: `${message.guild}` },
          { name: '\u200B', value: '\u200B' },

          { name: 'مالک سرور', value: `${message.guild.owner}` },
          { name: '\u200B', value: '\u200B' },


          { name: 'تعداد ممبر', value: `${message.guild.memberCount}` },
          { name: '\u200B', value: '\u200B' },

          { name: 'تعداد رول', value: `${message.guild.roles.cache.size}` },
          
          
          

          

          
        )
    message.reply('بفرما اینم اطلاعات سرور');

    message.channel.send(serinfo);
  }
}); 





client.on("message", message => {
  if (message.content.toLowerCase().startsWith(prefux + 'help')) {

   const toggel = message.content.slice(5).trim();
    if(toggel === 'm') 
     return;
   
  const FieldsEmbed = new Pagein.FieldsEmbed()
   .setArray([
     {word:"***دستورات کلی***"},
     {word:"\u200B"},
     {word:"**&helpm** لیست کامندهای موزیک"},
     {word:"\u200B"},
     {word:'**&hello** سلام کردن به بات'},
     {word:"\u200B"},
     {word:'**&games** یه لیست از گیم های دیسکورد'},
     {word:"\u200B"},
     {word:'**&post <text>** پست کردن یک امبد با متن خودتان'},
     {word:"\u200B"},
     {word:'**&info** اطلاعات سرور'},
     {word:"\u200B"},
     




     



     
     
     
     
     ])
   .setChannel(message.channel)
   .setElementsPerPage(11)
   .setPageIndicator(false)
   .formatField('**Commands**', el => el.word)
   FieldsEmbed.embed
   .setColor('RANDOM')
  FieldsEmbed.build();
  
}
        
});

 


















/**
 * music cmds
 */




client.on("message", async (message) => {
  if (message.author.bot) return;
  if (!message.guild) return;

  const prefixRegex = new RegExp(`^(<@!?${client.user.id}>|${escapeRegex(PREFIX)})\\s*`);
  if (!prefixRegex.test(message.content)) return;

  const [, matchedPrefix] = message.content.match(prefixRegex);

  const args = message.content.slice(matchedPrefix.length).trim().split(/ +/);
  const commandName = args.shift().toLowerCase();

  const command =
    client.commands.get(commandName) ||
    client.commands.find((cmd) => cmd.aliases && cmd.aliases.includes(commandName));

  if (!command) return;

  if (!cooldowns.has(command.name)) {
    cooldowns.set(command.name, new Collection());
  }

  const now = Date.now();
  const timestamps = cooldowns.get(command.name);
  const cooldownAmount = (command.cooldown || 1) * 1000;

  if (timestamps.has(message.author.id)) {
    const expirationTime = timestamps.get(message.author.id) + cooldownAmount;

    if (now < expirationTime) {
      const timeLeft = (expirationTime - now) / 1000;
      return message.reply(
        `please wait ${timeLeft.toFixed(1)} more second(s) before reusing the \`${command.name}\` command.`
      );
    }
  }

  timestamps.set(message.author.id, now);
  setTimeout(() => timestamps.delete(message.author.id), cooldownAmount);

  try {
    command.execute(message, args);
  } catch (error) {
    console.error(error);
    message.reply("There was an error executing that command.").catch(console.error);
  }
}); 
99