import mime from "mime"
export default class FormData {
  constructor(boundary) {
    this.boundary = boundary || randomString(64)
    this.data = Buffer.alloc(0)
  }
  /**
   * Adds a parameter to the
   * @param {any} name The name of the parameter
   * @param {any} data The content of the parameter
   * @param {any} filename The content to send to
   * @returns {FormData}
   */
  append(name, data, filename) {
    if (typeof name !== "string") throw new TypeError("name must be a string. Recieved type " + typeof name)
    if (typeof data !== "string" && !Buffer.isBuffer(data)) throw new Error("data must be a buffer or a string. Recieved type " + typeof data)
    if (typeof filename == "string" && !/^[^\\/:\*\?"<>\|]+$/.test(filename)) throw new Error("filename is not a valid file")
    this.data = Buffer.concat([this.data,
      Buffer.from(`--${this.boundary}\r\n`),
      Buffer.from(`Content-Disposition: form-data; name="${name}"${typeof filename == "string" ? `; filename="${filename}"` : ""}\r\n`),
      typeof filename == "string" && mime.getType(filename) !== null ? Buffer.from(`Content-Type: ${mime.getType(filename)}\r\n`) : Buffer.alloc(0),
      Buffer.from("\r\n"),
      Buffer.from(data),
      Buffer.from("\r\n")
    ])
    return this
  }
  toBuffer() {
    return Buffer.concat([this.data, Buffer.from(`--${this.boundary}--`)])
  }
}
function randomString(length) {
  var chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz'.split('');

  if (!length) {
    length = Math.floor(Math.random() * chars.length);
  }

  var str = '';
  for (var i = 0; i < length; i++) {
    str += chars[Math.floor(Math.random() * chars.length)];
  }
  return str;
}