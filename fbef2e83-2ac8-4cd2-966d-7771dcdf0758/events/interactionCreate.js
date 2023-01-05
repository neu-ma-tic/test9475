// const conn = require(__dirname + '/../DB/DBConnection.js.js');
//
// module.exports = {
//     name: 'interactionCreate',
//     async execute(client, interaction) {
//         if (!interaction.isCommand()) return;
//
//         const command = client.commands.get(interaction.commandName);
//
//         if (!command) return;
//
//         console.log(`${interaction.user.tag} in #${interaction.channel.name} triggered an interaction.\n`
//             + `command used: ${interaction.commandName}`);
//
//         try {
//             command.execute(interaction);
//         } catch (error) {
//             console.error(error);
//             await interaction.reply({ content: 'The was error while executing this command!', ephemeral: true });
//         }
//     }
// }