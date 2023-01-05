const Discord = require('discord.js');
const client = new Discord.Client();

const token = 'NDM3ODMyOTczOTEyNjM3NDQw.Wt1huw.jUEecxCyNR8GT7pc3OPbqKC1ViE';
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

const prefix = "!";

  

client.on('message', msg => {
  if (msg.content === '!help') 
  {
    let embed = new Discord.MessageEmbed()
    .setTitle('OrganyzeBullet Command List.')
    .setDescription('A description.')
    .setColor('DARK_GOLD')

    msg.reply(embed);
    return
  }
  else if (msg.content === '!ping') 
  {
    msg.reply('Pong!');
    return
  }
  else if (msg.content === prefix + 'dab') 
  {
    msg.reply('very edgy');
    return
  }
  else if (msg.content === 'dabb') 
  {
    msg.reply('phat dab');
    return
  }
  else if (msg.content === '>w>') 
  {
    msg.reply('Gross. Who are you? An Alex? OOF');
    return
  }
  else if (msg.content === 'same') 
  {
    msg.reply('honda civic spotted');
    return
  }
  else if (msg.content === 'Lol') 
  {
    msg.reply('An Alex is spotted.');
    return
  }
  else if (msg.content === 'egoo') 
  {
    msg.react('😃')
    return
  }
  



//slices off prefix from our message, then trims extra whitespace, then returns our array of words from the message
  const args = msg.content.slice(prefix.length).trim().split(' ')
  
  //splits off the first word from the array, which will be our command
  const command = args.shift().toLowerCase()
  //log the command
  console.log('command: ', command)
  //log any arguments passed with a command
  console.log(args)

  if(command === 'ego') {
    msg.react("😀")
    msg.reply('wow, what a great post')
  }
  if (command === "clear") {
    //default deletes message itself plus previous
    let num = 2;
    
    //if argument is provided, we need to convert it from string to number
    if (args[0]) {
      //add 1 to delete clear command itself
      num = parseInt(args[0]) + 1;
    }
     //notify channel of deleted messages
    msg.channel.send(`I have deleted [${args[0]}] posts.`);
    //bulk delete the messages
    msg.channel.bulkDelete(num);

  }


});

client.login(token);