const { SlashCommandBuilder } = require('@discordjs/builders');
const conn = require(__dirname + "/../DB/DBConnection.js");

module.exports = {
    data: new SlashCommandBuilder()
        .setName('select')
        .setDescription('select all student!'),
    async execute({ interaction, ...params }) {
        await conn.query("SELECT * FROM atd_list", function (err, result, fields) {
            if (err) throw err;
            console.log(result);
        })
    }
}