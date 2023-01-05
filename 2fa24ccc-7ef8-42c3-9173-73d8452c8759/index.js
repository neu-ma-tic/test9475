const e = require('express')
const a = e()
a.get('/', function (rq, rs){
  rs.send('Hola Mundo :)')
})
let p = process.env.PORT || 3000;
a.listen(p)
require('dotenv').config()
/////////////////////////////////////
const Discord = require("discord.js")
const client = new Discord.Client();
const ms = require("ms")
const fs = require('fs');
require('./mongo')
const Mutedb = require("./modelos/tempmute");
const Warndb = require("./modelos/warn_member");
const WarnUp = require("./events/warnup");
const WarnConfig = require("./events/config");
client.commands = new Discord.Collection();
 fs.readdirSync("./comandos").forEach((carpeta) =>{
  const comando = fs.readdirSync(`./comandos/${carpeta}/`).filter(file => file.endsWith(".js"));
  for(files of comando){
    const command = require(`./comandos/${carpeta}/${files}`);
    client.commands.set(command.config.name, command)
  }
});
client.on("ready", () =>{
 client.login(process.env.token)
  console.log("estamos prendidos !")
  setInterval(async function (){
    let all = await Mutedb.find()
    all.map(async dato =>{
      if(dato.time < Date.now()){
        let miembro = client.guilds.resolve(dato.guildid).member(dato.userid)
        miembro.roles.remove(dato.rolid)
        await Mutedb.deleteOne({ userID: dato.userid})
      }
    })
  },10000)
});

const mod = new Map();
const cooldown = new Set();
client.on("message", async (message) =>{
  /*if(message.author.id === "649015003499855894"){
  if(message.attachments.map(a => a.url)[0]){
    console.log("image")
  }
  }*/
  if(message.author.bot || message.channel.type === "dm")return;
  var prefix = "!"
  if(message.content.startsWith(prefix)){
  var split = message.content.split(" ")
  var command = split[0].slice(prefix.length)
  var args = split.slice(1)
  let command_file = client.commands.get(command) || client.commands.find(file => file.config.aliases.includes(command))
  if(command_file){

    command_file.run(client, message, args)
  }
}
    var id = message.channel.id+message.author.id;

    var repite = mod.get(id)

    var contenido = message.content || message.attachments.map(a => a.name)[0]
    
    console.log(contenido)
    if(!repite){
      mod.set(id,{
      r: 2,
      c: contenido
    });
    }else{
      if(contenido === repite.c){
      if(repite.r == 3){
        mod.set(id,{
        r: 1,
        c: contenido
       });
       
       var persona = message.member
       var razon = "El mismo mensaje 3 veces";
       WarnUp.run(message, persona, razon);
      return WarnConfig.run(message, persona)
      }
      mod.set(id,{
        r: repite.r+1,
        c: contenido
      })
    }else{
      mod.set(id,{
      r: 2,
      c: contenido
    });
    }
    }
  });
  client.login(process.env.token)