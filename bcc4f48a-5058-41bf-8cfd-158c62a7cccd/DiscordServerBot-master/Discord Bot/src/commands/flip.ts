import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'

export default class DoggoCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?flip/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?flip', description: 'Flips a coin. Landing on either heads or tails' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        let options = ['your coin landed on tails', 'your coin landed on heads'];
        answer.setTitle(msgObj.author.username + ", " + options[Math.floor(Math.random()*options.length)]);
        answer.setColor("#ffe100");
    }
}