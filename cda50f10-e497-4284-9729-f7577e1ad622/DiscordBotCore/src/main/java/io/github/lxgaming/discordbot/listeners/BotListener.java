/*
 * Copyright 2017 Alex Thomson
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package io.github.lxgaming.discordbot.listeners;

import io.github.lxgaming.discordbot.DiscordBotCore;
import io.github.lxgaming.discordbot.entries.Message;
import net.dv8tion.jda.core.events.ReadyEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

public class BotListener extends ListenerAdapter {
	
	@Override
	public void onReady(ReadyEvent event) {
		DiscordBotCore.getInstance().getChannelManager().setupChannels();
		DiscordBotCore.getInstance().getJDA().addEventListener(new MessageListener());
		DiscordBotCore.getInstance().getJDA().addEventListener(new UserListener());
		DiscordBotCore.getInstance().getJDA().addEventListener(new VoiceListener());
		
		if (!DiscordBotCore.getInstance().getConfiguration().isConnectionMessage()) {
			return;
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(new Message()
				.setChannel(DiscordBotCore.getInstance().getChannelManager().getChannelId("Bot"))
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getReadyFormat())
				.setName("")
				.setNick("")
				.setServer(DiscordBotCore.getInstance().getChannelManager().getGuild().getName())
				.setMessage("DiscordBot Connected")
				.setDiscord(true)
				.setMinecraft(true)
				.setConsole(true)
				.setRedis(false));
		return;
	}
}
