const fs = require("fs");

module.exports = {
  name: "clips",
  description: "لیست کردن تمانی کلیپ ها",
  execute(message) {
    fs.readdir("./sounds", function(err, files) {
      if (err) return console.log("نا موفق در خواندن فایل: " + err);

      let clips = [];

      files.forEach(function(file) {
        clips.push(file.substring(0, file.length - 4));
      });

      message.reply(`${clips.join(" ")}`).catch(console.error);
    });
  }
};
