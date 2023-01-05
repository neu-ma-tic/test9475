import { discordUser } from "./discordUser";

export interface suggest {
    Description: string;
    Type: SuggestionTypes;
    DiscordUser: discordUser
}

export enum SuggestionTypes{
    Bot = 0,
    Website = 1,
    General = 2,
    Youtube = 3,
    Undecided = 4
}

export class suggest implements suggest {

}