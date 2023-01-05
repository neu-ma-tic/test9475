const Command = require("../Structres/Command.js");

module.exports = new Command({
    name: "clear",
    description: "清除訊息",
    aliases:["cc"],
    permission: "MANAGE_MESSAGES",
    async run(message, args, client) {

        const amount = args[1];

        if (!amount || isNaN(amount))
            return message.reply(
                `${amount ==  undefined ? "Nothing":amount 
                } 不是有效的數字!`
            ); 
        const amountParsed = parseInt(amount);

        if (amountParsed > 100) return message.reply("清除訊息上限為100!");

        message.channel.bulkDelete(amountParsed+1,true);

        const msg = await message.channel.send(`清除了${amountParsed}則訊息`);

        setTimeout(() => msg.delete, 3000);
    }


});