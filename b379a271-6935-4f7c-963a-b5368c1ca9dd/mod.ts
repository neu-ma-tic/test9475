import { bot } from "./cache.ts";
import { configs } from "./configs.ts";
import {
  camelize,
  DiscordInteractionResponseTypes,
  Interaction,
  InteractionResponseTypes,
  InteractionTypes,
  json,
  serve,
  startBot,
  validateRequest,
  verifySignature,
} from "./deps.ts";
import { fileLoader, importDirectory } from "./src/utils/helpers.ts";
import { loadLanguages, translate } from "./src/utils/i18next.ts";
import { log } from "./src/utils/logger.ts";
import { config } from "https://deno.land/x/dotenv/mod.ts";
import "https://deno.land/x/dotenv/load.ts";
import keepAlive from "./server.ts";

log.info(
  "Beginning Bot Startup Process. This can take a little bit depending on your system. Loading now...",
);

// Forces deno to read all the files which will fill the commands/inhibitors cache etc.
await Promise.all(
  [
    "./src/commands",
    "./src/inhibitors",
    "./src/events",
    "./src/arguments",
    "./src/monitors",
    "./src/tasks",
    "./src/permissionLevels",
    "./src/events",
  ].map((path) => importDirectory(Deno.realPathSync(path))),
);
await fileLoader();

// Loads languages
await loadLanguages();
await import("./src/database/database.ts");

startBot({
  token: Deno.env.get("TOKEN")!,
  // Pick the intents you wish to have for your bot.
  // For instance, to work with guild message reactions, you will have to pass the "GuildMessageReactions" intent to the array.
  intents: ["Guilds", "GuildMessages", "GuildVoiceStates"],
  // These are all your event handler functions. Imported from the events folder
  eventHandlers: bot.eventHandlers,
});

// keepAlive();

serve({
  "/": main,
});

async function main(request: Request) {
  // Validate the incmoing request; whether or not, it includes
  // the specified headers that are sent by Discord.
  const { error } = await validateRequest(request, {
    POST: {
      headers: ["X-Signature-Ed25519", "X-Signature-Timestamp"],
    },
  });
  if (error) {
    return json({ error: error.message }, { status: error.status });
  }

  const publicKey = Deno.env.get("DISCORD_PUBLIC_KEY");
  if (!publicKey) {
    return json({
      error: "Missing Discord public key from environment variables.",
    });
  }

  const signature = request.headers.get("X-Signature-Ed25519")!;
  const timestamp = request.headers.get("X-Signature-Timestamp")!;

  const { body, isValid } = verifySignature({
    publicKey,
    signature,
    timestamp,
    body: await request.text(),
  });
  if (!isValid) {
    return json({ error: "Invalid request; could not verify the request" }, {
      status: 401,
    });
  }

  const payload = camelize<Interaction>(JSON.parse(body));
  if (payload.type === InteractionTypes.Ping) {
    return json({
      type: InteractionResponseTypes.Pong,
    });
  } else if (payload.type === InteractionTypes.ApplicationCommand) {
    if (!payload.data?.name) {
      return json({
        type: InteractionResponseTypes.ChannelMessageWithSource,
        data: {
          content:
            "Something went wrong. I was not able to find the command name in the payload sent by Discord.",
        },
      });
    }

    const command = bot.commands.get(payload.data.name);
    if (!command) {
      return json({
        type: InteractionResponseTypes.ChannelMessageWithSource,
        data: {
          content: "Something went wrong. I was not able to find this command.",
        },
      });
    }

    // Make sure the user has the permission to run this command.
    // if (!(await hasPermissionLevel(command, payload))) {
    // return json({
    //   type: InteractionResponseTypes.ChannelMessageWithSource,
    //   data: {
    //     content: translate(
    //       payload.guildId!,
    //       "MISSING_PERM_LEVEL",
    //     ),
    //   },
    // });
    // }

    if (typeof command !== "undefined") {
      const result = await command.execute(payload);
      // if (!isInteractionResponse(result)) {
      //   await logWebhook(payload).catch(console.error);
      //   return json({
      //     data: result,
      //     type: DiscordInteractionResponseTypes.ChannelMessageWithSource,
      //   });
      // }

      // DENO/TS BUG DOESNT LET US SEND A OBJECT WITHOUT THIS OVERRIDE
      return json(result as unknown as { [key: string]: unknown });
    }
  }

  return json({ error: "Bad request" }, { status: 400 });
}

// const interaction = new DiscordInteractions({
//   applicationId: "843485383224197140",
//   authToken: configs.token,
//   publicKey: "85ba2076bdff89633e62c23ceeaddc24000dcf446bfcdd7d330d6e84b64a88b4",
// });

// await interaction
//   .getApplicationCommands()
//   .then(console.log)
//   .catch(console.error);

// const command = {
//   name: "avatar",
//   description: "get a users avatar",
//   options: [
//     {
//       name: "big",
//       description: "should the image be big",
//       type: ApplicationCommandOptionType.BOOLEAN,
//     },
//   ],
// };

// const command = {
//   name: "ponga",
//   description: "pong",
//   options: [
//     {
//       name: "echo",
//       description: "echo this string",
//       type: ApplicationCommandOptionType.STRING
//     },
//   ],
// };

// await interaction
//   .createApplicationCommand(command, "843498760280604682")
//   .then(console.log)
//   .catch(console.error);
