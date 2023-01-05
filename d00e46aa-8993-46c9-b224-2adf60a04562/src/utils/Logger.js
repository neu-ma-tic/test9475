const chalk = require("chalk");
const moment = require("moment");

module.exports = class Logger {
    static log(content) {
        const timestamp = chalk.greenBright(`[${moment().format('DD-MM-YYYY kk:mm:ss')}]`);
        console.log(chalk.whiteBright(`${timestamp} (${chalk.blueBright("INFO")}) ${content} `));
    }

    static warn(content) {
        const timestamp = chalk.greenBright(`[${moment().format('DD-MM-YYYY kk:mm:ss')}]`);
        console.log(chalk.whiteBright(`${timestamp} (${chalk.yellowBright("WARN")}) ${content}`));
    }

    static error(content) {
        const timestamp = chalk.greenBright(`[${moment().format('DD-MM-YYYY kk:mm:ss')}]`);
        console.log(chalk.whiteBright(`${timestamp} (${chalk.redBright("WARN")}) ${content}`));
    }
}