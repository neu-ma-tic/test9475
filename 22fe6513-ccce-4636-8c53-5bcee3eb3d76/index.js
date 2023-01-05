const express = require('express');
const app = express();
const Discord = require("discord.js");
require("dotenv").config();

const client = new Discord.Client({
  partials: ["MESSAGE", "CHANNEL", "REACTION"],
});
const prefix = "!";
const music_prefix = ".";
const fs = require("fs");

client.commands = new Discord.Collection();

const commandFiles = fs
  .readdirSync("./commands/")
  .filter((file) => file.endsWith(".js"));
for (const file of commandFiles) {
  const command = require(`./commands/${file}`);
  client.commands.set(command.name, command);
}

client.once("ready", async () => {
  console.log("BotJohnSon is Online!\n");
});

client.on("message", (message) => {
  if (message.author.bot) return;

  if (
    message.content.includes("+") ||
    message.content.includes("-") ||
    message.content.includes("*") ||
    message.content.includes("/") ||
    message.content.includes("%")
  ) {
    const re = /[-+*\/^%]/;
    var stringArray = message.content.split(re);
    if (allAreNumeric(stringArray) && stringArray.length == 2) {
      var ans = calculate(message, stringArray);
      if (!isNaN(ans)) {
        message.channel.send(ans + "呀！咁都要問");
      } else {
        message.channel.send("計唔到呀，計到你計啦");
      }
    }
  }

  if (message.content.includes("大件事") && message.content.includes("人講")) {
    message.reply("無人講咪你講咯");
  }
  if (message.content.includes("8964")) {
    message.channel.send(
      "⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n" +
      "⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n" +
      "⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n" +
      "⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
    );
  }
  if (message.content.includes("loli") || message.content.includes("蘿莉")) {
    client.commands.get("gif").execute(message, "loli");
  } else if (
    message.content.includes("yamete") ||
    message.content.includes("yamede")
  ) {
    message.channel.send("dame dame dameyo~ dame nanoyo~");
  } else if (
    message.content.includes("早晨") ||
    message.content.includes("morning") ||
    message.content.includes("早安") ||
    message.content.includes("早呀") ||
    message.content.includes("早啊") ||
    message.content === "早" ||
    message.content.includes("早上好")
  ) {
    message.channel.send("早晨呀！");
  } else if (
    message.content.includes("Alan Po") ||
    message.content.includes("alan po") ||
    message.content.includes("無頭髮")
  ) {
    message.channel.send(
      "https://cdn.discordapp.com/attachments/780809156889542688/796016930330378260/ezgif-2-6863cf4f01c6.gif"
    );
  } else if (message.content.includes("killer")) {
    message.channel.send(
      "https://cdn.discordapp.com/attachments/780809156889542688/796017200141828116/ezgif-2-e3917b9bd540.gif"
    );
  }
  if (
    (message.content.includes("幾時") && message.content.includes("GPA")) ||
    (message.content.includes("幾時") && message.content.includes("gpa"))
  ) {
    message.channel.send("唔知呀屌你老母！");
  }
  if (message.content.includes("英文答案")) {
    message.channel.send(
      "為你送上由寶馬山便當送出總值$10400精美英文懶人包 \nhttps://drive.google.com/folderview?id=1VB6jObDXM1d_BoOHX4IItHsOKGp2TmIf"
    );
  }
  if (message.content.includes("簽到") || message.content.includes("签到")) {
    client.commands.get("gif").execute(message, 'loli');
  }
  if (message.content.includes("你好")) {
    message.channel.send("https://na.cx/i/YCf43B8.gif");
  } else if (message.content.includes("細加號")) {
    message.channel.send("https://na.cx/i/YCf43B8.gif");
  } else if (message.content.includes("中加號")) {
    message.channel.send("https://na.cx/i/YCf43B8.gif");
  } if (
    message.content.includes("晚安") ||
    message.content.includes("night") ||
    message.content.includes("早抖")
  ) {
    message.reply("弱者先訓覺!");
  } else if (
    message.content.includes("jump") ||
    message.content.includes("想死") ||
    message.content.includes("唔想生存")
  ) {
    message.reply("https://www.sbhk.org.hk/");
  }
  if (
    message.content.includes(".gun") ||
    message.content.includes("點跟") ||
    message.content.includes(".GUN")
  ) {
    ran = Math.random() * 2;
    if (ran < 1) {
      message.channel.send("唔洗跟,我地各有各行自己嘅路");
    } else if (ran >= 1) {
      message.channel.send("無得跟!");
    }
  }
  if (message.content.includes("大家咁話")) {
    if (ran < 1) {
      message.channel.send(
        "https://tenor.com/view/%e8%a9%a6%e7%95%b6%e7%9c%9f-%e5%a4%a7%e5%ae%b6%e5%92%81%e8%a9%b1-gif-20331757"
      );
    }
  } else if (message.content.startsWith("+")) {
    const argss = message.content.slice(1).split(/ +/);
    var number = argss.shift();
    if (isNumeric(number) && number.length <= 3999) {
      number++;
      message.channel.send("+" + number);
    }
    return;
  } else if (!message.content.startsWith(prefix) && !message.content.startsWith(music_prefix) || message.author.bot) {
    return;
  }
  const args = message.content.slice(prefix.length).split(/ +/);
  const command = args.shift().toLowerCase();
  if (message.content.startsWith(prefix)) {
    switch (command) {
      case "gif":
        client.commands.get("gif").execute(message, args);
        break;
      case "rickandmorty":
        client.commands.get("rickandmorty").execute(message, args);
        break;
      case "meme":
        client.commands.get("meme").execute(message, args);
        break;
      case "weather":
        client.commands.get("weather").execute(message, args);
        break;
      case "crypto":
        client.commands.get("crypto").execute(message, args);
        break;
    }
  } else if (message.content.startsWith(music_prefix)) {
    client.commands.get('play').execute(client, message, args, command);
  }
});

function isNumeric(value) {
  return /^\d+$/.test(value);
}
function calculate(value, value2) {
  var a = parseInt(value2[0]);
  var b = parseInt(value2[1]);
  if (value.content.includes("+")) return a + b;
  else if (value.content.includes("-")) return a - b;
  else if (value.content.includes("*")) return a * b;
  else if (value.content.includes("/")) return a / b;
  else if (value.content.includes("%")) return a % b;
  else if (value.content.includes("^")) return a ^ b;
}

function allAreNumeric(value) {
  for (var i = 0; i < value.length; i++) {
    if (!isNumeric(value[i])) return false;
  }
  return true;
}

client.login(process.env.BOTTOKEN);

const port = 3000;

app.get('/', (req, res) => res.send('Hello World!'));

app.listen(port, () => console.log(`app listening at http://localhost:${port}`));