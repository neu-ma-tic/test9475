const {MessageEmbed} = require('discord.js')
const api = require('imageapi.js')

module.exports = {
    name: 'meme',
    description: 'Memes!',
    async execute(client, message, args) {
        let subreddits = [
            'comedyheaven',
            'dank',
            'meme',
            'memes'
         ]

         let subreddit = subreddits[Math.floor(Math.random()*(subreddits.length))]
         console.log(subreddit)
         let img = await api(subreddit)
         console.log(img)

         const embed = new MessageEmbed()
         .setTitle(`A meme from r/${subreddit}`)
         .setURL(`https://reddit.com/r/${subreddit}`)
         .setColor('RANDOM')
         .setImage(img)
         .setFooter('Bot made by ImJari#6285')
         message.channel.send(embed)
     }
}