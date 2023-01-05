import * as discord from 'discord.js'
import { RichEmbed } from 'discord.js'
import * as fs from 'fs'
import * as path from 'path'
import { IBot, IBotCommand, IBotConfig, ILogger } from './api'
import { BotMessage } from './message'
import { websiteBotService } from './websiteBotService'

const xp = require('../xp.json')

export class Bot implements IBot {
    public get commands(): IBotCommand[] { return this._commands }

    public get logger() { return this._logger }

    public get allUsers() { return this._client ? this._client.users.array().filter((i) => i.id !== '1') : [] }

    public get onlineUsers() { return this.allUsers.filter((i) => i.presence.status !== 'offline') }

    private readonly _commands: IBotCommand[] = []
    private _client!: discord.Client
    private _config!: IBotConfig
    private _logger!: ILogger
    private _botId!: string
    private _welcomeChannel!: discord.TextChannel
    private _websiteBotService!: websiteBotService

    public start(logger: ILogger, config: IBotConfig, commandsPath: string, dataPath: string) {
        this._logger = logger
        this._config = config

        this.loadCommands(commandsPath, dataPath)

        if (!this._config.token) { throw new Error('invalid discord token') }

        this._client = new discord.Client()

        this._client.on('ready', () => {
            this._botId = this._client.user.id
            if (this._config.game) {
                this._client.user.setGame(this._config.game)
            } else {
                this._client.user.setActivity('?commands | With Dapper Dino', {type: 'PLAYING'})
            }
            if (this._config.username && this._client.user.username !== this._config.username) {
                this._client.user.setUsername(this._config.username)
            }
            this._client.user.setStatus('online')
            this._logger.info('started...')
            this._welcomeChannel = this._client.channels.get(this._config.welcomeChannel) as discord.TextChannel
            this._websiteBotService = new websiteBotService(this._client, this._config)
            this._websiteBotService.startupService()
        })

        this._client.on('guildMemberAdd', async (member) => {
            const welcomeEmbed = new discord.RichEmbed()
                .setTitle('Welcome ' + member.user.username + '!')
                .setColor('#ff0000')
                .addField('Information', 'I\'ve just sent you a PM with some details about the server, it would mean a lot if you were to give them a quick read.')
                .addField('Thanks For Joining The Other ' + (member.guild.memberCount).toString() + ' Of Us!', 'Sincerely, your friend, DapperBot.')
            if (member.user.avatarURL != null) {
                    welcomeEmbed.setImage(member.user.avatarURL)
                } else {
                    welcomeEmbed.setImage(this._client.user.displayAvatarURL)
                }
            this._welcomeChannel.send(welcomeEmbed)
            member.send('Hello ' + member.displayName + '. Thanks for joining the server. If you wish to use our bot then simply use the command \'?commands\' in any channel and you\'ll recieve a pm with a list about all our commands. Anyway, here are the server rules:')
            const embed = new discord.RichEmbed()
                .addField('Rule 1', 'Keep the chat topics relevant to the channel you\'re using')
                .addField('Rule 2', 'No harassing others (we\'re all here to help and to learn)')
                .addField('Rule 3', 'No spam advertising (if there\'s anything you\'re proud of and you want it to be seen then put it in the showcase channel, but only once)')
                .addField('Rule 4', 'Don\'t go around sharing other people\'s work claiming it to be your own')
                .addField('Rule 5', 'You must only use ?report command for rule breaking and negative behaviour. Abusing this command will result if you being the one who is banned')
                .setThumbnail(this._client.user.displayAvatarURL)
                .setColor('0xff0000')
                .setFooter('If these rules are broken then don\'t be surprised by a ban')
            member.send(embed)
            member.send('If you are happy with these rules then feel free to use the server as much as you like. The more members the merrier :D')
            member.send('Use the command \'?commands\' to recieve a PM with all my commands and how to use them')
            member.send('(I am currently being tested on by my creator so if something goes wrong with me, don\'t panic, i\'ll be fixed. That\'s it from me. I\'ll see you around :)')
            member.addRole(member.guild.roles.find('name', 'Member'))
        })

        this._client.on('guildMemberRemove', async (member) => {
            this._welcomeChannel.send(member + ', it\'s a shame you had to leave us. We\'ll miss you :(')
        })

        this._client.on('message', async (message) => {
            if (message.author.id !== this._botId) {
                const text = message.cleanContent
                this._logger.debug(`[${message.author.tag}] ${text}`)
                if (!xp[message.author.id]) {
                    xp[message.author.id] = {
                        xp: 0,
                        level: 1
                    }
                }
                const xpAmt = Math.floor(Math.random() * 10) + 5
                const curxp = xp[message.author.id].xp // Users current xp
                const curlvl = xp[message.author.id].level // Users current level
                const nxtLvl = (xp[message.author.id].level * 200) * 1.2 // User's required xp for level up
                xp[message.author.id].xp = curxp + xpAmt // Increase the user's xp
                if (nxtLvl <= xp[message.author.id].xp) {
                xp[message.author.id].level = curlvl + 1 // Incriment level
                const embed = new discord.RichEmbed()
                    .setTitle('Level Up!')
                    .setColor('ff00ff')
                    .addField('Congratulations', message.author)
                    .addField('New Level:', curlvl + 1)
                message.channel.send(embed).then((msg) => {
                    (msg as any).delete(5000)
                })
                }
                fs.writeFile('../xp.json', JSON.stringify(xp), (err) => {
                    if (err) {
                        console.log(err)
                    }
                })
                for (const cmd of this._commands) {
                    try {
                        if (cmd.isValid(text)) {
                            const answer = new BotMessage(message.author)
                            if (!this._config.idiots || !this._config.idiots.includes(message.author.id)) {
                                await cmd.process(text, answer, message, this._client, this._config, this._commands, this._websiteBotService)
                            } else {
                                if (this._config.idiotAnswer) {
                                    answer.setTextOnly(this._config.idiotAnswer)
                                }
                            }
                            if (answer.isValid()) {
                                message.channel.send(answer.text || { embed: answer.richText })
                                    .then(console.log)
                                    .catch(console.error)
                            }
                            break
                        }
                    } catch (ex) {
                        this._logger.error(ex)
                        return
                    }
                }
            }
        })
        this._client.login(this._config.token)
    }

    private loadCommands(commandsPath: string, dataPath: string) {
        if (!this._config.commands || !Array.isArray(this._config.commands) || this._config.commands.length === 0) {
            throw new Error('Invalid / empty commands list')
        }
        for (const cmdName of this._config.commands) {
            const cmdClass = require(`${commandsPath}/${cmdName}`).default
            const command = new cmdClass() as IBotCommand
            command.init(this, path.resolve(`${dataPath}/${cmdName}`))
            this._commands.push(command)
            this._logger.info(`command "${cmdName}" loaded...`)
        }
    }
}