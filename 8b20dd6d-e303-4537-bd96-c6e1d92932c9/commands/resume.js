const { canModifyQueue } = require("../util/EvobotUtil");

module.exports = {
  name: "resume",
  aliases: ["r"],
  description: "شروع دباره پخش یک اهنگ",
  execute(message) {
    const queue = message.client.queue.get(message.guild.id);
    if (!queue) return message.reply("در حال حاضر چیزی پخش نمیشود").catch(console.error);
    if (!canModifyQueue(message.member)) return;

    if (!queue.playing) {
      queue.playing = true;
      queue.connection.dispatcher.resume();
      return queue.textChannel.send(`${message.author} ▶ موزیک را پخش کرد`).catch(console.error);
    }

    return message.reply("لیست پخش استاپ نشده").catch(console.error);
  }
};
