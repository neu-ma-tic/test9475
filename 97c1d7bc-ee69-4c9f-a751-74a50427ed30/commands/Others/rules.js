const { MessageEmbed } = require('discord.js')
const moment = require('moment') // npm i moment
moment.locale('ENG')

module.exports ={
    commands: ['rules'], 
    permissions: 'ADMINISTRATOR', // You Can Keep Any Permissions
    description: 'Shows User Info About A User or Pinged User.', // Optional

    callback: (message, args) => {

        message.delete()

        const embed = new MessageEmbed()
        .setColor('#313131')
        .setTitle(``)
        .setDescription("📜 ︱**Základní Pravidla**\n\n> Chovej se jako člověk a ne jako dítě.\n\n> Zbytečně nespamovat (Platí pro všechny textové kanály).\n\n> Na serveru platí také základní discord pravidla. [GUIDELINES](https://discordapp.com/guidelines), [SAFETY](https://discord.com/new/safety)\n\n 📜 ︱**Zákazy**\n\n> Je zakázáno jakkoliv vyznávat Fašizmus, Nacizmus, Rasizmus, nevhodná slova či obrázky, gify, url odkazy!\n\n> Je zakázáno jakkoliv rozesílat pornografii, nevhodná videa, crash gify!\n\n> Ve voice chatu je zakázáno sdílet nevhodný obsah např. pornografie, Fašizmus, Nacizmus, Rasizmus a mnoho dalšího nevhodného kontentu.\n\n> Je zakázáno jakkoliv propagovat obsah bez povolení Vedení toho discord server.\n\n 📜 ︱**Důležíté**\n\n> Je zakázáno jakkoliv hledat či slovíčkařit ohledně pravidel. (Může být potrestáno banem či mutem!).")
        // Add More Fields If Want
        message.channel.send(embed)
    }
}
