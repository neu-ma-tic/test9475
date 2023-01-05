module.exports = {
  name: "ping",
  description: "shows user ping.",
  execute(message, args) {
    message.channel.send("Pinging...").then(msg =>{
      const ping = msg.createdTimestamp - message.createdTimestamp;
      msg.edit(`cutebot ping is ${ping}ms`)
    })
  }
}