import APIManager from "../lib/APIManager.js"
var api = new APIManager(process.env.TOKEN)
api.sendRequest({
  method: "POST",
  endpoint: "/applications/754203081838821376/commands",
  payload: JSON.stringify({
    name: "form",
    description: "Makes a form",
    options: [
      {
        type: 3,
        name: "title",
        description: "The title of the form",
        required: true
      },
      {
        type: 5,
        name: "allow_multiple_responses",
        description: "Whether to allow multiple responses. False by default",
        required: false
      }
    ]
  })
})