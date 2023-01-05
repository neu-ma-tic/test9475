import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'

export default class BotInfoCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?botinfo/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?botinfo', description: 'Here is some information about me, DapperBot' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        answer.setDescription("Bot Information");
        answer.setColor("0xff0000");
        answer.setThumbnail(client.user.displayAvatarURL);
        answer.addField("My name is DapperBot", "My goal in life is to make your life easier, and more fun :D", false);
        answer.addField("I was born on:", client.user.createdAt.toString(), false);
    }
}