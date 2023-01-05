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

public class SkipCommand implements ICommand {
	
	@Override
	public void execute(TextChannel textChannel, Member member, Message message, List<String> arguments) {
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.DEFAULT);
		
		if (DiscordBot.getInstance().getDiscord().getAudioQueue().isRepeatSong()) {
			embedBuilder.setColor(DiscordUtil.WARNING);
			DiscordBot.getInstance().getDiscord().getAudioQueue().setRepeatSong(false);
			embedBuilder.setTitle("Repeat is now off, Skipping...", null);
		} else {
			embedBuilder.setColor(DiscordUtil.SUCCESS);
			embedBuilder.setTitle("Skipping...", null);
		}
		
		DiscordBot.getInstance().getDiscord().getAudioQueue().playNext();
		DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
	}
	
	@Override
	public String getName() {
		return "Skip";
	}
	
	@Override
	public String getDescription() {
		return "Plays next song in queue.";
	}
	
	@Override
	public String getUsage() {
		return DiscordBot.getInstance().getConfig().getCommandPrefix() + "Skip";
	}
	
	@Override
	public List<String> getAliases() {
		return Arrays.asList("Next");
	}
}