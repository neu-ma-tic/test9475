const { MessageEmbed } = require('discord.js');
module.exports = {
      name: 'ping',
      usage: [""],
      aliases: ["p"],
      description: "Gets Bot\'s current latency and API latency.",
      run: async(client, message, prefix) => {
        if(!message.content.startsWith(prefix)) return;
              try {
              const embed = new MessageEmbed()
              .setDescription('`Pinging...`')
              .setColor("RANDOM");    
              const msg = await message.channel.send({ embeds: [embed] });
              const timestamp = (message.editedTimestamp) ? message.editedTimestamp : message.createdTimestamp;
              const latency = `\`\`\`ini\n[ ${Math.floor(msg.createdTimestamp - timestamp)}ms ]\`\`\``;
              const apiLatency = `\`\`\`ini\n[ ${Math.round(message.client.ws.ping)}ms ]\`\`\``;
              embed.setTitle(`Pong!`)
              .setDescription('')
              .addField('', latency, true)
              .addField(`✅ API Latency`, apiLatency, true)
              .setTimestamp();
              msg.edit({ embeds: [embed] });
              
      //ERROR CATCH
      } catch (err) {
      const errorEmbed = new MessageEmbed()
      .setTitle("ERROR")
      .setDescription(`❌ ${err.message}`)
      .setColor("RED")
      .setFooter({
        text: `message will be deleted after 10 seconds`
      })
      message.channel.send({embeds: [errorEmbed] }).then(e => {
        setTimeout(() => e.delete(), 10000);
      });
    }
  }
};