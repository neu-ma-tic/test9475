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
import io.github.lxgaming.discordbot.entries.Audio;
import io.github.lxgaming.discordbot.entries.ICommand;
import net.dv8tion.jda.core.EmbedBuilder;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.TextChannel;

public class RemoveCommand implements ICommand {
	
	@Override
	public void execute(TextChannel textChannel, Member member, Message message, List<String> arguments) {
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.DEFAULT);
		
		if (arguments == null || arguments.isEmpty()) {
			embedBuilder.setColor(DiscordUtil.ERROR);
			embedBuilder.setTitle("Invalid arguments!", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		if (DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue() == null || DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue().isEmpty()) {
			embedBuilder.setColor(DiscordUtil.ERROR);
			embedBuilder.setTitle("Queue is empty!", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		if (arguments.get(0).equalsIgnoreCase("all")) {
			DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue().clear();
			embedBuilder.setColor(DiscordUtil.SUCCESS);
			embedBuilder.setTitle("All songs from queue removed.", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		try {
			int index = (Integer.parseInt(arguments.get(0)) - 1);
			if (index > DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue().size() || index < 0) {
				throw new NumberFormatException();
			}
			
			Audio audio = DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue().remove(index);
			
			embedBuilder.setColor(DiscordUtil.SUCCESS);
			if (audio != null && audio.getAudioTrack() != null) {
				embedBuilder.setTitle("Removed '" + audio.getAudioTrack().getInfo().title + "'.");
			} else {
				embedBuilder.setTitle("Removed '" + "Unknown" + "'.");
			}
			
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
		} catch (NumberFormatException ex) {
			embedBuilder.setColor(DiscordUtil.ERROR);
			embedBuilder.setTitle("Supplied value is outside the queue range!", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
	}
	
	@Override
	public String getName() {
		return "Remove";
	}
	
	@Override
	public String getDescription() {
		return "Removes specific songs from queue.";
	}
	
	@Override
	public String getUsage() {
		return DiscordBot.getInstance().getConfig().getCommandPrefix() + "Remove <Number | All>";
	}
	
	@Override
	public List<String> getAliases() {
		return Arrays.asList("RM");
	}
}