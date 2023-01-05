module.exports = {
    name: 'ban',
    description: `\`\`\`
    Command: c?ban
    Description: TODO
    \`\`\``,
    
    async execute(msg, ...args) {
        msg.reply(`c?ban: ${args}`)
    }
}