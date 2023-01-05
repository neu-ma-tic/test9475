import {Client, Collection, Intents} from "discord.js";
import { readdirSync } from "fs";
import { ICommand } from "./interfaces/ICommands";
import { IEvent } from "./interfaces/IEvents";

class Bot extends Client{
    public prefix : string;
    public commands : Collection<string, ICommand> = new Collection();
    public event : Collection<string, IEvent> = new Collection();

    public constructor() {
        super();
    }

    public init = () => {
        this.prefix = process.env.DISCORD_PREFIX;
        
        this.login(process.env.DISCORD_TOKEN);

        const command_files = readdirSync("./commands/").filter((file) => file.endsWith(".ts"));
        command_files.map(async (fileName:string) => {
            const command = (await import(`./commands/${fileName}`)) as ICommand;
            this.commands.set(command.name, command);
        });

        let dirs = ["client", "server"];

        var event_files;
        const load_dir = async (dirs) => {
            event_files = readdirSync(`./events/${dirs}`).filter((file) => file.endsWith(".ts"));

            event_files.map(async (filename: string) =>{
                const event = (await import(`./events/${dirs}/${filename}`)) as IEvent;

                const event_name = event.name;
                this.on(event_name, event.execute.bind(null, this));
            })
        }
        ["client", "server"].forEach((e) => load_dir(e));
    }
}
export {Bot};