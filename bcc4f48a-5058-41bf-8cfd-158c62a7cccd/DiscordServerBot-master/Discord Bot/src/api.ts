import * as discord from 'discord.js'
import { websiteBotService } from './websiteBotService'

export interface ILoggerMethod {
    (msg: string, ...args: any[]): void
    (obj: object, msg?: string, ...args: any[]): void
}

export interface ILogger {
    debug: ILoggerMethod
    info: ILoggerMethod
    warn: ILoggerMethod
    error: ILoggerMethod
}

export interface IBotConfig {
    token: string
    welcomeChannel: string
    reportChannel: string
    kicksAndBansChannel: string
    apiBearerToken: string
    apiEmail: string
    apiPassword: string
    commands: string[]
    game?: string
    username?: string
    idiots?: string[]
    idiotAnswer?: string
}

export interface IBotCommandHelp {
    caption: string
    description: string
}

export interface IBot {
    readonly commands: IBotCommand[]
    readonly logger: ILogger
    readonly allUsers: IUser[]
    readonly onlineUsers: IUser[]
    start(logger: ILogger, config: IBotConfig, commandsPath: string, dataPath: string): void
}

export interface IBotCommand {
    getHelp(): IBotCommandHelp
    init(bot: IBot, dataPath: string): void
    isValid(msg: string): boolean
    process(msg: string, answer: IBotMessage, msgObj: discord.Message, client: discord.Client, config: IBotConfig, commands: IBotCommand[], webBotService: websiteBotService): Promise<void>
}

export interface IUser {
    id: string
    username: string
    discriminator: string
    tag: string
}

type MessageColor =
    [number, number, number]
    | number
    | string

export interface IBotMessage {
    readonly user: IUser
    setTextOnly(text: string): IBotMessage
    addField(name: string, value: string, inline: boolean): IBotMessage
    addBlankField(): IBotMessage
    setColor(color: MessageColor): IBotMessage
    setDescription(description: string): IBotMessage
    setFooter(text: string, icon?: string): IBotMessage
    setImage(url: string): IBotMessage
    setThumbnail(url: string): IBotMessage
    setTitle(title: string): IBotMessage
    setURL(url: string): IBotMessage
}