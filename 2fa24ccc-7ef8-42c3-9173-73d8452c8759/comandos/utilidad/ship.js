const Discord = require("discord.js");
const Canvas = require("canvas");
module.exports.run =async(client, message, args) => {

  var mencionado = message.mentions.members.first();

  if(!mencionado) return message.channel.send(`${message.author}, digame con quien va a medir su amor`);

  const fond = Canvas.createCanvas(660,220)
  const ctx = fond.getContext('2d')

  const autor = await Canvas.loadImage(message.author.displayAvatarURL({dynamic:false,size:2048,format:"png"}));

  const mencion = await Canvas.loadImage(mencionado.user.displayAvatarURL({dynamic:false,size:2048,format:"png"}));

  ctx.drawImage(autor, 0, 0, 210, 210)
  
  ctx.drawImage(mencion, 450, 0, 210, 210)
  
  let mont = Math.floor(Math.random()*(100));


  let mensaje = "";
  
  let rank = "";

  let emoji = "";

  if(0 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f615.png";
    rank = `. . . . . . . . . .`;
    mensaje = `No funcionara`
    };
  if(10 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f614.png";
    rank = `█. . . . . . . . .`;
    mensaje = `Definitivamente, no funcionara.`
    };

  if(20 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f61e.png";
        rank = `██. . . . . . . .`;
    mensaje = `Amistad es lo que veo`
    };

  if(30 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f928.png";
        rank = `███. . . . . . .`;
    mensaje = `Talvez ocurra algo`};

  if(40 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f9d0.png";
        rank = `████. . . . . .`;
    mensaje = `Posiblemente se quede en solo amigos`};

  if(50 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f914.png";
        rank = `█████. . . . .`;
    mensaje = `Puede que suceda algo`};

  if(60 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f974.png";
        rank = `██████. . . .`;
    mensaje = `Talvez una relacion no duradera`};

  if(70 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f60b.png";
        rank = `███████. . .`;
    mensaje = `Puede que se de algo que dure un tiempo `};

  if(80 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f60d.png";
        rank = `████████. .`;
    mensaje = `Un noviasgo largo y duradero`;}

  if(90 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/2764.png";
        rank = `█████████.`;
    mensaje = `Una pareja muy duradera`;}

  if(100 <= mont){
    emoji = "https://images.emojiterra.com/twitter/v13.0/512px/1f496.png";
        rank = `██████████`;
    mensaje = `Son el uno para el otro ❤`;}
    const emojis = await Canvas.loadImage(emoji)

    ctx.drawImage(emojis, 225, 5, 210, 210)
var nombre = message.author.username;
var nombre_m = mencionado.user.username;
var vuelta = nombre.split('').reverse();

var vueltita = Math.floor(nombre.length/2)
var vueltita_m = Math.floor(nombre_m.length/2)

var combo = `${vuelta.slice(vueltita).reverse().join("")+nombre_m.slice(vueltita_m)}`
const atach = new Discord.MessageAttachment(fond.toBuffer(),"imagen.png")
message.channel.send(`**${mont}** % [${rank}]\n**${mensaje}**\nNombre: **${combo}**`,atach)
}

module.exports.config = {
  name: "ship",
  aliases: ["love"],
  cooldown: "10s",
  description: "Mide tu nivel de amor con alguien 😍",
  usage: "!ship @persona",
  category: "utilidad"
}