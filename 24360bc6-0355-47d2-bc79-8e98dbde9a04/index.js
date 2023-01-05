import GatewayConnection from "./lib/GatewayConnection.js"
import APIManager from "./lib/APIManager.js"
import Interaction from "./lib/types/Interaction.js"

import { createWriteStream, readdirSync } from "node:fs"
import { join, dirname } from "node:path"
import { fileURLToPath } from "node:url"

import express from "express"
import nacl from "tweetnacl"
import Database from "@replit/database"
import GuildManager from "./lib/cache/GuildManager.js"

const logFiles = false
const useEndpointURL = true

const publicKey = process.env.PUBKEY
const token = process.env.TOKEN
const api = new APIManager(token)
const con = new GatewayConnection(token, {
  intents: [GatewayConnection.INTENT_FLAGS.GUILDS, GatewayConnection.INTENT_FLAGS.GUILD_MESSAGE_REACTIONS],
  showSensitiveData: false
})
const log = logFiles ? createWriteStream(join(dirname(fileURLToPath(import.meta.url)), `./logs/${Date.now()}.log`)) : { write: console.log }
const guilds = new GuildManager(con, api)
const database = new Database("https://discordbotdb.salace2.repl.co/")
var port = process.env.PORT || 8080
var componentListeners = {}
var modalListeners = []
if (useEndpointURL) {
  const app = express()
  app.use(express.json({
    verify(req, res, buf) {
      const signature = req.get('X-Signature-Ed25519');
      const timestamp = req.get('X-Signature-Timestamp');
      var verified = nacl.sign.detached.verify(
        Buffer.from(Buffer.concat([Buffer.from(timestamp), buf])),
        Buffer.from(signature, "hex"),
        Buffer.from(publicKey, "hex")
      )
      if (!verified) {
        res.status(401).end("invalid req signature")
        throw new Error("bad request sig")
      }
    }
  }))
  app.post("/", (req, res) => {
    // Verify the contents
    handleInteraction(req.body, res)
  })
  app.get("/", (req, res) => res.status(200).end("This is discord bot interaction endpoint."))
  app.listen(port, () => console.log("Listenening on " + port))
} else {
  con.on("INTERACTION_CREATE", handleInteraction)
}
con.on("READY", d => {
  con.setPresence({
    status: "online",
    activities: [{
      type: 0,
      name: process.env.PRESENCE || `with ${d.guilds.length} servers`
    }],
    afk: false,
    since: null
  })

  readdirSync(join(dirname(fileURLToPath(import.meta.url)), `./startup`)).forEach(async f => (await import(`./startup/${f}`)).default({ api, con, guilds, database }))
})
async function handleInteraction(data, res) {
  var interaction = Interaction(data, { api, con, res })
  switch (interaction.type) {
    case 1:
      interaction.respond(1)
      break
    case 2:
      var options = {};
      console.log(interaction.data)
      options = parseCommandOptions(interaction.data.options == undefined ? [] : interaction.data.options, interaction.data.resolved);
      var cmd = await import(`./applicationCommands/${interaction.data.name}.js`)
      try {
        cmd.default(interaction, options, { api, con, addComponentListener, addModalListener, guilds, database })
      } catch (e) {
        log.write("[ERROR]   " + e.toString() + "\n")
      }
      break;
    case 3:
      if (componentListeners[interaction.message.id] && componentListeners[interaction.message.id][interaction.data.custom_id]) {
        var component = componentListeners[interaction.message.id][interaction.data.custom_id]
        component.listener(interaction)
        if (component.ttl !== Infinity) {
          clearTimeout(component.ttlTimeout)
          component.linkTimers.forEach(a => {
            var addComponent = componentListeners[a[0]][a[1]]
            clearTimeout(addComponent.ttlTimeout)
            addComponent.ttlTimeout = component.ttlTimeout = setTimeout(() => {
              addComponent.onRemove()
              delete componentListeners[a[0]][a[1]]
            }, addComponent.ttl).unref()
          })
          component.ttlTimeout = setTimeout(() => {
            component.onRemove()
            delete componentListeners[interaction.message.id][interaction.data.custom_id]
          }, component.ttl).unref()
        }
        componentListeners[interaction.message.id][interaction.data.custom_id] = component
      }
      break;
    case 4:
      var options = {}
      options = parseCommandOptions(interaction.data.options == undefined ? [] : interaction.data.options, interaction.data.resolved);
      var cmd = await import(`./autocompleteCommands/${interaction.data.name}.js`)
      cmd.default(interaction, options, { api, con, addComponentListener, addModalListener, database })
      break;
    case 5:
      modalListeners.forEach(h => {
        if (h.component_id == interaction.data.custom_id) {
          return h.listener(interaction, parseModalValues(interaction.data.components))
        }
      })
      break;
  }
}
function addComponentListener(message_id, component_id, listener, { ttl = 60000, onRemove = () => { }, linkTimers = [] } = {}) {
  var ttlTimeout = null;
  if (ttl !== Infinity) {
    ttlTimeout = setTimeout(() => {
      onRemove()
      delete componentListeners[message_id][component_id]
    }, ttl).unref()
  }
  componentListeners[message_id] = componentListeners[message_id] || {}
  componentListeners[message_id][component_id] = { listener, ttlTimeout, ttl, onRemove, linkTimers }
}
function addModalListener(component_id, listener) {
  modalListeners.push({ component_id, listener })
}
function parseModalValues(components) {
  var options = {}
  components.forEach(r => {
    switch (r.type) {
      case 1:
        options = { ...options, ...(parseModalValues(r.components)) }
        break;
      case 4:
        options[r.custom_id] = r.value
        break;
    }
  })
  return options
}
function parseCommandOptions(options, resolved) {
  var subCmdInvoked = ""
  var subCmdGroupInvoked = ""
  var options1 = {}
  options.forEach(option => {
    switch (option.type) {
      case 1:
        subCmdInvoked = option.name
        options1 = parseCommandOptions(option.options, resolved).options
        break
      case 2:
        subCmdGroupInvoked = option.name
        var result = parseCommandOptions(option.options, resolved)
        subCmdInvoked = result.subCmdInvoked
        options[1] = result.options
      case 3:
        options1[option.name] = option.value
        break
      case 4:
        options1[option.name] = option.value
        break
      case 5:
        options1[option.name] = option.value
        break
      case 6:
        options1[option.name] = resolved.users[option.value]
        break
      case 7:
        options1[option.name] = resolved.channels[option.value]
        break
      case 8:
        options1[option.name] = resolved.roles[option.value]
        break
      case 9:
        options1[option.name] = resolved.users[option.value] ? resolved.users[option.value] : resolved.roles[option.value]
        break
      case 10:
        options1[option.name] = option.value
        break
      case 11:
        options1[option.name] = option.value
        break
    }
  })
  return { subCmdInvoked, subCmdGroupInvoked, options: options1 }
}
con.on("debug", e => log.write("[GATEWAY] " + e + "\n"))
api.on("debug", e => log.write("[API]     " + e + "\n"))
con.connect()