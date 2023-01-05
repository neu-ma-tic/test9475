const { SlashCommandBuilder } = require('@discordjs/builders');
const { trackEmbed } = require(__dirname + '/../embed/trackEmbed.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('insert')
        .setDescription("Inserting student's information")
        .addStringOption(option => option.setName('stdid').setDescription('Enter a Student ID')),
    async execute({ interaction }) {
        stdID = interaction.options.getString('stdid'); // id_name
        id = stdID.substring(0, 5);
        name = stdID.substring(6, );
        if (isNaN(id)) { // ID is Not a Number
            await interaction.reply({
                content: `Student ID must be a number!\nYour entered: ${stdID}`,
                ephemeral: true
            });
            return;
        }
        else if (!isNaN(name)) { // Name is Number
            await interaction.reply({ content: `Student Name must be letters!\nYour entered: ${stdID}`, ephemeral:true });
            return;
        }
        else {
            await interaction.reply({ content: "Select Your Track!", components: [ trackEmbed ], ephemeral: true });
        }
    },
    getID() {
        const stdID = {id,name};
        return stdID;
    }
};