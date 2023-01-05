import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'

export default class RTFMCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?rtfm/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?rtfm', description: 'ADMIN ONLY - (?rtfm [@user]) - Give a noob his own discord bot bible' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        if(!msgObj.member.hasPermission("MANAGE_MESSAGES"))
        {
            msgObj.delete();
            return;
        }
        let rtfmUser = msgObj.guild.member(msgObj.mentions.users.first());
        if(!rtfmUser)
        {
            msgObj.delete();
            return;
        }
        let rtfmEmbed = new discord.RichEmbed()
            .setColor("#ff0000")
            .setTitle("The Holy Book of Discord Bots")
            .setURL('https://discord.js.org/#/docs/main/stable/general/welcome/')
            .addField("There's no need to fear " + rtfmUser.displayName + ".", msgObj.author + " is here to save you. They have bestowed upon you the holy book of Discord Bots. If you read this book each day you will by no doubt develop something great.")
            .setFooter("Always refer to this book before becoming an annoyance to the members of the 'Happy To Help' role")

        msgObj.channel.send(rtfmEmbed).then(newmsg => {
            msgObj.delete(0);
        });
    }
}