import { DiscordenoMessage, Player } from "../../../deps.ts";
import { createCommand } from "../../utils/helpers.ts";
import { sortWordByMinDistance } from "https://deno.land/x/damerau_levenshtein@v0.1.0/mod.ts";
import { bot } from "../../../cache.ts";

createCommand({
  name: "radio",
  aliases: ["r"],
  guildOnly: true,
  arguments: [{ type: "...strings", name: "query", required: true }],
  userServerPermissions: ["SPEAK", "CONNECT"],

  async execute(message: DiscordenoMessage, args) {
    const voiceState = message.guild?.voiceStates.get(message.authorId);

    const data = JSON.parse(
      Deno.readTextFileSync("./src/commands/voice/radios.json"),
    );

    if (!voiceState?.channelId) {
      return message.reply("Join a voice channel you dweeb");
    }

    // if (!args.length) return message.reply('Wrong number of args');

    // console.log(video.url);

    let radio: IRadio | null = null;

    let closestMatch: string = args.query.toUpperCase();

    var radiolink: string;

    var keys = [];
    for (var k in data) keys.push(k);

    closestMatch = sortWordByMinDistance(closestMatch, keys)[0].string;
    radio = data[closestMatch];
    radiolink = radio!.link;

    message.reply(radio!.id);

    // break;
    // }

    if (radio) {
      // Get player from map (Might not exist)
      const player = bot.lavadenoManager.players.get(
        message.guildId.toString(),
      );

      if (player) {
        player.connect(voiceState.channelId.toString(), {
          selfDeaf: true,
        });
        const results = await player.manager.search("bka");
        const { track, info } = results.tracks[0];
        player.play("https://www.youtube.com/watch?v=rixsfO9WkbM");
      } else {
        // player doesn't exist, create one and connect
        const newPlayer = bot.lavadenoManager.create(
          message.guildId.toString(),
        );
        newPlayer.connect(voiceState.channelId.toString(), {
          selfDeaf: true,
        });

        (await newPlayer.play(radio.link)).on(
          "error",
          () => message.reply(":("),
        );
      }

      //     const connection = await voiceState?.channelId.;
      //     connection
      //         .play(radiolink, { seek: 0, volume: 1, bitrate: 'auto' })
      //         .on('finish', () => {
      //             voiceState.leave();
      //         });

      //     await message.reply(`Radio ${closestMatch} is playing`);
      // }
    }
  },
});

const isLink = (link: string) => {
  var pattern = new RegExp(
    "^(https?:\\/\\/)?" + // protocol
      "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
      "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
      "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
      "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
      "(\\#[-a-z\\d_]*)?$",
    "i",
  ); // fragment locator

  return !!pattern.test(link);
};

export interface IRadio {
  name: string;
  id: string;
  link: string;
}
interface IRadios {
  radios: IRadio[];
}

// export abstract class Radios {
//     async radios(message: CommandMessage) {
//         const da = data;
//         var str = '';

//         for (let radio in da) {
//             str += radio + '\n';
//         }
//         message.channel.send(str);
//     }
// }
