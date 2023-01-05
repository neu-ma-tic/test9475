export default function (interaction, { api, con, res = undefined }) {
  interaction.respond = async (type, data = {}, additionalOptions = {}) => {
    if (res) {
      return res.status(200).json({type, data})
    } 
    await api.sendRequest({
      method: "POST",
      endpoint: `/interactions/${interaction.id}/${interaction.token}/callback`,
      payload: JSON.stringify({ type, data }),
      ...additionalOptions
    })
  }
  interaction.getOriginal = async () => {
    var res = await api.sendRequest({
      method: "GET",
      endpoint: `/webhooks/${con.applicationID}/${interaction.token}/messages/@original`
    })
    return await res.json()
  }
  interaction.editOriginal = async (message, additionalOptions = {}) => {
    var res = await api.sendRequest({
      method: "PATCH",
      endpoint: `/webhooks/${con.applicationID}/${interaction.token}/messages/@original`,
      payload: JSON.stringify(message),
      ...additionalOptions
    })
    return await res.json()
  }
  interaction.deleteOriginal = async () => {
    await api.sendRequest({
      method: "DELETE",
      endpoint: `/webhooks/${con.applicationID}/${interaction.token}/messages/@original`
    })
  }
  interaction.createFollowup = async (message, additionalOptions = {}) => {
    var res = await api.sendRequest({
      method: "POST",
      endpoint: `/webhooks/${con.applicationID}/${interaction.token}`,
      payload: JSON.stringify(message),
      ...additionalOptions
    })
    return res.json()
  }
  interaction.getFollowup = async (id) => {
    var res = await api.sendRequest({
      method: "GET",
      endpoint: `/webhooks/${con.applicationID}/${interaction.token}/messages/${id}`
    })
    return await res.json()
  }
  interaction.deleteFollowup = async (id) => {
    await api.sendRequest({
      method: "DELETE",
      endpoint: `/webhooks/${con.applicationID}/${interaction.token}/messages/${id}`
    })
  }
  return interaction
}