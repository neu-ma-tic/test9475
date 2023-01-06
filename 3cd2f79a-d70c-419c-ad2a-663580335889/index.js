var help=["fuck","fkcu","fumck","fusck","fushk","furck","shucklehead","ash","piss","shit","pee","poo","fu-ck"]
const Discord = require("discord.js");
const client = new Discord.Client();
client.on("ready", () => {
  console.log("I am ready!");
  autorun=true
});
g=true
var n=0
client.setMaxListeners(100)
client.on("message", (message) => {
	if (message.content.includes("not allowed")) {
		message.channel.startTyping(96)
		message.channel.stopTyping()
		message.reply("fuck, i can say it");
		return;
	}
	if (message.content=="/servers"){
		message.reply(n+" servers")
	}
	if (message.content=="/welcome lovebot"){
		n+=1
	}
	if (message.content=="/bye lovebot") {
		n-=1
	}
	if (message.content.startsWith("*")) return;
	if (message.content.startsWith("!")) return;
	if (message.content.startsWith("?")) return;
	if (g==true) {
		g=false;
	}
	if (message.content.includes("who is your owner")){
		message.reply("my owner is dart2.0");
		return;
	}
	if (message.author.bot) return;
  	if (message.content.includes("movie")){
		message.reply(":film_frames:");
		return;
	}
	else if (message.content.includes("film")){
		message.reply(":film_frames:");
		return;
	}
	else if (message.content.includes("bike")){
		message.reply(":bike:");
		return;
	}
	else if (message.content.includes("stop")){
		message.reply(":no_entry:");
		return;
	}
	else if (message.content.includes("plane land")){
		message.reply(":plane_arriving:");
		return;
	}
	else if (message.content.includes("plane t")){
		message.reply(":plane_departure:");
		return;
	}
	else if (message.content.includes("plane")){
		message.reply(":airplane:");
		return;
	}
	else if (message.content.includes("hash")){
		message.reply(":hash:");
		return;
	}
	else if (message.content.includes("secret: ")){
		message.reply("||"+(message.content)+"||")
		return;
	}
	else if (message.content.includes("lovebot.destroy")) {
	  message.reply("destroying");
	  user=client.destroy()
  	}
	for (l in help){
	  	if (message.content.includes(help[l])){
			message.reply(":no_entry_sign:")
			return
	  	}
  	}
	if (message.content.includes("mute")){
		(message.reply(":mute:"))
	}
	else if (message.content.includes("pict")){
		message.reply("__/\\ /\\ __")
		message.reply("╠╦═╬╗")
		message.reply("■♪♥¿ª☺º◘")
		message.reply("‗↕↕¤∟←↓↨→•")
		message.reply("¶↨ı▼æ©°▄¨µ©")
		message.reply("¦♠▒▀▀«Þø▬☻¦")
	}
	else if (g==true){ message.reply("HI I'M HERE TO HELP YOU");
	}
	else if (message.content.includes("invite")){
		message.reply("you can invite me at https://discordapp.com/oauth2/authorize?client_id=655415053306036245&permissions=8&scope=bot")
	}
	else if (message.content.startsWith("hi")) {
		message.reply("hi how can i help you?");
		message.author.send("hi")
	} else
	if (message.content.startsWith("hello")) {
		message.reply("hi how can i help you?");
	}
	else if (message.content.startsWith("help")) {
		message.reply("how can i help you?");
	}
	else if (message.content.includes("server")){
		client.login("NjU1NTA1ODM5ODM4NDYxOTgz.XfefQQ.WXDg3BsO3Ph1ee3dxA2w5huRxAc");
	}
	else if (message.content.includes("java")) {
    message.reply("i'm written in java");
  }
  else if (message.content.includes("how are you")) {
    message.reply("I'm fine thanks, and you");
  }
  else if (message.content.includes("who are you")) {
    message.reply("I'm Dart2.0 and who are you in real live, "+message.author+"?");
  }
  else if (message.content.includes("see")) {
    message.reply("I'm fine thanks, and you");
  }
  else if (message.content.includes("weather")) {
  	message.reply("It is well i think")
  }
  else if (message.content.includes("what can i do")) {
  	message.reply("You can talk to me")
  } //else {
	  //message.reply("for bot help say !help or ?help")
  //}
  else if (message.content.includes("bot talk")){
  if (message.channel.name=="bot-talk"){
	  message.channel.setName("@starter-channel")
	  message.reply("bot talk off")
  }
  else {
  message.channel.setName("@bot talk")
  message.reply("bot talk on")
  }
  }
  else if (message.content.includes("owner")){
	  message.guild.owner.send(message.author+" asked for you")
  }
  else if (message.content.includes("")){
	message.reply("☻♠╦♪╦♣╦♪╦♠☻")
  }
  
});

client.login("NjU1NTA1ODM5ODM4NDYxOTgz.XfoPwg.j3jHzXYye1aAkN4ryKtU1vfWmLU");
