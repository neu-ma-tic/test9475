const GuildSchema = require('./models/GuildSchema');
const UserSchema = require('./models/UserSchema');

module.exports.getGuild = async (key) => {

    let guildData = await GuildSchema.findOne({ id: key });

    if (guildData) { 
        return guildData;
    } else {
        guildData = new GuildSchema({
            id: key,
        })
        await guildData.save().catch(err => console.log(err));
        return guildData;
    }
};

module.exports.getUser = async (key) => {

    let userData = await UserSchema.findOne({ id: key });

    if (userData) { 
        return userData;
    } else {
        userData = new UserSchema({
            id: key,
        })
        await userData.save().catch(err => console.log(err));
        return userData;
    }
};