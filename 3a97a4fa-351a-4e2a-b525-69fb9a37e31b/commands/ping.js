module.exports = {
  name: "ping",
  cooldown: 10,
  description: "نشان دادن پینگ بات",
  execute(message) {
    message.reply(`📈 پینگ بات به شما: ${Math.round(message.client.ws.ping)} ms`).catch(console.error);
  }
};
