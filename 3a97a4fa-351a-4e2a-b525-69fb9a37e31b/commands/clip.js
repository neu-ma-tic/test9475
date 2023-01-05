module.exports = {
  name: "clip",
  description: "پلی کردن صدای یک کلیپ",
  async execute(message, args) {
    const { channel } = message.member.voice;
    const queue = message.client.queue.get(message.guild.id);

    if (!args.length) return message.reply("Usage: /clip <name>").catch(console.error);
    if (queue) return message.reply("شما نمیتوانید از این دستور استفاده کنید چون یک لیست پخش در حال پخش اهنگ است");
    if (!channel) return message.reply(`شما باید اول جوین یک وییس چنل بشی`).catch(console.error);

    const queueConstruct = {
      textChannel: message.channel,
      channel,
      connection: null,
      songs: [],
      loop: false,
      volume: 100,
      playing: true
    };

    message.client.queue.set(message.guild.id, queueConstruct);

    try {
      queueConstruct.connection = await channel.join();
      const dispatcher = queueConstruct.connection
        .play(`./sounds/${args[0]}.mp3`)
        .on("finish", () => {
          message.client.queue.delete(message.guild.id);
          channel.leave();
        })
        .on("error", err => {
          message.client.queue.delete(message.guild.id);
          channel.leave();
          console.error(err);
        });
    } catch (error) {
      console.error(error);
    }
  }
};
