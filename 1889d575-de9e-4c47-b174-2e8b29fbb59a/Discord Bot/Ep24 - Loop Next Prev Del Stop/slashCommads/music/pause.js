const { getVoiceConnection } = require("@discordjs/voice");

module.exports = {
  name: "pause",
  description: "Pausa el reproductor",
  run: async (client, interaction) => {
    const pvc = getVoiceConnection(interaction.guild.id);
    const vc = interaction.member.voice.channel;
    if (!vc) {
      return interaction.reply({
        content: "Tienes que estar en un canal de voz",
        ephemeral: true,
      });
    }

    if (!pvc)
      return interaction.reply({
        content: "El bot no esta reproduciendo musica",
        ephemeral: true,
      });

    if (vc != pvc.joinConfig.channelId) {
      return interaction.reply({
        content: "Tienes que estar en el mismo canal de voz que el bot",
        ephemeral: true,
      });
    }

    const player = pvc.state.subscription.player;

    player.pause();

    interaction.reply("Bot pausado");
  },
};
