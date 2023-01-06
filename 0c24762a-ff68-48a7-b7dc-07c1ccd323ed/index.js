
const Discord = require('discord.js');

const client = new Discord.Client();

var channelRecepce;
var channelPing;
const newUsers = new Discord.Collection();

const narutoGifs = ["https://tenor.com/view/gtg-omw-gotta-blast-naruto-run-gif-5552832.gif", "https://tenor.com/view/zanuto-naruto-run-zanb-twitch-streamer-gif-17322459.gif", "https://tenor.com/view/area51raid-area51-alien-aliens-naruto-run-gif-15092690.gif", "https://tenor.com/view/kookie-naruto-run-gif-7251770.gif", "https://tenor.com/view/naruto-running-anime-gif-8479684.gif", "https://tenor.com/view/naruto-run-shadow-funny-gif-11517603.gif", "https://tenor.com/view/naruto-naruto-run-weeb-weeb-naruto-running-away-gif-13207948.gif", "https://tenor.com/view/naruto-fatboy-run-fast-ninja-gif-11322683.gif", "https://tenor.com/view/run-beach-naruto-run-gif-14342203.gif", "https://tenor.com/view/gtg-omw-gotta-blast-naruto-run-gif-5552832.gif"];

var http = require('http');

http.createServer(function(req, res) {
  res.write("I'm alive");
  res.end();
}).listen(8080);



client.on("ready", () => {
  channelRecepce = client.channels.cache.find(channel => channel.id == "791282463984320533");
  channelPing = client.channels.cache.find(channel => channel.id == "790728748650725406");
  client.user.setActivity("Ψhelp", {
    type: "WATCHING"
  });
  console.log("Poskok je online!");
});

client.on("guildMemberAdd", (member) => {
  newUsers.set(member.id, member.user);
  channelRecepce.send(`Dborý den, <@${member.user.id}>, jen malá vstupní otázečka...`);
  setTimeout(function() {
    channelRecepce.send(`<@${member.user.id}> Jste e-girl? (Odpovězte \"Ano\" nebo \"Ne\")`);
  }, 2000);
});

client.on('message', (msg) => {
  if(msg.content.length < 1){
    return;
  }
  if(msg.content.toLowerCase() == "ψhelp"){
    msg.channel.send("Ne, to nefunguje.");
    return;
  }
  let domCont = msg.content.toLowerCase();
  if(domCont.length<30 && domCont.includes("klidn") && (domCont.includes("dominik") || domCont.includes("domc") || domCont.includes("domč") || domCont.includes("domis") || domCont.includes("domís") || domCont.includes("doman") || domCont.includes("domán"))){
    msg.channel.send("<@659333475245096962> Klidni hormon pls");
  }
  if (msg.channel.id == channelRecepce.id) {
    if (!(msg.member.roles.cache.size === 1)) {
      newUsers.delete(msg.member.id);
    }
    if (newUsers.has(msg.member.id)) {
      let cont = msg.content.toLowerCase();
      while(cont.includes('!')){
        cont = cont.replace('!', '');
      }
      if (cont == "ano" || cont == "jo" || cont == "jj" || cont == "jop" || cont == "yes" || cont == "samozřejmě" || cont == "samozrejme") {
        newUsers.delete(msg.member.id);
        channelRecepce.send(`<@${msg.member.id}> Naši moderátoři už jsou na cestě!`, { files: [narutoGifs[Math.floor(Math.random() * narutoGifs.length)]] });
        channelPing.send(`<@&790710882580561972> <@&790710959605678090> <@&790710928869556244> <@&790710997992079392> Je tu e-girl, přidělte ji roli!`, { files: ["https://tenor.com/view/discord-gif-18948777.gif"] });
      }
      else if (cont == "ne" || cont == "nn" || cont == "nope" || cont == "nop" || cont == "no") {
        newUsers.delete(msg.member.id);
        channelRecepce.send(`<@${msg.member.id}> Rozumím, ve lhůtě 30 dní budou moderátoři vyrozuměni o vaší existenci a možná vám přidělí roli.`);
      }
      else if (cont == "perhaps" || cont == "maybe" || cont == "mozna" || cont == "možná" || cont == "nevim") {
        channelRecepce.send(`Haha, humorné. <@${msg.member.id}> a teď odpověz \"Ano\" nebo \"Ne\"`);
      }
      else {
        channelRecepce.send(`Cococococo? <@${msg.member.id}> Odpověz \"Ano\" nebo \"Ne\"`);
      }
    }
  }
});



client.login('NzkxMDc2MTcyOTU1OTEwMTY1.X-J5GQ.LVLBzMxC_egEY7ztItHkLLYWDOk');
