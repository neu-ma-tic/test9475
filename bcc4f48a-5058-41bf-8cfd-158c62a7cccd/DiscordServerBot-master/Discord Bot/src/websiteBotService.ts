import * as aspnet from '@aspnet/signalr'
import * as discord from 'discord.js'
import * as api from './api.js'
import { ApiRequestHandler } from './apiRequestHandler.js'
import { compactDiscordUser } from './models/compactDiscordUser.js'
import { email } from './models/email.js'

(global as any).XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest

export class websiteBotService {

    private _serverBot: discord.Client
    private _config: api.IBotConfig

    constructor(serverBot: discord.Client, config: api.IBotConfig) {
        this._serverBot = serverBot
        this._config = config
    }

    public startupService = () => {

        const connection = new aspnet.HubConnectionBuilder()
            .withUrl('https://dapperdino.azurewebsites.net/discordbothub')
            .configureLogging(aspnet.LogLevel.Information)
            .build()
        connection.start().catch((err) => console.error(err.toString()))

        connection.on('ReceiveMessage', (user, message) => {
            const testUser = this._serverBot.users.get(this.GetDiscordUserByUsername(user).DiscordId)
            if (testUser) {
                testUser.send(message)
                    .catch(console.error)
            }
        })
    }

    public GetServerPopulation() {
        return this._serverBot.users.array().length
    }

    public GetDiscordUserByUsername(username: string) {
        const allUsers = this._serverBot.users.array()
        let user
        for (user of allUsers) {

            if (user.username === username) {
                console.log('Found User')
                break
            }
        }
        const userObject = new compactDiscordUser()
        if (user != null) {
            userObject.Username = user.username
            userObject.DiscordId = user.id
        }
        return userObject
    }

    public GetDiscordUserById(id: string) {
        const allUsers = this._serverBot.users.array()
        let user
        for (user of allUsers) {
            if (user.id === id) {
                break
            }
        }
        const userObject = new compactDiscordUser()
        userObject.Username = user.username
        userObject.DiscordId = user.id

        return userObject
    }

    public GetDiscordUserByEmail(emailAddress: string) {
        const emailObject = new email()
        emailObject.Email = emailAddress
        const responseData = new ApiRequestHandler().RequestAPI('POST', emailObject, 'https://dapperdinoapi.azurewebsites.net/api/search/user', this._config)
        console.log(responseData)
    }
}