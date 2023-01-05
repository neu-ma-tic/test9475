import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'
import { Bot } from '../bot';

export default class ReportCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?report/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?report', description: '(?report [@user] [reason]) to file a report claim that will be processed by the Admins' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        let reportedUser = msgObj.guild.member(msgObj.mentions.users.first());
        if(!reportedUser)
        {
            msgObj.channel.send("Sorry, I couldn't find that user");
            return;
        }
        let words = msg.split(' ');
        let reason = words.slice(2).join(' ');
        let reportEmbed = new discord.RichEmbed() //Creates embed of report details
            .setDescription("Report Details")
            .setColor("0x191a1c")
            .addField("Reported User:", reportedUser + " with ID: " + reportedUser.id)
            .addField("Reported By:", msgObj.author + " with ID: " + msgObj.author.id)
            .addField("Report in the:", msgObj.channel + " channel")
            .addField("Reported at:", msgObj.createdAt)
            .addField("Reason for report:", reason)
        msgObj.delete(0)
            .then(console.log)
            .catch(console.error);
        (client.channels.get(config.reportChannel) as discord.TextChannel).send(reportEmbed)
            .then(console.log)
            .catch(console.error);
    }
}