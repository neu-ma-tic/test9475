import { compactDiscordUser } from "./compactDiscordUser";

export interface discordUser extends compactDiscordUser{
    Name: string
}

export class discordUser implements discordUser {
    
}