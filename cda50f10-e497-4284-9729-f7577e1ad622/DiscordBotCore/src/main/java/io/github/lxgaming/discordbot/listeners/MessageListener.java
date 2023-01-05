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
import io.github.lxgaming.discordbot.commands.DiscordCommand;
import io.github.lxgaming.discordbot.entries.Message;
import net.dv8tion.jda.core.entities.ChannelType;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

public class MessageListener extends ListenerAdapter {
	
	@Override
	public void onMessageReceived(MessageReceivedEvent event) {		
		if (!event.isFromType(ChannelType.TEXT) || event.getAuthor().isBot() || event.getAuthor().isFake()) {
			return;
		}
		
		if (event.getMessage().getContent().startsWith(DiscordBotCore.getInstance().getConfiguration().getCommandPrefix()) && DiscordBotCore.getInstance().getConfiguration().isAllowCommands()) {
			new DiscordCommand().execute(event.getTextChannel(), event.getMember(), event.getMessage().getContent().substring(DiscordBotCore.getInstance().getConfiguration().getCommandPrefix().length()));
			return;
		} else if (event.getMessage().getContent().startsWith("/") && DiscordBotCore.getInstance().getConfiguration().isAllowCommands()) {
			new DiscordCommand().execute(event.getTextChannel(), event.getMember(), event.getMessage().getContent().substring(1));
			return;
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(new Message()
				.setChannel(event.getChannel().getId())
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getChannelFormat().get(DiscordBotCore.getInstance().getChannelManager().getChannelName(event.getTextChannel().getId())))
				.setName(event.getMember().getEffectiveName())
				.setNick(event.getMember().getNickname())
				.setServer(event.getChannel().getName())
				.setMessage(event.getMessage().getContent())
				.setDiscord(false)
				.setMinecraft(true)
				.setConsole(true)
				.setRedis(false));
		return;
	}
}
