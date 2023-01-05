module.exports = {
    name: 'leave',
    aliases: ["dc"],
    description: 'تمامی اهنگ ها رو متوقف میکنه و بات رو از چنل خارج میکنه',
    async execute(message, args) {
        const voiceChannel = message.member.voice.channel;
 
        if(!voiceChannel) return message.channel.send("شما حتما باید در یک وویس چنل جوین باشید");

        const goodbyes = [
                "فعلا خداحافظ شما",
                "به سلامت",
                "قربانت یاعلی",
                "خوش گذشت فردا هم بیا",
                "سلام برسون",
                "داوش ما رفتیم",
                
                
       ]

       const goodbye = goodbyes[Math.floor(Math.random() * goodbyes.length)]









        await voiceChannel.leave();
        await message.channel.send(`${goodbye}`)
 
    }
}