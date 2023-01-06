import lightbulb

from protótipo.bot import Bot

meta_plugin = lightbulb.Plugin("Meta")

bot = Bot()

@meta_plugin.command
@lightbulb.command("ping", "Mostra a latência do bot.")
@lightbulb.implements(lightbulb.SlashCommand)
async def command_ping(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(f"Pong!\nLatência: {ctx.bot.heartbeat_latency * 1000:,.0f} ms.")


def load(bot: Bot) -> None:
    bot.add_plugin(meta_plugin)

def unload(bot: Bot) -> None:
        bot.remove_plugin(meta_plugin)
