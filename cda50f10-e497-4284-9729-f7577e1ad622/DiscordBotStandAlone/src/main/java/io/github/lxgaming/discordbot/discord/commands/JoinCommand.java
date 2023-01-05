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

import java.util.List;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.discord.util.DiscordUtil;
import io.github.lxgaming.discordbot.entries.ICommand;
import net.dv8tion.jda.core.EmbedBuilder;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.TextChannel;
import net.dv8tion.jda.core.entities.VoiceChannel;

public class JoinCommand implements ICommand {
	
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
		
		List<VoiceChannel> voiceChannels = member.getGuild().getVoiceChannelsByName(arguments.get(0), false);
		if (voiceChannels.size() < 1) {
			embedBuilder.setColor(DiscordUtil.ERROR);
			embedBuilder.setTitle("Unable to find specified voice channel!", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
			return;
		}
		
		if (member.getGuild().getAudioManager().getConnectedChannel() != null) {
			member.getGuild().getAudioManager().closeAudioConnection();
		}
		
		try {
			member.getGuild().getAudioManager().openAudioConnection(voiceChannels.get(0));
			embedBuilder.setColor(DiscordUtil.SUCCESS);
			embedBuilder.setTitle("Joined channel '" + voiceChannels.get(0).getName() + "'.", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
		} catch (RuntimeException ex) {
			embedBuilder.setColor(DiscordUtil.ERROR);
			embedBuilder.addField("Cannot join channel '" + voiceChannels.get(0).getName() + "'!", ex.getMessage(), false);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
		}
	}
	
	@Override
	public String getName() {
		return "Join";
	}
	
	@Override
	public String getDescription() {
		return "Connects the bot to a voice channel.";
	}
	
	@Override
	public String getUsage() {
		return DiscordBot.getInstance().getConfig().getCommandPrefix() + "Join <Channel>";
	}
	
	@Override
	public List<String> getAliases() {
		return null;
	}
}