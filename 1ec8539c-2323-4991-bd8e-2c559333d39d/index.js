const { Client, Intents } = require("discord.js");
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.GUILD_MEMBERS,Intents.FLAGS.DIRECT_MESSAGES] });

client.on('debug', console.log);

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
    });

client.on ("messageCreate", msg => {
  if (msg.author.bot) return;
 
  if (msg.content === "ping"){ 
    console.log(msg.author.id);
    msg.reply(msg.author.id + " pong");
    return;
    }


  // commands from bot creator
  if (msg.author.id === process.env.ADMIN_ID) 
  {
    console.log(msg.author.id);

    if (msg.content === "$list") { 
      msg.reply("пагадити");

      msg.guild.roles.fetch()
        .then(roles => {
          console.log(`There are ${roles.size} roles.`);

          roles.forEach((role) => {
            console.log(`Role name:  ${role.toString()}`);
          });
        })
        .catch(console.error);

      msg.guild.members.fetch()
        .then(members => {
          console.log(`There are ${members.size} members`);

          members.forEach((member) => {
            //console.log(`User name:  ${member.user.tag}, bot: ${member.user.bot}`);
            
            if (member.user.bot) return;
            //console.log(`Roles: ${member.roles.cache}`);

            if (!member.roles.cache.some(role => role.name === 'Член-клуба') && member.roles.cache.some(role => role.name.startsWith('Уровень')))
            {
              console.log(`User name:  ${member.user.tag}, bot: ${member.user.bot}`);
              
              /*
              if (member.user.dmChannel)
                console.log(`${member.user.tag} WAS messaged`)
              else 
                console.log(`${member.user.tag} was NOT messaged`);
              */

              /*member.send(`*Я имел ввиду 11 февраля. Сорян, слишком упоролся, пока разбирался как писать ботов.`).then(()=>console.log(`Message sent to ${member.user.tag}`))
                .catch(()=> 
                  console.log(`Couldn't send msg to ${member.user.tag}`));*/
            }
          
          });
          })
        .catch(console.error);


      }
    else msg.reply("да, хозяин");


    return;
  }; 
  
  if (msg.mentions.members.some(member => member == client.user)){ 
    msg.reply(msg.content + " у тебя в штанах");
    return;
  };

});

client.login(process.env.TOKEN);

