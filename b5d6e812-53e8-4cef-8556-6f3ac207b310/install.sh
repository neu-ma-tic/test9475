#!/usr/bin/bash

pkg update
pkg upgrade
pkg install nodejs
npm i discord.js
npm i discord-reply
npm i node-fetch
node index.js

echo "[*] All depedencies have been installed, please run the command \"node index\" to immediately start the script" 
