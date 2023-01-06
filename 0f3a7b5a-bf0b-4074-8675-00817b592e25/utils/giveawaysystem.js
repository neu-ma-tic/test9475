module.exports = async (Discord, bot) =>{

    let fs = require('fs');
    const { GiveawaysManager } = require('discord-giveaways');
    const prefix  = config.BOT_PREFIX;
    // Load Enmap
    const Enmap = require('enmap');
    // Create giveaways table
    const giveawayDB = new Enmap({ name: 'giveawayDB' });
    const GiveawayManagerWithOwnDatabase = class extends GiveawaysManager {
        // This function is called when the manager needs to get all giveaways which are stored in the database.
        async getAllGiveaways() {
            // Get all giveaways from the database
            return giveawayDB.fetchEverything().array();
        }
    
        // This function is called when a giveaway needs to be saved in the database.
        async saveGiveaway(messageID, giveawayData) {
            // Add the new giveaway to the database
            giveawayDB.set(messageID, giveawayData);
            // Don't forget to return something!
            return true;
        }
    
        // This function is called when a giveaway needs to be edited in the database.
        async editGiveaway(messageID, giveawayData) {
            // Replace the unedited giveaway with the edited giveaway
            giveawayDB.set(messageID, giveawayData);
            // Don't forget to return something!
            return true;
        }
    
        // This function is called when a giveaway needs to be deleted from the database.
        async deleteGiveaway(messageID) {
            // Remove the giveaway from the database
            giveawayDB.delete(messageID);
            // Don't forget to return something!
            return true;
        }
    };
    // We now have a giveawaysManager property to access the manager everywhere!
    bot.giveaways = new GiveawayManagerWithOwnDatabase(bot, {
        updateCountdownEvery: 10000,
        botsCanWin: false,
        exemptPermissions: ['MANAGE_MESSAGES', 'ADMINISTRATOR'],
        embedColor: '#00ff00',
        embedColorEnd: '#FF0000',
        reaction: '🎉'
    });
    
    // bot.giveaways = new GiveawaysManager(bot, {
    //     storage: "./commands/giveaways/giveaways.json",
    //     updateCountdownEvery: 10000,
    
    //     botsCanWin: false,
    //     exemptPermissions: ['MANAGE_MESSAGES', 'ADMINISTRATOR'],
    //     embedColor: '#00ff00', // green
    //     embedColorEnd: '#FF0000', // red
    //     reaction: '🎉'
    // });
    // ------ SET BOT COMMANDS ------ //
    bot.commands = new Discord.Collection();
    bot.aliases = new Discord.Collection();
    bot.categories = fs.readdirSync("././commands/");
    ["command"].forEach(handler => {
        require(`../handlers/${handler}`)(bot);
    }); 
    bot.on('message', async message =>{
        if(message.author.bot) return;
        if(!message.content.startsWith(prefix)) return;
        if(!message.guild) return;
        if(!message.member) message.member = await message.guild.fetchMember(message);
        const args = message.content.slice(prefix.length).trim().split(/ +/g);
        const cmd = args.shift().toLowerCase();
        if(cmd.length == 0 ) return;
        let command = bot.commands.get(cmd)
        if(!command) command = bot.commands.get(bot.aliases.get(cmd));
        if(command) command.run(bot, message, args) 
    })

}