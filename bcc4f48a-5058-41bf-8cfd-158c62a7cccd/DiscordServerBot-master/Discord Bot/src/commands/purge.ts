import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'

export default class PurgeCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?purge/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?purge', description: 'ADMIN ONLY - (?purge [@user] [number of message to delete]) Bulk delete a number of this user\'s messages from the channel' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        msgObj.delete(0);
        if(!msgObj.member.hasPermission("MANAGE_MESSAGES"))
        {
            return;
        }
        let purgedUser = msgObj.guild.member(msgObj.mentions.users.first());
        if(!purgedUser)
        {
            return;
        }
        if(purgedUser.hasPermission("MANAGE_MESSAGES"))
        {
            return;
        }
        let words = msg.split(' ');
        let amount = parseInt(words.slice(2).join(' '));
        if(isNaN(amount))
        {
            return;
        }
        msgObj.channel.bulkDelete(amount)
            .then(messages => console.log(`Bulk deleted ${messages.size} messages`))
            .catch(console.error)
    }
}