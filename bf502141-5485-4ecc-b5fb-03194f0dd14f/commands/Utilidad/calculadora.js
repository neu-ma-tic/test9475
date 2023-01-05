const Discord = require("discord.js");
const math = require("math-expression-evaluator");

module.exports = {
  name: "calculadora",
  aliases: ["calcular"],
  category: "Utilidad",
  description: "ayuda saquenme de pakistan",
  usage: "<>",
  cooldown: 2,
  run: async (client, message, args, color) => {
    const embed = new Discord.MessageEmbed()
  .setColor(color);
  
  if (!args[0]) {
    embed.setFooter("Por favor ingrese una `expresion`.");
    return await message.channel.send({ embeds: [embed] }); // Devuelve un mensaje si es que ejecuta el comando sin nada
  }
  let resultado;
  try {
    resultado = math.eval(args.join(" ")); // El Args toma el calculo
  } catch (e) {
    resultado = "error: Entrada Invalida"; // Cuando es incorrecta
  }
  embed.addField("Entrada:", `\`\`\`js\n${args.join(" ")}\`\`\``, false) // Te da el calculo
  .setTitle("🧮 Calculadora")
  .addField("Salida", `\`\`\`js\n${resultado}\`\`\``, false);
  await message.channel.send({ embeds: [embed] }); // Finaliza el código
// Cualquier duda, lean la doc de la NPM 
  },
};
