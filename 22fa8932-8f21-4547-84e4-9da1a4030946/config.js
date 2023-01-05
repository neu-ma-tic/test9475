module.exports = {
    owner: process.env.OWNERID,
    prefix: "m!"
    defaultGuildSettings: {
        prefix: "m!",
        welcomeMessage: {
            enabled: false,
            welcomeMessage: "Welcome **{{member}}** to **{{server}}**!",
            channelID: null
        },
        soundboardRole: "Soundboard DJ",
        modRole: "Moderator",
        adminRole: "Administrator",
        logChannel: "EXA-logs"
    }
}