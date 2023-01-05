const { MessageButton, MessageActionRow, MessageEmbed } = require("discord.js");

module.exports = {
  name: "ping",
  description: "Run this to see my ping.",
  type: "CHAT_INPUT",
  options: [
    {
      name: "category",
      description: `choose a category!`,
      type: "STRING",
      required: true,
      choices: [
        {
          name: "Anal",
          value: "anal",
        },
        {
          name: "Ass",
          value: `ass`,
        },
        {
          name: "Bikini",
          value: "biniki",
        },
        {
          name: "Blonde",
          value: "blonde",
        },
        {
          name: "Blowjob",
          value: "blowjob",
        },
        {
          name: "Cowgirl",
          value: "cowgirl",
        },
        {
          name: "Dildo",
          value: "dildo",
        },
        {
          name: "Lingerie",
          value: "lingerie",
        },
        {
          name: "Maid",
          value: "maid",
        },
        {
          name: "Nurse",
          value: "nurse",
        },
        {
          name: "Mature",
          value: "mature",
        },
        {
          name: "Milf",
          value: "milf",
        },
        {
          name: "Pantyhose",
          value: "pantyhose",
        },
        {
          name: "POV",
          value: "pov",
        },
        {
          name: "Teen",
          value: "teen",
        },
        {
          name: "Undressing",
          value: "undressing",
        },
        {
          name: "Upskirt",
          value: "upskirt",
        },
      ],
    },
  ],
  run: async (client, interaction, container) => {

    let buttonslink = new container.Discord.MessageActionRow().addComponents([
    new container.Discord.MessageButton()
        .setLabel('❤️ VOTE FOR ME!')
        .setURL("https://discordbotlist.com/bots/lett/upvote")
        .setStyle('LINK'),
      new MessageButton()
        .setLabel('📨 INVITE!')
        .setURL("https://discord.com/api/oauth2/authorize?client_id=851917411795599360&permissions=2147543120&scope=bot")
        .setStyle('LINK'),
    ]);

    let buttontest = new container.Discord.MessageActionRow().addComponents([
    new container.Discord.MessageButton()
          .setStyle("SUCCESS")
          .setCustomId("0")
          .setLabel(`Next`),
      ]);

    const ping = new container.Discord.MessageEmbed()
      .setColor('RANDOM')
      .setTimestamp()
      .setTitle('🏓╎ Pong!')
      .setDescription(`🏠╎Websocket Latency: ${client.ws.ping}ms\n🤖╎Bot Latency: ${Date.now() - interaction.createdTimestamp}ms`);
    interaction.reply({
      embeds: [ping],
      components: [buttonslink, buttontest],
    })

    const collector = interaction.channel.createMessageComponentCollector({
      time: 2000 * 60,
    });

    collector.on("collect", async (b) => {
      const embedimg = new MessageEmbed()
        .setAuthor({
          name: client.user.username,
          iconURL: client.user.displayAvatarURL({ dynamic: true }),
        })
        .setTitle("Image Command")
        .setColor("#FF1493")
        .setDescription("Enjoy, click the button to change the content!")
      // page first
      if (b.customId == "0") {
        interaction.editReply({
          embeds: [embedimg],
          components: [buttontest],
          ephemeral: true
        })
      }
    })

    		collector.on("end", () => {
			buttontest.components.forEach((btn) => btn.setDisabled(true));
			interaction.editReply({
				components: [buttontest]
			}).catch((e) => null);
		});
  },
};