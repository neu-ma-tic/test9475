import { IBot, IBotCommand, IBotCommandHelp, IBotMessage, IBotConfig } from '../api'
import { getRandomInt } from '../utils';
import * as discord from 'discord.js';
import { faq } from '../models/faq';
import { resourceLink } from '../models/resourceLink';
import { apiRequestHandler } from '../apiRequestHandler';
import { dialogueHandler, dialogueStep } from '../dialogueHandler';

export default class AddFaqCommand implements IBotCommand {
    private readonly CMD_REGEXP = /^\?addfaq/im

    public getHelp(): IBotCommandHelp {
        return { caption: '?addfaq', description: 'ADMIN ONLY - Creates a new entry to the FAQ channel, follow the prompts' }
    }

    public init(bot: IBot, dataPath: string): void { }

    public isValid(msg: string): boolean {
        return this.CMD_REGEXP.test(msg)
    }

    cbFunc = (response: any, data: any, endEarly: any) => {
        if (data == null) {
            data = new Array<string>(response);
        }
        else {
            data.push(response);
        }
        if(data[2]){
            if(data[2] != 'yes' || data[2] == 'Yes'){
                endEarly = true;
            }
        }
        console.log("cbfunc " + endEarly);
        console.log(data.join(", "));
        return [data, endEarly];
    };

    httpFunc = (response: any, data: any, ticketuser: any, config: any) => {
        let faqObject:faq = new faq();
        faqObject.Question = data[0];
        faqObject.Answer = data[1];
        if(data[2].toLowerCase() == 'yes' && data[3] != null && data[4] != null){
            faqObject.ResourceLink = new resourceLink();
            faqObject.ResourceLink.Link = data[3];
            faqObject.ResourceLink.DisplayName = data[4];
            new apiRequestHandler().RequestAPI("POST", faqObject, 'https://dapperdinoapi.azurewebsites.net/api/faq', config);
        }
        else if(data[2].toLowerCase() != 'yes'){
            new apiRequestHandler().RequestAPI("POST", faqObject, 'https://dapperdinoapi.azurewebsites.net/api/faq', config);
        }

        return data;
    };
    
    public async process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[]): Promise<void> {
        if(!msgObj.member.hasPermission("MANAGE_MESSAGES"))
        {
            msgObj.channel.send("You don't have the privileges to add to the FAQ channel!"); //Makes sure the user has the correct permissions to be able to use this command
            return;
        }
  
        let collectedInfo;
        //datacallback

        let test: dialogueStep = new dialogueStep("Enter Question:", "Question Successful", "Question Unsuccessful", this.cbFunc, collectedInfo);
        let test2: dialogueStep = new dialogueStep("Enter Answer:", "Answer Successful", "Answer Unsuccessful", this.cbFunc, collectedInfo);
        let test3: dialogueStep = new dialogueStep("Would you like to add a resourceful URL related to the FAQ? (Enter 'Yes' if so, otherwise enter 'No')", "URL Choice Successful", "URL Choice Unsuccessful", this.cbFunc, this.httpFunc, collectedInfo);
        let test4: dialogueStep = new dialogueStep("Enter URL:", "URL Successful", "URL Unsuccessful", this.cbFunc, collectedInfo);
        let test5: dialogueStep = new dialogueStep("Enter URL Mask:", "URL Mask Successful", "URL Mask Unsuccessful", this.cbFunc, this.httpFunc, collectedInfo);

        let handler = new dialogueHandler([test, test2, test3, test4, test5], collectedInfo);

        collectedInfo = await handler.GetInput(msgObj.channel as discord.TextChannel, msgObj.member, config as IBotConfig);

        let faqEmbed = new discord.RichEmbed()
            .setTitle("-Q: " + collectedInfo[0])
            .setDescription("-A: " + collectedInfo[1])
            .setColor("#2dff2d")
        if(collectedInfo[2].toLowerCase() == 'yes')
        {
            faqEmbed.addField("Useful Resource: ", "[" + collectedInfo[4] + "](" + collectedInfo[3] + ")");
        }
        msgObj.channel.send(faqEmbed).then(newMsg =>{
            msgObj.delete(0);
        });
    }
}