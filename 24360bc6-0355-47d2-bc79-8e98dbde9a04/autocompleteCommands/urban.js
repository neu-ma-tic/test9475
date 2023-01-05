import fetch from "node-fetch"
export default async function (interaction, { options}) {
  var results = (await(await fetch(`https://api.urbandictionary.com/v0/autocomplete-extra?term=${options.term}`)).json()).results
  var choices = []
  for (var i = 0; i < results.length; i++) {
    choices.push({ name: results[i].term, value: results[i].term })
    if(i == 25) break
  }
  interaction.respond(8, {choices})
}