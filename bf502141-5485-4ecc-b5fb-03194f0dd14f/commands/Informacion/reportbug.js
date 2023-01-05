const {
  MessageEmbed,
  MessageActionRow,
  MessageButton,
  ButtonInteraction,
} = require("discord.js");
const {
  config
} = require("../..");

module.exports = {
  name: "reportbug",
  aliases: [],
  category: "Informacion",
  description: "Comando para reportar un bug",
  usage: "<reporte>",
  run: async (client, message, args) => {

    let bug = args.join(" ");
    if (!bug) return message.channel.send("¡Escribe un bug a reportar!");
    // BOTONES
    let button1 = new MessageButton()
      .setCustomId("yes")
      .setLabel("Confirmar")
      .setStyle("SUCCESS")
      .setEmoji(config.emoji.succesid);
    let button2 = new MessageButton()
      .setCustomId("no")
      .setLabel("Cancelar")
      .setStyle("DANGER")
      .setEmoji(config.emoji.errorid);
    let row = new MessageActionRow().addComponents(button1, button2);
    // MENSAJE DE CONFIRMACION
    let author = message.author.username;
    let ID = message.author.id;
    let confirmar = new MessageEmbed()
      .setColor(color)
      .setAuthor("Confirmacion de Reporte", client.user.displayAvatarURL())
      .setDescription("¿Estás seguro que quieres reportar este bug? __¡Usar mal el comando causara la prohibición!__")
      .addField("Bug a reportar:", bug);
    message.channel.send({
      embeds: [confirmar],
      components: [row]
    });
    //Colector
    const filter = (interaction) => {
      if (interaction.user.id == message.author.id) return true;
      else {
        interaction.reply({
          content: "Tu no puedes usar este boton",
          ephemeral: true,
        });
        return false;
      }
    };

    const collector = message.channel.createMessageComponentCollector({
      filter,
      max: 1,
    });

    collector.on("end", async (ButtonInteraction) => {
      const id = ButtonInteraction.first().customId;

      if (id == "yes") {
        let confirmado = new MessageEmbed()
          .setColor(0x00ff7b)
          .setAuthor("Bug Reportado Con Exito!", client.user.displayAvatarURL())
          .addField("Bug reportado:", bug);
        let reporte = new MessageEmbed()
          .setAuthor("Nuevo Reporte de Bug", client.user.displayAvatarURL())
          .setColor(color)
          .addField("Reporte:", bug)
          .setThumbnail(message.author.displayAvatarURL())
          .setFooter(`Reporte Enviado por ${author} | ID: ${ID}`, message.author.displayAvatarURL());
        client.channels.cache.get("936724519341674497").send({
          embeds: [reporte]
        });
        ButtonInteraction.first().reply({
          embeds: [confirmado]
        });
      }
      if (id == "no") {
        let cancelado = new MessageEmbed()
          .setColor(0xff0000)
          .setAuthor("Reporte Cancelado Con exito!", client.user.displayAvatarURL());
        ButtonInteraction.first().reply({
          embeds: [cancelado]
        });
      }
    });
  },
};