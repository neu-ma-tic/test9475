import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'

export default class CommandsCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?commands/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?commands', description: 'Sends you a list of all our commands, that\'ts how you got here in the first place' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        let helpEmbed = new discord.RichEmbed()
            .setTitle("Here is a list of all our commands")
            .setColor("#ff0000");
        let helpObj;
        for (const cmd of commands)
        {
            helpObj = cmd.getHelp();
            helpEmbed.addField(helpObj.caption,helpObj.description,false);
        }
        msgObj.author.send(helpEmbed);
        let confirmationEmbed = new discord.RichEmbed()
            .setTitle("Hello " + msgObj.author.username)
            .setColor("#ff0000")
            .addField("I've just sent you a pm with all the server's commands","I hope you enjoy your time here and make the most out of me, DapperBot",false)
        msgObj.channel.send(confirmationEmbed).then(newMsg =>{
            msgObj.delete(0);
            (newMsg as discord.Message).delete(5000);
        });
    }
}