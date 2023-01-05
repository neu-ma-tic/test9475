import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'
import { websiteBotService } from '../websiteBotService';

export default class ServerInfoCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?serverinfo/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?serverinfo', description: 'Here is some information about our server' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[], websiteBotService: websiteBotService): Promise<void> {
        answer.setDescription("Server Information");
        answer.setColor("0xff0000");
        answer.setThumbnail(msgObj.guild.iconURL);
        answer.addField("The best server ever:", msgObj.guild.name, false);
        answer.addField("Was created on:", msgObj.guild.createdAt.toString(), false);
        answer.addField("You joined us on:", msgObj.member.joinedAt.toString(), false);
        answer.addField("Our member count is currently at:", websiteBotService.GetServerPopulation().toString(), false);
    }
}