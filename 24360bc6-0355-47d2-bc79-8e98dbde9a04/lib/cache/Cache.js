export default class Cache {
  constructor() {
    /**
     * The currently cached items
     * @type {Map<string, object>}
     */
    this.items = new Map()
  }
  /**
   * Fetches an item not on the list
   * @param {string} id
   * @abstract
   */
  async fetchItem(id) {
    throw new Error("The specified object does not exist.")
  }
  async get(id) {
    if (this.items.has(id)) return this.items.get(id)
    var item = await this.fetchItem(id)
    if(item == undefined) return undefined
    this.items.set(id, item)
    return this.items.get(id)
  }
  /**
   * Adds a object
   * @abstract
   * @param {object} obj
   */
  add(obj) {
    throw new Error("This is read-only")
  }
  /**
   * Removes an object
   * @abstract
   * @param {string} id
   */
  delete(id) {
    throw new Error("This is read-only")
  }
  /**
   * Modifies an object
   * @abstract
   * @param {string} id
   */
  set(id, obj) {
    throw new Error("This is read-only")
  }
}