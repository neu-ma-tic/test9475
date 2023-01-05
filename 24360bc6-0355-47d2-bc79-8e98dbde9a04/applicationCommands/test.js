export default async function (interaction, options, { api, con, addComponentListener }) {
  var timesPressed = 0
  await interaction.respond(4,{
    content: "Hello",
    components: [
      {
        type: 1,
        components: [
          {
            type: 2,
            style: 1,
            label: "Press",
            custom_id: "test"
          }
        ]
      }
    ]
  })
  var message = await interaction.getOriginal()
  addComponentListener(message.id, "test", component => {
    component.respond(7, { content: "Hello\nThe button bellow has been pressed " + (++timesPressed) + "times."})
  })
}