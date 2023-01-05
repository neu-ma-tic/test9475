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

package io.github.lxgaming.discordbot.discord.commands;

import java.net.URL;
import java.util.Iterator;
import java.util.List;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.discord.handlers.AudioPlayerLoadResultHandler;
import io.github.lxgaming.discordbot.discord.util.DiscordUtil;
import io.github.lxgaming.discordbot.entries.ICommand;
import net.dv8tion.jda.core.EmbedBuilder;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.TextChannel;

public class PlayCommand implements ICommand {
	
	@Override
	public void execute(TextChannel textChannel, Member member, Message message, List<String> arguments) {
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.DEFAULT);
		
		if (member.getGuild().getAudioManager().getConnectedChannel() == null) {
			embedBuilder.setColor(DiscordUtil.ERROR);
			embedBuilder.setTitle("Not connected to voice channel!", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		if (arguments == null || arguments.isEmpty()) {
			if (DiscordBot.getInstance().getDiscord().getAudioPlayer().isPaused()) {
				DiscordBot.getInstance().getDiscord().getAudioPlayer().setPaused(false);
				embedBuilder.setColor(DiscordUtil.SUCCESS);
				embedBuilder.setTitle("Playback resumed.", null);
			} else {
				DiscordBot.getInstance().getDiscord().getAudioPlayer().setPaused(true);
				embedBuilder.setColor(DiscordUtil.WARNING);
				embedBuilder.setTitle("Playback paused.", null);
			}
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		embedBuilder.setColor(DiscordUtil.SUCCESS);
		for (Iterator<String> iterator = arguments.iterator(); iterator.hasNext();) {
			String string = iterator.next();
			
			URL url = DiscordUtil.encodeURL(string);
			if (url == null) {
				embedBuilder.setColor(DiscordUtil.WARNING);
				embedBuilder.addField("Invalid URL!", string, false);
				continue;
			}
			
			if (!DiscordBot.getInstance().getConfig().getAllowedSources().contains(url.getHost())) {
				embedBuilder.setColor(DiscordUtil.WARNING);
				embedBuilder.addField("This source is not allowed!", string, false);
				continue;
			}
			
			DiscordBot.getInstance().getDiscord().getAudioPlayerManager().loadItem(string, new AudioPlayerLoadResultHandler(textChannel, member));
			embedBuilder.addField("Processing", string, false);
		}
		DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
	}
	
	@Override
	public String getName() {
		return "Play";
	}
	
	@Override
	public String getDescription() {
		return "Toggles Playback state or Play specified media if URL is provided.";
	}
	
	@Override
	public String getUsage() {
		return DiscordBot.getInstance().getConfig().getCommandPrefix() + "Play [URL]";
	}
	
	@Override
	public List<String> getAliases() {
		return null;
	}
}