import { stringify } from "csv-stringify"
import FormData from "../lib/utils/FormData.js"
export default async function (interaction, options, { api, con, addComponentListener, addModalListener }) {
  console.log(options)
  var timesPressed = 0
  await interaction.respond(4, {
    content: "You are making a form",
    components: [
      {
        type: 1,
        components: [
          {
            type: 2,
            style: 1,
            label: "Add Paragraph Text Box",
            custom_id: "add_option_paragraph"
          },
          {
            type: 2,
            style: 1,
            label: "Add Short Response Text Box",
            custom_id: "add_option_text"
          },
          {
            type: 2,
            style: 1,
            label: "Preview Form",
            custom_id: "preview"
          },
          {
            type: 2,
            style: 1,
            label: "Publish form",
            custom_id: "publish"
          }
        ]
      }

    ]
  })
  var modal_id = "modal_" + Date.now()
  var modal = {
    title: options.options.title,
    custom_id: modal_id,
    components: []
  }
  var message = await interaction.getOriginal()
  var modalOptions = {}
  var spreadsheet = []
  var embed = {fields: []}
  addComponentListener(message.id, "add_option_paragraph", async component => {
    var custom_id = "add_option_" + Date.now()
    if (modal.components.length == 5) return component.respond(4, {flags: 64, content: "Form inputs are limited to 5 inputs"})
    await component.respond(9, {
      title: "Add Option",
      custom_id,
      components: [
        {
          type: 1,
          components: [{
            type: 4,
            custom_id: "label",
            style: 1,
            label: "Label",
            required: true,
            max_length: 45
          }]
        },
        {
          type: 1,
          components: [{
            type: 4,
            custom_id: "placeholder",
            style: 1,
            label: "Placeholder",
            required: false,
            max_length: 100
          }]
        }
      ]
    })
    addModalListener(custom_id, (i, values) => {
      var modalId = "form_option_" + Date.now()
      var component = { label: values.label, custom_id: modalId, style: 2, type: 4 }
      if (values.placeholder !== "") component.placeholder = values.placeholder
      modalOptions[modalId] = values.label
      modal.components.push({
        type: 1,
        components: [component]
      })
      embed.fields.push({name: values.label, value: `Type: Paragraph\nPlaceholder: ${values.placeholder === ""? "N/A" : values.placeholder}`})
      i.respond(7, {
        embeds: [embed]
      })
    })
  })
  addComponentListener(message.id, "add_option_text", async component => {
    var custom_id = "add_option_" + Date.now()
    if (modal.components.length == 5) return component.respond(4, { flags: 64, content: "Form inputs are limited to 5 inputs" })
    await component.respond(9, {
      title: "Add Option",
      custom_id,
      components: [
        {
          type: 1,
          components: [{
            type: 4,
            custom_id: "label",
            style: 1,
            label: "Label",
            required: true,
            max_length: 45
          }]
        },
        {
          type: 1,
          components: [{
            type: 4,
            custom_id: "placeholder",
            style: 1,
            label: "Placeholder",
            required: false,
            max_length: 100
          }]
        }
      ]
    })
    addModalListener(custom_id, (i, values) => {
      var modalId = "form_option_" + Date.now()
      var component = { label: values.label, custom_id: "form_option_"+Date.now(), style: 1, type: 4 }
      if (values.placeholder !== "") component.placeholder = values.placeholder
      modalOptions[modalId] = values.label
      modal.components.push({
        type: 1,
        components: [component]
      })
      embed.fields.push({ name: values.label, value: `Type: Short Response\nPlaceholder: ${values.placeholder === "" ? "N/A" : values.placeholder}` })
      i.respond(7, {
        embeds: [embed]
      })
    })
  })
  addComponentListener(message.id, "preview", (i) => {
    if (modal.components.length == 0) return i.respond(4, { flags: 64, content: "Forms must have atlest one text box" })
    i.respond(9, modal)
  })
  addComponentListener(message.id, "publish", async (i) => {
    if (modal.components.length == 0) return i.respond(4, { flags: 64, content: "Forms must have atlest one text box" })
    if ((parseInt(i.app_permissions) & 3072) == 0) return i.respond(4, { flags: 64, content: "I do not have `View Channel` and `Send Message` permissions" })
    var msg = await (await api.sendRequest({
      method: "POST",
      endpoint: `/channels/${i.channel_id}/messages`,
      payload: JSON.stringify({
        components: [{
          type: 1,
          components: [
            {
              type: 2,
              style: 1,
              label: "Fill Form",
              custom_id: "fill_form"
            },
            {
              type: 2,
              style: 1,
              label: "Export CSV",
              custom_id: "export_csv"
            }
          ]
        }]
      })
    })).json()
    interaction.deleteOriginal()
    addComponentListener(msg.id, "export_csv", async a => {
      await a.respond(5, { flags: 64 })
      var formParams = new FormData()
      stringify(spreadsheet, (err, data) => {
        if (err) throw err
        formParams.append("files[0]", data, "spreadsheet.csv")
        a.editOriginal({}, {
          additionalHeaders: {
            "Content-Type": `multipart/form-data; boundary=${formParams.boundary}`
          },
          payload: formParams.toBuffer()
        })
      })
    })
    addComponentListener(msg.id, "fill_form", (a) => {
      a.respond(9, modal)
    })
    var headers = {}
    for (var value of Object.values(modalOptions)) {
      headers[value] = value
    }
    headers["User"] = "User"
    spreadsheet.push(headers)
    addModalListener(modal_id, (a, values) => {
      a.respond(4, { content: "Form submitted", flags: 64 })
      var object = {}
      for (var [key, value] of Object.entries(values)) {
        object[modalOptions[key]] = value
      }
      object["User"] = a.member.user.username + "#" + a.member.user.discriminator
      spreadsheet.push(object)
    })
    i.respond(4, {flags: 64, content: "Done!"})
  })
}