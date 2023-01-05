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

import java.util.Arrays;
import java.util.List;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.discord.util.DiscordUtil;
import io.github.lxgaming.discordbot.entries.ICommand;
import net.dv8tion.jda.core.EmbedBuilder;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.TextChannel;

public class RepeatCommand implements ICommand {
	
	@Override
	public void execute(TextChannel textChannel, Member member, Message message, List<String> arguments) {
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.DEFAULT);
		
		if (arguments == null || arguments.isEmpty()) {
			embedBuilder.setColor(DiscordUtil.DEFAULT);
			embedBuilder.addField("Repeat Song", "" + DiscordBot.getInstance().getDiscord().getAudioQueue().isRepeatSong(), true);
			embedBuilder.addField("Repeat Queue", "" + DiscordBot.getInstance().getDiscord().getAudioQueue().isRepeatQueue(), true);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		if (arguments.get(0).equalsIgnoreCase("song")) {
			if (DiscordBot.getInstance().getDiscord().getAudioPlayer().isPaused() || DiscordBot.getInstance().getDiscord().getAudioPlayer().getPlayingTrack() == null) {
				embedBuilder.setColor(DiscordUtil.ERROR);
				embedBuilder.setTitle("No song playing!", null);
				DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
				return;
			}
			
			if (DiscordBot.getInstance().getDiscord().getAudioQueue().isRepeatSong()) {
				DiscordBot.getInstance().getDiscord().getAudioQueue().setRepeatSong(false);
				embedBuilder.setColor(DiscordUtil.WARNING);
				embedBuilder.setTitle("No longer repeating current song.", null);
			} else {
				DiscordBot.getInstance().getDiscord().getAudioQueue().setRepeatSong(true);
				embedBuilder.setColor(DiscordUtil.SUCCESS);
				embedBuilder.setTitle("Repeating current song.", null);
			}
			
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		if (arguments.get(0).equalsIgnoreCase("queue")) {
			if (DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue() == null || DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue().isEmpty()) {
				embedBuilder.setColor(DiscordUtil.ERROR);
				embedBuilder.setTitle("No song in queue!", null);
				DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
				return;
			}
			
			if (DiscordBot.getInstance().getDiscord().getAudioQueue().isRepeatQueue()) {
				DiscordBot.getInstance().getDiscord().getAudioQueue().setRepeatQueue(false);
				embedBuilder.setColor(DiscordUtil.WARNING);
				embedBuilder.setTitle("No longer repeating current queue.", null);
			} else {
				DiscordBot.getInstance().getDiscord().getAudioQueue().setRepeatQueue(false);
				embedBuilder.setColor(DiscordUtil.SUCCESS);
				embedBuilder.setTitle("Repeating current queue.", null);
			}
			
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
	}
	
	@Override
	public String getName() {
		return "Repeat";
	}
	
	@Override
	public String getDescription() {
		return "Repeats current song or queue.";
	}
	
	@Override
	public String getUsage() {
		return DiscordBot.getInstance().getConfig().getCommandPrefix() + "Repeat <Song | Queue>";
	}
	
	@Override
	public List<String> getAliases() {
		return Arrays.asList("Loop");
	}
}