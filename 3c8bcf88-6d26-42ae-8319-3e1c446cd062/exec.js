module.exports.run = async (bot, message, args) => {
    var shell = require('shelljs');
    var v = require('./index.js')

    shell.exec(args.join(' '), function(code, stdout, stderr) {
        if (stdout != null && stdout !== undefined && stdout !== "" && stdout !== " ") {
            message.channel.send("" + stdout.slice(0, 1993) + "");
            for (let i = 1; i < stdout.length / 1993; i++) {
                let first = i * 1993;
                let second = (i + 1) * 1993;
                message.channel.send("" + stdout.slice(first, second) + "");
            }
        }

        if (stderr != null && stderr !== undefined && stderr !== "" && stderr !== " ") {
            message.channel.send("" + stderr.slice(0, 1993) + "");
            for (let i = 1; i < stderr.length / 1993; i++) {
                let first = i * 1993;
                let second = (i + 1) * 1993;
                message.channel.send("" + stderr.slice(first, second) + "");
            }
        }
    })

}

module.exports.config = {
  command: "execute",
  alias: "exec"
}