const Discord = require("discord.js")
exports.run = async (bot, message, argumentos, arg_texto, chat) => {
  
  const ajuda = new Discord.MessageEmbed()
    .setColor("GREEN")
    .setTitle("Lista de comandos!")
    .setDescription("Reagir de acordo com o  que procura!\n\n📚 - Informações\n\n🔱 - Administrativos\n\n🎊 - Diversão")
    .setTimestamp()
    .setFooter(`Comando solicitado por ${message.member.displayName}`, message.author.displayAvatarURL({Size: 32}))   
    
  message.channel.send(ajuda).then(msg => {
    msg.react('📚').then(r => {
      msg.react('🔱').then(r => {
    msg.react('🎊').then(r => {
      })
    })
  })
    
    const infosFilter = (reaction, user) => reaction.emoji.name === '📚' && user.id === message.author.id;
        const admFilter = (reaction, user) => reaction.emoji.name === '🔱' && user.id === message.author.id;
    const funFilter = (reaction, user) => reaction.emoji.name === '🎊' && user.id === message.author.id;
    
    const infos = msg.createReactionCollector(infosFilter);
        const adm = msg.createReactionCollector(admFilter);
    const fun = msg.createReactionCollector(funFilter);

    infos.on('collect', r2 => {
      
      ajuda.setTitle("Comandos informativos!")
      ajuda.setDescription("- b!help - Mostra os comandos do bot!\n\n - b!avatar @usuario - Veja o avatar de alguém!\n\n - b!botinfo - Veja informações sobre o Bily!\n\n - b!invite - Veja o link para adicionar o Bily!\n\n - b!ping - Veja a sua latência e a da API!\n\n - b!serverinfo - Veja informações sobre o servidor!\n\n - b!uptime - Veja o tempo de atividade do Bily\n\n - b!upvote - Veja o link para dar um upvote no Bily!")
      msg.edit(ajuda)

       })
    
    adm.on('collect', r2 => {
      
      ajuda.setTitle("Comandos de administração!")
      ajuda.setDescription("- b!ban @usuário <motivo> - Bana um membro!\n\n - b!kick @usuário <motivo> - Expulse um membro!\n\n - b!listban - Veja a lista dos usuários banidos!\n\n - b!unban - Desbana um membro!\n\n - b!clear <quantidade> - Exclua uma quantidade entre 1 e 99 mensagens!#comando em manutenção#\n\n - b!lock - Bloqueie um canal!\n\n - b!unlock - Desbloqueie um canal!")
      msg.edit(ajuda)
      
    })
    
    fun.on('collect', r2 => {
      
      ajuda.setTitle("Comandos de diversão!")
      ajuda.setDescription("- b!say - Me faça falar algo!\n\n - b!coinflip <cara> ou <coroa> - Jogue o clássico cara ou coroa!\n\n - b!f1 @usuário - Aposte uma corrida de Fórmula 1!\n\n - b!hug @usuario - Dê um abraço!\n\n - b!kiss @usuario - Dê um beijo!\n\n - b!pat @usuário - Faça cafuné!\n\n - b!roleta - Jogue uma partida de roleta-russa!\n\n - b!slap @usuário - Dê um tapa!\n\n - b!ship @usuário1 @usuário2 - Shipe os usuários mencionados!")
      msg.edit(ajuda)
      
    })
  })  
} 