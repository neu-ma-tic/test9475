const { canModifyQueue } = require("../util/EvobotUtil");

module.exports = {
  name: "volume",
  aliases: ["v"],
  description: "عوض کردن میزان صدای بات",
  execute(message, args) {
    const queue = message.client.queue.get(message.guild.id);

    if (!queue) return message.reply("در حال حاضر هیچ اهنگی پلی نمیشود").catch(console.error);
    if (!canModifyQueue(message.member))
      return message.reply("داش باید اول جون یک وویس چنل بشی").catch(console.error);

    if (!args[0]) return message.reply(`🔊 در حال حاضر میزان صدا: **${queue.volume}%** است`).catch(console.error);
    if (isNaN(args[0])) return message.reply("لطفا از یک تا صد یک عدد را بدون علامت درصد بنویسید").catch(console.error);
    if (Number(args[0]) > 100 || Number(args[0]) < 0 )
      return message.reply("لطفا یک عدد بین یک تا صد رو انتخاب کنید").catch(console.error);

    queue.volume = args[0];
    queue.connection.dispatcher.setVolumeLogarithmic(args[0] / 100);

    return queue.textChannel.send(`میزان صدا تنظیم شد: **${args[0]}%**`).catch(console.error);
  }
};
