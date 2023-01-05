import { bot } from "../../../cache.ts";
import { createCommand } from "../../utils/helpers.ts";
import { checkIfUserInMusicChannel } from "../../utils/voice.ts";
import {
  DiscordenoInteractionResponse,
  sendInteractionResponse,
  snowflakeToBigint,
} from "../../../deps.ts";

createCommand({
  name: "pause",
  guildOnly: true,
  slash: {
    enabled: true,
    guild: true,
    execute: (message) => {
      var data: DiscordenoInteractionResponse = {
        data: { content: "ping" },
        type: 4,
      };
      return sendInteractionResponse(
        snowflakeToBigint(message.id),
        message.token,
        data,
      );
    },
  },
  async execute(message) {
    const player = bot.lavadenoManager.players.get(message.guildId.toString());

    if (!player || !(await checkIfUserInMusicChannel(message, player))) {
      return message.reply(`The bot is not playing right now`);
    }

    await player.pause();

    return message.reply(`The music has now been paused.`);
  },
});
