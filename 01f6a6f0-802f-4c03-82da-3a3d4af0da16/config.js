module.exports = {
    owner: process.env.OWNERID,
    prefix: process.env.COMMAND_PREFIX,
    defaultGuildSettings: {
        prefix: process.env.COMMAND_PREFIX,
        welcomeMessage: {
            enabled: false,
            welcomeMessage: "Welcome **{{member}}** to **{{server}}**!",
            channelID: null
        },
        soundboardRole: "",
        modRole: "",
        adminRole: "",
        logChannel: "1030756515109408788"
    }
}