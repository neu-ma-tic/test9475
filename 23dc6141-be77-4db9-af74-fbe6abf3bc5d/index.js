const Discord = require('discord.js');
const bot = new Discord.Client();
prefix = '';
bot.on('ready', () =>{
    console.log('bot is active');
});

bot.on('message', message =>{
    
  //if(message.channel.id == '831952027436449813'){
    if(!message.content.startsWith(prefix) || message.author.bot) return;
    //message2 = message.split('');
    
    //message.channel.send(message.member.user.tag);
    //message.channel.send(message.member.id);
    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLocaleLowerCase();
    message2 = String(message);
    message2 = message2.toLocaleLowerCase();
    //var chars = message2.split('');
    
    //message.channel.send(chars); 
    if (message2 == 'nitroso'){
        message.delete()
    }
  //}
})
bot.login(i40kSWrn5hM7Z94TU3Cqu6lJrr_EhneV);