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
import net.dv8tion.jda.core.events.user.UserAvatarUpdateEvent;
import net.dv8tion.jda.core.events.user.UserGameUpdateEvent;
import net.dv8tion.jda.core.events.user.UserNameUpdateEvent;
import net.dv8tion.jda.core.events.user.UserOnlineStatusUpdateEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

public class UserListener extends ListenerAdapter {
	
	@Override
	public void onUserAvatarUpdate(UserAvatarUpdateEvent event) {
		if (!DiscordBotCore.getInstance().getConfiguration().isUserAvatarUpdate()) {
			return;
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(new Message()
				.setChannel(DiscordBotCore.getInstance().getChannelManager().getChannelId("Bot"))
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getUserAvatarUpdateFormat())
				.setName(event.getUser().getName())
				.setNick(DiscordBotCore.getInstance().getChannelManager().getGuild().getMember(event.getUser()).getNickname())
				.setServer(DiscordBotCore.getInstance().getChannelManager().getGuild().getName())
				.setMessage(event.getUser().getAvatarId())
				.setDiscord(true)
				.setMinecraft(true)
				.setConsole(false)
				.setRedis(false));
		return;
	}
	
	@Override
	public void onUserGameUpdate(UserGameUpdateEvent event) {
		if (!DiscordBotCore.getInstance().getConfiguration().isUserGameUpdate() || DiscordBotCore.getInstance().getChannelManager().getGuild().getMember(event.getUser()).getGame() == null) {
			return;
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(new Message()
				.setChannel(DiscordBotCore.getInstance().getChannelManager().getChannelId("Bot"))
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getUserGameUpdateFormat())
				.setName(event.getUser().getName())
				.setNick(DiscordBotCore.getInstance().getChannelManager().getGuild().getMember(event.getUser()).getNickname())
				.setServer(DiscordBotCore.getInstance().getChannelManager().getGuild().getName())
				.setMessage(DiscordBotCore.getInstance().getChannelManager().getGuild().getMember(event.getUser()).getGame().getName())
				.setDiscord(true)
				.setMinecraft(true)
				.setConsole(false)
				.setRedis(false));
		return;
	}
	
	@Override
	public void onUserNameUpdate(UserNameUpdateEvent event) {
		if (!DiscordBotCore.getInstance().getConfiguration().isUserNameUpdate()) {
			return;
		}
		
		DiscordBotCore.getInstance().getMessageSender().sendMessage(new Message()
				.setChannel(DiscordBotCore.getInstance().getChannelManager().getChannelId("Bot"))
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getUserNameUpdateFormat())
				.setName(event.getUser().getName())
				.setNick(DiscordBotCore.getInstance().getChannelManager().getGuild().getMember(event.getUser()).getNickname())
				.setServer(DiscordBotCore.getInstance().getChannelManager().getGuild().getName())
				.setMessage(event.getOldName())
				.setDiscord(true)
				.setMinecraft(true)
				.setConsole(false)
				.setRedis(false));
		return;
	}
	
	@Override
	public void onUserOnlineStatusUpdate(UserOnlineStatusUpdateEvent event) {
		if (!DiscordBotCore.getInstance().getConfiguration().isUserOnlineStatusUpdate()) {
			return;
		}
		
		String status = DiscordBotCore.getInstance().getChannelManager().getGuild().getMember(event.getUser()).getOnlineStatus().name();
		DiscordBotCore.getInstance().getMessageSender().sendMessage(new Message()
				.setChannel(DiscordBotCore.getInstance().getChannelManager().getChannelId("Bot"))
				.setFormat(DiscordBotCore.getInstance().getConfiguration().getUserOnlineStatusUpdateFormat().get(status))
				.setName(event.getUser().getName())
				.setNick(DiscordBotCore.getInstance().getChannelManager().getGuild().getMember(event.getUser()).getNickname())
				.setServer(DiscordBotCore.getInstance().getChannelManager().getGuild().getName())
				.setMessage(status)
				.setDiscord(true)
				.setMinecraft(true)
				.setConsole(false)
				.setRedis(false));
		return;
	}
}
