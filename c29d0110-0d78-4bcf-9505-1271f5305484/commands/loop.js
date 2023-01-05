const { canModifyQueue } = require("../util/EvobotUtil");

module.exports = {
  name: "loop",
  aliases: ["l"],
  description: "تکرار اهنگ های لیست",
  execute(message) {
    const queue = message.client.queue.get(message.guild.id);
    if (!queue) return message.reply("در حال حاضر اهنگی در حال پلی شدن نیست").catch(console.error);
    if (!canModifyQueue(message.member)) return;

    // toggle from false to true and reverse
    queue.loop = !queue.loop;
    return queue.textChannel.send(`تکرار اهنگ${queue.loop ? "**روشن**" : "**خاموش**"}است`).catch(console.error);
  }
};
