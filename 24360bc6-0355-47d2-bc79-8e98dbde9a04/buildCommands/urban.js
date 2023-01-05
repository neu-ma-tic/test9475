import APIManager from "../lib/APIManager.js"
var api = new APIManager(process.env.TOKEN)
api.sendRequest({
  method: "POST",
  endpoint: "/applications/754203081838821376/commands",
  payload: JSON.stringify({
    name: "urban",
    description: "Searches Urban Dictionary",
    options: [
      {
        type: 3,
        name: "term",
        description: "The term to search",
        required: true,
        autocomplete: true
      }
    ]
  })
})