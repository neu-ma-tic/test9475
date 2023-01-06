const booru = require("booru");

exports.run = (bot, message, args) => {
  message.delete();
  
  try {
    message.channel.send(
      new(require("discord.js")).MessageEmbed()
      .setColor(0xbc13fe)
      .setTitle("SIMP")
      .setImage(booru.sites("rule34.xxx"))
      .setFooter("God is watching 👁👁")
    );
  } catch(error) {
    message.channel.send(error);
  }
};