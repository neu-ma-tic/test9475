import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'
import { createSecurePair } from 'tls';
import * as fs from "fs"

const xp = require("../../xp.json");

export default class LevelCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?level/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?level', description: 'Lets you know your level and exp in the server' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        if(!xp[msgObj.author.id]){
            xp[msgObj.author.id] = {
                xp: 0,
                level: 1
            };
        }
        let curXp = xp[msgObj.author.id].xp;
        let curLvl = xp[msgObj.author.id].level;
        let nxtLvlXp = (curLvl * 200) * 1.2;
        let difference = nxtLvlXp - curXp;

        let levelEmbed = new discord.RichEmbed()
            .setTitle(msgObj.author.username)
            .setColor("#ff00ff")
            .addField("Level", curLvl, true)
            .addField("XP", curXp, true)
            .setFooter(`${difference} XP until level up`, msgObj.author.displayAvatarURL)

        msgObj.channel.send(levelEmbed).then(newMsg =>{
            msgObj.delete(0);
            (newMsg as discord.Message).delete(5000);
        })
        
        fs.writeFile("../xp.json", JSON.stringify(xp), (err) =>{
            if(err)
            {
                console.log(err);
            }
        })
    }
}