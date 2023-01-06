using Discord.Interactions;
using System.Threading.Tasks;

public class Commands : InteractionModuleBase<SocketInteractionContext>
{
    [SlashCommand("echo", "Repeats what you say.")]
    public async Task Echo(string input)
    {
        await RespondAsync($"✏️ You said: `{input}`");
    }

    [SlashCommand("ping", "Displays the ping of the bot.")]
    public async Task Ping()
    {
        await RespondAsync($"🏓 Pong! The client latency is **{Bot.Client.Latency}** ms.");
    }
}