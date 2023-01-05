import APIManager from "../lib/APIManager.js"
var api = new APIManager(process.env.TOKEN)
api.sendRequest({
  method: "POST",
  endpoint: "/applications/754203081838821376/commands",
  payload: JSON.stringify({
    name: "reactionrole",
    description: "Manages Reaction Roles",
    permissions: 1 << 28,
    options: [
      {
        type: 1,
        name: "set",
        description: "Adds or modifies a existing reaction role",
        options: [
          {
            type: 3,
            name: "message",
            required: true,
            description: "The link to the message."
          },
          {
            type: 8,
            name: "role",
            required: true,
            description: "The Role to give the reacting user to"
          },
          {
            type: 3,
            name: "emoji",
            required: true,
            description: "The emoji to trigger the role give."
          }
        ]
      },
      {
        type: 1,
        name: "remove",
        description: "Removes a reaction role",
        options: [
          {
            type: 3,
            name: "message",
            required: true,
            description: "The link to the message."
          },
          {
            type: 3,
            name: "emoji",
            required: true,
            description: "The emoji to trigger the role give."
          }
        ]
      }
    ]
  })
})