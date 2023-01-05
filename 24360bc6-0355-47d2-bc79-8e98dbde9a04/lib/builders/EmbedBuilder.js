export default class EmbedBuilder {
  constructor() {
    this.embed = {

    }
  }
  /**
   * Sets the title of the embed
   * @param {string} title
   * @returns {EmbedBuilder}
   */
  setTitle(title) {
    if (typeof title !== "string") throw new TypeError("`title` must be a string")
    if (title.length == 0) throw new Error("`title` must be at least one char.")
    this.embed.title = title
    return this
  }
  /**
   * Sets the description of the embed
   * @param {string} description
   * @returns {EmbedBuilder}
   */
  setDescription(description) {
    if (typeof description !== "string") throw new TypeError("`description` must be a string")
    if (description.length == 0) throw new Error("`description` must be at least one char.")
    this.embed.description = description
    return this
  }
  /**
   * 
   * @param {string|URL} url
   * @returns {EmbedBuilder}
   */
  setURL(url) {
    if (typeof url !== "string" && !(url instanceof URL)) throw new TypeError("`imageURL` must be a string or URL")
    if (typeof url == "string" && !["attachment:", "http:", "https:"].includes((new URL(url)).protocol)) throw new TypeError("`imageURL` must be a valid URL")
    if (url instanceof URL && !["attachment:", "http:", "https:"].includes(url.protocol)) throw new TypeError("`imageURL` must be a valid URL")
    this.embed.url = url.toString()
    return this
  }
  /**
   * Sets the timestamp of the embed
   * @param {Date} date
   * @returns {EmbedBuilder}
   */
  setTimestamp(date) {
    if (!(date instanceof Date) || isNaN(date.valueOf)) throw new TypeError("`date` must be a valid date")
    this.embed.timestamp = date.toISOString()
    return this
  }
  /**
   * Sets the color of the embed
   * @param {number} color
   * @returns {EmbedBuilder}
   */
  setColor(color) {
    if (typeof color !== "number" || !isFinite(color) || color > 0xFFFFFF) throw new TypeError("`date` must be a valid 24bit number")
    this.embed.color = color
    return this
  }
  /**
   * Sets the description of the embed
   * @param {string} footer
   * @returns {EmbedBuilder}
   */
  setFooterText(footer) {
    if (typeof footer !== "string") throw new TypeError("`footer` must be a string")
    if (footer.length == 0) throw new Error("`footer` must be at least one char.")
    this.embed.footer = this.embed.footer || {}
    this.embed.footer.text = footer
    return this
  }
  /**
   * Sets the image of the embed
   * @param {string|URL} imageURL
   * @returns {EmbedBuilder}
   */
  setFooterIcon(imageURL) {
    if (typeof imageURL !== "string" && !(imageURL instanceof URL)) throw new TypeError("`imageURL` must be a string or URL")
    if (typeof imageURL == "string" && !["attachment:", "http:", "https:"].includes((new URL(imageURL)).protocol)) throw new TypeError("`imageURL` must be a valid URL")
    if (imageURL instanceof URL && !["attachment:", "http:", "https:"].includes(imageURL.protocol)) throw new TypeError("`imageURL` must be a valid URL")
    this.embed.footer = this.embed.footer || {}
    this.embed.footer.icon_url = imageURL.toString()
    return this
  }
  /**
   * Sets the image of the embed
   * @param {string|URL} imageURL
   * @returns {EmbedBuilder}
   */
  setThumbnail(imageURL) {
    if(typeof imageURL !== "string" && !(imageURL instanceof URL)) throw new TypeError("`imageURL` must be a string or URL")
    if (typeof imageURL == "string" && !["attachment:", "http:", "https:"].includes((new URL(imageURL)).protocol)) throw new TypeError("`imageURL` must be a valid URL")
    if (imageURL instanceof URL && !["attachment:", "http:", "https:"].includes(imageURL.protocol)) throw new TypeError("`imageURL` must be a valid URL")
    this.embed.thumbnail = this.embed.thumbnail || {}
    this.embed.thumbnail.url = imageURL.toString()
    return this
  }
  /**
   * Sets the author name of the embed
   * @param {string} name
   * @returns {EmbedBuilder}
   */
  setAuthorName(name) {
    if (typeof name !== "string") throw new TypeError("`name` must be a string")
    if (name.length == 0) throw new Error("`name` must be at least one char.")
    this.embed.author = this.embed.author || {}
    this.embed.author.name
    return this
  }
  /**
   * Sets the author URL of the embed
   * @param {string|URL} url
   * @returns {EmbedBuilder}
   */
  setAuthorURL(url) {
    if (typeof url !== "string" && !(url instanceof URL)) throw new TypeError("`imageURL` must be a string or URL")
    if (typeof url == "string" && !["http:", "https:"].includes((new URL(url)).protocol)) throw new TypeError("`imageURL` must be a valid URL")
    if (url instanceof URL && !["http:", "https:"].includes(url.protocol)) throw new TypeError("`imageURL` must be a valid URL")
    this.embed.author = this.embed.author || {}
    this.embed.author.url = url
    return this
  }
  /**
   * Sets the author image of the embed
   * @param {string|URL} imageURL
   * @returns {EmbedBuilder}
   */
  setAuthorImage(imageURL) {
    if (typeof imageURL !== "string" && !(imageURL instanceof URL)) throw new TypeError("`imageURL` must be a string or URL")
    if (typeof imageURL == "string" && !["attachment:", "http:", "https:"].includes((new URL(imageURL)).protocol)) throw new TypeError("`imageURL` must be a valid URL")
    if (imageURL instanceof URL && !["attachment:", "http:", "https:"].includes(imageURL.protocol)) throw new TypeError("`imageURL` must be a valid URL")
    this.embed.author = this.embed.thumbnail || {}
    this.embed.author.icon_url = imageURL.toString()
    return this
  }
  /**
   * Adds a field to the embed
   * @param {string} name
   * @param {string} value
   * @param {boolean} [inline=false]
   * @returns {EmbedBuilder}
   */
  addField(name, value, inline = false) {
    this.embed.fields = []
    this.embed.push({ name, value, inline })
    return this
  }
}