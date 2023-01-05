
import utils from "node:util"
export default async function (interaction, { options }, context) {
  interaction.respond(4, {
    content: "" + await eval(options.statement)
  })
}