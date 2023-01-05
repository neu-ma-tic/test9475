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

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.discord.util.DiscordUtil;
import io.github.lxgaming.discordbot.entries.ICommand;
import net.dv8tion.jda.core.EmbedBuilder;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.TextChannel;

public class ShuffleCommand implements ICommand {
	
	@Override
	public void execute(TextChannel textChannel, Member member, Message message, List<String> arguments) {
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.DEFAULT);
		
		if (DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue() == null || DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue().size() < 2) {
			embedBuilder.setColor(DiscordUtil.ERROR);
			embedBuilder.setTitle("The current queue is not big enough to shuffle!", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		Collections.shuffle(DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue(), new Random(System.nanoTime()));
		embedBuilder.setColor(DiscordUtil.SUCCESS);
		embedBuilder.setTitle("Current queue shuffled.", null);
		DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
	}
	
	@Override
	public String getName() {
		return "Shuffle";
	}
	
	@Override
	public String getDescription() {
		return "Shuffles all songs in current queue.";
	}
	
	@Override
	public String getUsage() {
		return DiscordBot.getInstance().getConfig().getCommandPrefix() + "Shuffle";
	}
	
	@Override
	public List<String> getAliases() {
		List<String> aliases = new ArrayList<String>();
		aliases.add("Shake");
		return aliases;
	}
}