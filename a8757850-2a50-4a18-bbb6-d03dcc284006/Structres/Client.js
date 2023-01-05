require('dotenv').config();

const Discord = require("discord.js");

const Command = require("./Command.js");

const Event = require("./Event.js");

const config = require("../Data/config.json");

const intents = new Discord.Intents(32767);

const fs = require("fs");

class Client extends Discord.Client {
  constructor() {
    super({ intents, allowedMentions: { repliedUser: false } });//commands reply wont ping you

    /**
     * @type  {Discord.Collection<string, Command>}
     */
    this.commands = new Discord.Collection();
    this.aliases = new Discord.Collection();
    this.prefix = config.prefix;
  }

  start(mySecret) {

    fs.readdirSync("./Commands")
      .filter(file => file.endsWith(".js"))
      .forEach(file => {
        /**
         * @type {Command}
         */

        const command = require(`../Commands/${file}`);
        console.log(`Command ${command.name} loaded`);
        this.commands.set(command.name, command);


        if (command.aliases) {
          command.aliases.forEach(aliases => {
            this.aliases.set(aliases, command)
          })
        }
      });

    fs.readdirSync("./Events")
      .filter(file => file.endsWith(".js"))
      .forEach(file => {
        /**
         * @type {Event}
         */
        const event = require(`../Events/${file}`);
        console.log(`Event ${event.event} loaded`);
        this.on(event.event, event.run.bind(null, this));
      });

    this.login(mySecret);


  }
}

module.exports = Client;