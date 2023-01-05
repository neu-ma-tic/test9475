import { Milliseconds } from "../utils/constants/time.ts";
import { botId, cache, cacheHandlers } from "../../deps.ts";
import { bot } from "../../cache.ts";

const MESSAGE_LIFETIME = Milliseconds.MINUTE * 10;
const MEMBER_LIFETIME = Milliseconds.MINUTE * 30;

bot.tasks.set(`sweeper`, {
  name: `sweeper`,
  interval: Milliseconds.MINUTE * 5,
  execute: function () {
    const now = Date.now();
    // Delete presences from the bots cache.
    cacheHandlers.clear("presences");
    // For every guild, we will clean the cache
    cacheHandlers.forEach("guilds", (guild) => {
      // Delete presences from the guild caches.
      guild.presences.clear();
      // Delete any member who has not been active in the last 30 minutes and is not currently in a voice channel
      guild.members.forEach((member) => {
        // Don't purge the bot else bugs will occure
        if (member.id === botId) return;
        // The user is currently active in a voice channel
        if (guild.voiceStates.has(member.id)) return;
        const lastActive = bot.memberLastActive.get(member.id);
        // If the user is active recently
        if (lastActive && now - lastActive < MEMBER_LIFETIME) return;
        cache.members.delete(member.id);
        bot.memberLastActive.delete(member.id);
      });
    });

    // For ever, message we will delete if necessary
    cacheHandlers.forEach("messages", (message) => {
      // Delete any messages over 10 minutes old
      if (now - message.timestamp > MESSAGE_LIFETIME) {
        cache.messages.delete(message.id);
      }
    });
  },
});
