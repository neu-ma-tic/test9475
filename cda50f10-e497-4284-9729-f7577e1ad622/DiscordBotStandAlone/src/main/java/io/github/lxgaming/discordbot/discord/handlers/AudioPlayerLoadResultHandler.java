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

package io.github.lxgaming.discordbot.discord.handlers;

import java.util.Iterator;

import com.sedmelluq.discord.lavaplayer.player.AudioLoadResultHandler;
import com.sedmelluq.discord.lavaplayer.tools.FriendlyException;
import com.sedmelluq.discord.lavaplayer.track.AudioPlaylist;
import com.sedmelluq.discord.lavaplayer.track.AudioTrack;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.discord.util.DiscordUtil;
import io.github.lxgaming.discordbot.entries.Audio;
import io.github.lxgaming.discordbot.util.LogHelper;
import net.dv8tion.jda.core.EmbedBuilder;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.TextChannel;

public class AudioPlayerLoadResultHandler implements AudioLoadResultHandler {
	
	private final TextChannel textChannel;
	private final Member member;
	
	public AudioPlayerLoadResultHandler(TextChannel textChannel, Member member) {
		this.textChannel = textChannel;
		this.member = member;
	}
	
	@Override
	public void trackLoaded(AudioTrack audioTrack) {
		if (audioTrack == null) {
			return;
		}
		
		Audio audio = new Audio(getTextChannel(), getMember(), audioTrack);
		DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue().add(audio);
		if (DiscordBot.getInstance().getDiscord().getAudioPlayer().getPlayingTrack() == null) {
			DiscordBot.getInstance().getDiscord().getAudioQueue().playNext();
		} else {
			EmbedBuilder embedBuilder = new EmbedBuilder();
			embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
			embedBuilder.setColor(DiscordUtil.SUCCESS);
			embedBuilder.setTitle("'" + audio.getAudioTrack().getInfo().title + "' Has been added to the queue.", null);
			DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
		}
		audio = null;
	}
	
	@Override
	public void playlistLoaded(AudioPlaylist audioPlaylist) {
		for (Iterator<AudioTrack> iterator = audioPlaylist.getTracks().iterator(); iterator.hasNext();) {
			AudioTrack audioTrack = iterator.next();
			if (audioTrack == null) {
				continue;
			}
			
			Audio audio = new Audio(getTextChannel(), getMember(), audioTrack);
			DiscordBot.getInstance().getDiscord().getAudioQueue().getQueue().add(audio);
			if (DiscordBot.getInstance().getDiscord().getAudioPlayer().getPlayingTrack() == null) {
				DiscordBot.getInstance().getDiscord().getAudioQueue().playNext();
			} else {
				LogHelper.debug("'" + audio.getAudioTrack().getInfo().title + "' Has been added to the queue.");
			}
			audio = null;
		}
		LogHelper.debug(audioPlaylist.getTracks().size() + " Songs have been added to the queue.");
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.SUCCESS);
		embedBuilder.setTitle(audioPlaylist.getTracks().size() + " Songs have been added to the queue.", null);
		DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
	}
	
	@Override
	public void noMatches() {
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.ERROR);
		embedBuilder.setTitle("No matches found!", null);
		DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
	}
	
	@Override
	public void loadFailed(FriendlyException exception) {
		LogHelper.error("Failed to load - " + exception.getMessage());
		exception.printStackTrace();
		
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(textChannel.getJDA().getSelfUser().getName(), null, textChannel.getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.ERROR);
		embedBuilder.addField("Failed to load", exception.getMessage(), false);
		DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(textChannel, embedBuilder.build(), true);
	}
	
	public TextChannel getTextChannel() {
		return textChannel;
	}
	
	public Member getMember() {
		return member;
	}
}