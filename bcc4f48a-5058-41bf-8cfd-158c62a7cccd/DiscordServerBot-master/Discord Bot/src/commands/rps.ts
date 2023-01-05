import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils'
import * as discord from 'discord.js'
import * as fs from 'fs'

const gameScores = require("../../gameScores.json");

export default class RPSCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?rps/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?rps', description: '(?rps [choice]) Play rock, paper, scissors against the me. Replace choice with either rock, paper or scissors. Eg. ?rps rock' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        let words = msg.split(' ');
        let choice = words.slice(1).join(' ');
        let possibleChoices = ['rock', 'paper', 'scissors'];
        let botChoice = possibleChoices[Math.floor(Math.random() * 3)]
        let rpsEmbed = new discord.RichEmbed()
            .setTitle("Rock, Paper, Scissors")
            .setColor("#ff0000")
        if(choice == botChoice)
        {
            rpsEmbed.addField("We tied!", "We both picked " + choice + "! What a coincidence", false);
            gameScores.rpsTies += 1;
        }
        else if(choice == "rock")
        {
            if(botChoice == "scissors")
            {
                rpsEmbed.addField("Congratulations","You beat me with your " + choice + " against my " + botChoice + "!",false);
                gameScores.rpsLosses += 1;
            }
            else
            {
                rpsEmbed.addField("What a shame...","I beat you with my " + botChoice + " against your puny " + choice + "!",false);
                gameScores.rpsWins += 1;

            }
        }
        else if(choice == "paper")
        {
            if(botChoice == "rock")
            {
                rpsEmbed.addField("Congratulations","You beat me with your " + choice + " against my " + botChoice + "!",false);
                gameScores.rpsLosses += 1;
            }
            else
            {
                rpsEmbed.addField("What a shame...","I beat you with my " + botChoice + " against your puny " + choice + "!",false);
                gameScores.rpsWins += 1;
            }
        }
        else if(choice == "scissors")
        {
            if(botChoice == "paper")
            {
                rpsEmbed.addField("Congratulations","You beat me with your " + choice + " against my " + botChoice + "!",false);
                gameScores.rpsLosses += 1;
            }
            else
            {
                rpsEmbed.addField("What a shame...","I beat you with my " + botChoice + " against your puny " + choice + "!",false);
                gameScores.rpsWins += 1;
            }
        }
        else
        {
            rpsEmbed.addField("Failed to play Rock, Paper, Scissors", "Make sure that you entered the command properly",false);
            rpsEmbed.addField("Here is an example: ", "?rps paper", false);
        }
        fs.writeFile("../gameScores.json", JSON.stringify(gameScores), (err) =>{
            if(err)
            {
                console.log(err);
            }
        })
        rpsEmbed.addField("My stats", "Wins: " + gameScores.rpsWins + ". Losses: " + gameScores.rpsLosses + ". Ties: " + gameScores.rpsTies + ".",false);
        msgObj.channel.send(rpsEmbed).then(newMsg =>{
            msgObj.delete(0);
            (newMsg as discord.Message).delete(5000);
        });      
    }
}