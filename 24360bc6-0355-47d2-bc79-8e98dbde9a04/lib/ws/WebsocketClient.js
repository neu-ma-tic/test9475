import validateUTF8 from "./utf8validate.js"
import EventEmitter from "node:events"
import { URL } from "node:url"
import { request } from "node:http"
import { request as requestSecure } from "node:https"
import { randomBytes, createHash } from "node:crypto"
const RESERVED_OP_CODES = [3, 4, 5, 6, 7, 11, 12, 13, 14, 15]
const CONTROL_OP_CODES = [8, 9, 10]
const RESERVED_CLOSE_CODES = [1004, 1005, 1006, 1012, 1013, 1014]

class WebSocket extends EventEmitter {
	_con = null
	_packetBuffer = Buffer.alloc(0)
	_frameLoopFinished = true
	_expectBufferQueue = []
	_fragmented = true
	_opcode = 0
	_payload = Buffer.alloc(0)
	_code = null
	_reason = null

	static CONNECTING = 0
	static OPEN = 1
	static CLOSING = 2
	static CLOSED = 3

	closeTimeout = 2000

	url = ""
	protocol = ""
	extensions = ""
	readyState = 0
	/**
	 * 
	 * @param {string} url The URL
	 * @param {Array<string>|string} subprotocols
	 * @throws {SyntaxError} When the url cannot be parsed, url has a sheme other than `ws` or `wss`, url has a fragment
	 */
	constructor(url, protocols = []) {
		super()
		var protos = []
		try {
			var URI = new URL(url)
		} catch (e) {
			throw new DOMException(`Failed to construct 'WebSocket': The URL '${"" + url}' is invalid.`, "SyntaxError")
		}
		if (URI.hash !== "") throw new DOMException(`Failed to construct 'WebSocket': The URL contains a fragment identifier ('${URI.hash.substring(1)}'). Fragment identifiers are not allowed in WebSocket URLs.`, "SyntaxError")
		if (URI.protocol !== "ws:" && URI.protocol !== "wss:") throw new DOMException(`Failed to construct 'WebSocket': The URL scheme must be 'ws' or 'wss'. '${URI.protocol.substring(0, URI.protocol.length - 1)} is not allowed`, "SyntaxError")
		protos.forEach((v, i) => {
			if (protos.indexOf(v) !== i) throw new DOMException(`Failed to construct 'WebSocket': The subprotocol '${v}' is duplicated.`, "SyntaxError")
			if (protos.includes(":") || protos.includes(",") || protos.includes(";")) throw new DOMException(`Failed to construct 'WebSocket': The subprotocol '${v}' is invalid.`, "SyntaxError")
			for (var i = 0; i < v.length; i++) {
				if (v.charCodeAt(i) < 0x21 || v.charCodeAt(i) > 0x7E) throw new DOMException(`Failed to construct 'WebSocket': The subprotocol '${v}' is invalid.`, "SyntaxError")
			}
		})
		var con;
		var wsKey = randomBytes(16).toString("base64")
		var headers = {
			"upgrade": "websocket",
			"connection": "upgrade",
			"sec-websocket-key": wsKey,
			"sec-websocket-version": 13,
			"host": URI.host,
			"user-agent": "node"
		}
		this.url = url
		if (protos.length !== 0) headers["sec-websocket-protocol"] = protos.join(", ")
		if (URI.protocol == "wss:") {
			con = requestSecure({
				host: URI.hostname,
				port: URI.port,
				path: URI.pathname + URI.search,
				method: "GET",
				headers,
			})
			con.end()
		} else {
			con = request({
				host: URI.hostname,
				port: URI.port,
				path: URI.pathname + URI.search,
				method: "GET",
				headers,
			})
			con.end()
		}
		con.on("upgrade", (res, connection, head) => {
			console.log("handlingUpgrade")
			this._con = connection
			var accept = res.headers["sec-websocket-accept"]
			var hash = createHash("sha1")
			hash.update(wsKey + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11")
			if (hash.digest("base64") !== accept || res.headers["upgrade"].toLowerCase() !== "websocket" || res.headers["connection"].toLowerCase() !== "upgrade") {
				console.log("protocol err")
				connection.end()
			}
			console.log("checked response")

			this.readyState = 1
			this.emit("open")
			this._packetBuffer = Buffer.concat([this._packetBuffer, head])
			this._handleExpectBuffer()
			if (this._frameLoopFinished) this._frameLoop()
			this._con.on("data", async (buf) => {
				this._packetBuffer = Buffer.concat([this._packetBuffer, buf])
				this._handleExpectBuffer()
				if (this._frameLoopFinished) this._frameLoop()
			})

			this._con.on("close", () => {
				if (this.readyState !== 2)return  this.emit("close", { code: 1006, reason: "", wasClean: false })
				this.readyState = 3
				this.emit("close", {code: this._code, reason: this._reason, wasClean: true})
			})
			console.log("open")
		})
	}
	/**
	 * Sends data to the Websocket
	 * @param {string|Buffer} message
	 */
	send(message) {
		if (this.readyState !== 1) throw new DOMException("WebSocket is not in an OPEN state", "InvalidStateError")
		if (!Buffer.isBuffer(message) && typeof message !== "string") throw new TypeError("message must be a buffer or a string. Recieved " + message)
		if (typeof message == "string") return this._send({ op: 1, payload: Buffer.from(message, "utf-8") })
		this._send({opcode: 2, payload: message})
	}

	close(code = null, reason = "") {
		if (code <= 999 || RESERVED_CLOSE_CODES.includes(code) || (code >= 1015 && code <= 2999)) throw new DOMException("The close code is reserved", "InvalidAccessError")
		if(Buffer.from(reason).length > 123) throw new DOMException("reason must not be greater than 123 bytes", "SyntaxError")
		if (this.readyState == 2 || this.readyState == 3) return;
		if (this.readyState == 1) return this._close({code, reason})
	}

	/**
	 * @private
	 * @param {number} length
	 * @returns {Promise<Buffer>}
	 */
	async _expectBuffer(length) {
		return new Promise((resolve, reject) => {
			if (length <= this._packetBuffer.length) {
				resolve(this._packetBuffer.subarray(0, length))
				return this._packetBuffer = this._packetBuffer.subarray(length)
			}
			this._expectBufferQueue.push([length, resolve])
		})
	}
	/** @private */
	_handleExpectBuffer() {
		for (var i = 0; i < this._expectBufferQueue.length; i++) {
			var expect = this._expectBufferQueue[i]
			if (expect[0] > this._packetBuffer.length) break
			expect[1](this._packetBuffer.subarray(0, expect[0]))
			this._packetBuffer = this._packetBuffer.subarray(expect[0])
			this._expectBufferQueue.shift()
		}
	}
	/** @private */
	async _frameLoop() {
		this._frameLoopFinished = false
		var message = {
			FIN: null,
			reserved: null,
			opcode: null,
			masked: null,
			maskingKey: null,
			length: null,
			payload: null
		}
		var header2Bytes = await this._expectBuffer(2)
		message.FIN = !!(header2Bytes[0] & 0x80)
		message.reserved = (header2Bytes[0] & 0x70) >> 4
		message.opcode = header2Bytes[0] & 0x0F
		message.masked = !!(header2Bytes[1] & 0x80)
		var length = header2Bytes[1] & 0x7F
		if (length == 126) {
			var bufLength = await this._expectBuffer(2)
			length = bufLength.readUint16BE(0)
		} else if (length == 127) {
			var bufLength = await this._expectBuffer(8)
			length = Number(bufLength.readBigInt64BE(0))
		}
		message.length = length
		var payload = await this._expectBuffer(length)
		if (message.masked) message.maskingKey = await this._expectBuffer(4)
		var unmaskedPayload = Buffer.from(payload)
		if (message.masked) {
			for (var i = 0; i < unmaskedPayload.length; i++) unmaskedPayload[i] = payload[i] ^ message.maskingKey[i%4]
		}
		message.payload = unmaskedPayload
		this._processMessage(message)
		if(this._packetBuffer.length !== 0) return this._frameLoop() 
		this._frameLoopFinished = true
	}
	/**
	 * @private
	 * @param {Object} message
	 * @param {boolean} message.FIN
	 * @param {number} message.reserved
	 * @param {number} message.opcode
	 * @param {boolean} message.masked
	 * @param {Buffer} message.maskingKey
	 * @param {number} message.length
	 * @param {Buffer} message.payload
	 */
	async _processMessage({ FIN, reserved, opcode, masked, maskingKey, length, payload }) {
		if (this.readyState == 3 || (this.readyState == 2 && opcode !== 8)) return;
		if (masked) return this._close({ unclean: true })
		if (RESERVED_OP_CODES.includes(opcode)) return this._close({ unclean: true })
		if (reserved !== 0) return this._close({ unclean: true })
		if (!FIN && CONTROL_OP_CODES.includes(opcode)) return this._close({ unclean: true })
		if (!this._fragmented && opcode !== 0 && !CONTROL_OP_CODES.includes(opcode)) return this._close({ unclean: true })
		if (CONTROL_OP_CODES.includes(opcode) && length > 125) return this._close({ unclean: true })
		if (opcode == 0 && this._fragmented) return this._close({ unclean: true })
		switch (opcode) {
			case 0:
				this._payload = Buffer.concat([this._payload, payload])
				if (FIN) {
					if (this._opcode == 1) {
						if (!validateUTF8(this._payload)) return this._close({ unclean: true })
						this._fragmented = true
						this.emit("message", this._payload.toString("utf-8"))
						return this._payload = Buffer.alloc(0)
					}
					this.emit("message", this._payload)
					return this._payload = Buffer.alloc(0)
				}
				break;
			case 1:
				this._opcode = 1
				if (FIN) {
					if (!validateUTF8(payload)) return this._close({ unclean: true })
					return this.emit("message", payload.toString("utf-8"))
				}
				this._payload = Buffer.concat([this._payload, payload])
				this._fragmented = false;
				break;
			case 2:
				this._opcode = 2
				if (FIN) {
					return this.emit("message", payload)
				}
				this._payload = Buffer.concat([this._payload, payload])
				this._fragmented = false;
				break;
			case 8:
				if (this.readyState === 2 || this.readyState === 3) return;
				if (payload.length === 1) return this._close({ code: 1002, reason: "invalid payload length", recieving: true })
				var code = payload.length >= 2 ? payload.readUint16BE(0) : 1000
				var reason = payload.subarray(2)
				if (code <= 999 || RESERVED_CLOSE_CODES.includes(code) || (code >= 1015 && code <= 2999)) return this._close({ code: 1002, reason: "invalid close code", recieving: true })
				if (!validateUTF8(reason)) return this._close({ code: 1007, reason: "invalid close reason", recieving: true})
				this._close({ code, reason: reason.toString("utf-8"), recieving: true })
				break;
			case 9:
				await this._send({ opcode: 10, payload })
				break;
		}
	}
	async _close({ code = null, reason = "", recieving = false, unclean = false }) {
		this.readyState = 2
		this._reason = reason
		this._code = code == null? 1005: code
		if (unclean) {
			this._code = 1006
			return this._con.end()
		}
		if (code == null) {
			await this._send({
				opcode: 8,
				payload: Buffer.alloc(0)
			})
		} else {
			var message = Buffer.alloc(2)
			message.writeUint16BE(code)
			await this._send({
				opcode: 8,
				payload: Buffer.concat([message, Buffer.from(reason, "utf-8")])
			})
		}
		if (recieving) {
			return this._con.end()
		}
		setTimeout(() => {
			if (this.readyState == 3) return
			this._code = 1006
			this._con.end()
		}, this.closeTimeout)
	}
	_send({ FIN = true, reserved = 0, opcode = 1, payload }) {
		return new Promise((resolve) => {
			if ((this.readyState == 2 && opcode !== 8) || this.readyState == 3) return resolve()
			var header;
			if (payload.length <= 125) {
				header = Buffer.alloc(2)
				header[1] = payload.length | 128
			} else if (payload.length <= 0xffff) {
				header = Buffer.alloc(4)
				header[1] = 254
				header.writeUint16BE(payload.length, 2)
			} else {
				header = Buffer.alloc(10)
				header[1] = 255
				header.writeBigInt64BE(BigInt(payload.length), 2)
			}
			header[0] = (FIN << 7) | (reserved << 4) | opcode
			var maskingKey = randomBytes(4)
			var maskedPayload = Buffer.from(payload)
			for (var i = 0; i < maskedPayload.length; i++) maskedPayload[i] = payload[i] ^ maskingKey[i % 4]
			this._con.write(Buffer.concat([header, maskingKey, maskedPayload]), resolve)
		})
	}
}
export default WebSocket