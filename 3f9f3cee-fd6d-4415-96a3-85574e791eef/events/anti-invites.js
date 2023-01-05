const client = new require("..");

client.on("messageCreate", async (message) => {
  if (!message.guild) return;

  function deleteMessage() {
    message.delete();
    message.channel.send("NO ADV IN HERE");
  }

  const links = ["discord.gg/", "discord.com/invite/", "discord.xyz/"];

  for (const link of links) {
    //example: discord.gg/, discord.com/invite/,
    //array: ['Come join to my server', 'please come']

    if (!message.content.includes(link)) return;

    const code = message.content.split(link)[1].split(" ")[0];
    const isGuildInvite = message.guild.invites.cache.has(code);

    if (!isGuildInvite) {
      try {
        const vanity = await message.guild.fetchVanityData();
        if (code !== vanity?.code) return deleteMessage();
      } catch (err) {
        deleteMessage();
      }
    }
  }
});
