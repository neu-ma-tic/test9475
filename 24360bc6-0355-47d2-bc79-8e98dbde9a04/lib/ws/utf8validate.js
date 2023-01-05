const TYPES = [128, 64, 32, 16, 8]
const FIRST_CODE_POINTS = [0x80, 0x800, 0x10000]
function validateUTF8(buffer) {
	if (!Buffer.isBuffer(buffer)) throw new TypeError("buffer must be a buffer")
	for (var i = 0; i < buffer.length; i++) {
		var num = buffer[i]
		var type = getType(num)
		if (type == 0) continue
		if (type > 1 && i + type <= buffer.length) {
			var unicodeCodePoint = num & (0xFF >>> (type + 1))
			var x = type
			while (x-- > 1) {
				if (getType(buffer[++i]) != 1) return false
				unicodeCodePoint = (buffer[i] & 63) + (unicodeCodePoint << 6)
			}
			if (unicodeCodePoint >= 0xD800 && unicodeCodePoint <= 0xDFFF) return false // reserved Unicode points
			if (unicodeCodePoint < FIRST_CODE_POINTS[type - 2]) return false // overlong representations bad
			if (unicodeCodePoint > 0x10ffff) return false // Codepoints above U+10FFF are invalid
		} else {
			return false
		}
	}
	return true
}
function getType(num) {
	for (var i = 0; i < TYPES.length; i++) {
		if ((TYPES[i] & num) == 0) return i
	}
	return -1
}
export default validateUTF8