import * as discord from 'discord.js'
import * as api from './api.js'

export class dialogueHandler {
    private _steps: dialogueStep[] | dialogueStep
    private _data: any
    private _endEarly: boolean

    /**
     *
     */
    constructor(steps: dialogueStep[] | dialogueStep, data: any) {
        this._steps = steps
        this._data = data
        this._endEarly = false
    }

    public async GetInput(channel: discord.TextChannel, ticketUser: discord.GuildMember, config: api.IBotConfig) {
        // Create array for single dialogueStep to prevent extra checks + coding
        if (!Array.isArray(this._steps)) {
            this._steps = [this._steps]
        }
        for (const step of this._steps) {
            const filter = (m) => (m.member === ticketUser)

            // tslint:disable-next-line:one-variable-per-declaration
            let response, beforeM

            channel.send(ticketUser + ', ' + step.beforeMessage).then((newMsg) => {
                beforeM = newMsg
            })

            await channel.awaitMessages(filter, { max:  1})
                .then((collected) => {
                    response = collected.array()[0]

                    if (step.callback != null) {
                         [this._data, this._endEarly] = step.callback(response.content, this._data, this._endEarly)

                    }

                    if (step.httpCallback != null) {
                        this._data = step.httpCallback(response.content, this._data, ticketUser, config)
                    }

                    console.log('DH ' + this._endEarly)

                    // channel.send(step.succeedMessage).then(newMsg =>{
                    //    (newMsg as any).delete(1000);
                    // });
                })
                .catch((collected) => {
                    console.log(console.error(collected))
                    channel.send(step.errorMessage)
                })
            beforeM.delete(0)
            response.delete(0)
            if (this._endEarly === true) {
                return this._data
            }
        }

        return this._data

    }
}

export class dialogueStep implements dialogueStep {
    /**
     *
     */
    constructor(beforeMessage: string, succeedMessage?: string, errorMessage?: string, callback?: Function, httpCallback?: Function, editMessage?: Function) {
        this.callback = callback
        this.httpCallback = httpCallback
        this.beforeMessage = beforeMessage
        this.succeedMessage = succeedMessage
        this.errorMessage = errorMessage
        this.editMessage = editMessage
    }
}

export interface dialogueStep {
    callback?: Function
    httpCallback?: Function
    editMessage?: Function
    beforeMessage: string
    succeedMessage?: string
    errorMessage?: string
}