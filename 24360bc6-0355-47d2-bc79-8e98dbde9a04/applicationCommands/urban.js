import fetch from "node-fetch"
import EmbedBuilder from "../lib/builders/EmbedBuilder.js"
export default async function (interaction, { options }, { addComponentListener }) {
	await interaction.respond(5)
	var results = (await (await fetch(`https://api.urbandictionary.com/v0/define?term=${encodeURIComponent(options.term)}`)).json()).list
	if (results.length == 0) interaction.editOriginal({ content: "No definitions are found" })
	var index = 0
	var page = 1
	var pageLimit = Infinity
	var msg_id = ""
	var disableComponents = false
	function updateMsg() {
		var embeds = []
		var words = splitWords(results[index].definition, 4096)
		embeds.push((new EmbedBuilder()).setTitle(results[index].word).setURL(results[index].permalink).setDescription(words[0]).embed)
		words.splice(0, 1)
		words.forEach(a => embeds.push({ description: a }))
		return {
			embeds,
			components: [{
				type: 1,
				components: [
					{
						type: 2,
						style: 1,
						label: "Previous Definition",
						custom_id: "previous",
						emoji: { id: null, animated: false, name: "\u23ea" },
						disabled: index == 0 || disableComponents
					},
					{
						type: 2,
						style: 1,
						label: "Next Definition",
						custom_id: "next",
						emoji: { id: null, animated: false, name: "\u23e9" },
						disabled: (index == results.length - 1 && page >= pageLimit) || disableComponents
					}
				]
			}]
		}
	}
	msg_id = (await interaction.editOriginal(updateMsg())).id
	addComponentListener(msg_id, "previous", i => {
		index--
		if(index < 0) return index = 0
		i.respond(7, updateMsg())
	}, {
		onRemove: () => { disableComponents = true; interaction.editOriginal(updateMsg()) },
		linkTimers: [[msg_id, "next"]]
	})
	addComponentListener(msg_id, "next", async i => {
		index++
		if (index >= results.length) {
			await i.respond(6)
			page++
			var newDefs = (await(await fetch(`https://api.urbandictionary.com/v0/define?term=${encodeURIComponent(options.term)}&page=${page}`)).json()).list
			results = results.concat(newDefs)
			if (newDefs.length == 0) {
				pageLimit = --page
				index--
			}
			return interaction.editOriginal(updateMsg())
		}
		i.respond(7, updateMsg())
	}, {
		linkTimers: [[msg_id,"previous"]]
	})
}
function splitWords(str, splitLength) {
	var words = str.split(" ")
	var length = 0
	var returnValue = []
	var chunk = []
	words.forEach(s => {
		if (length + s.length + chunk.length > splitLength) {
			returnValue.push(chunk.join(" "))
			chunk = []
			length = 0
		}
		chunk.push(s)
		length += s.length
	})
	returnValue.push(chunk.join(" "))
	return returnValue
}
