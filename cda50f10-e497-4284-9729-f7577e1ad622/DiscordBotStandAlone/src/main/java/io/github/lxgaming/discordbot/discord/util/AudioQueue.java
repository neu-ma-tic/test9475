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

package io.github.lxgaming.discordbot.discord.util;

import java.util.ArrayList;
import java.util.List;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.entries.Audio;
import net.dv8tion.jda.core.EmbedBuilder;

public class AudioQueue {
	
	private List<Audio> queue;
	private boolean repeatQueue;
	private boolean repeatSong;
	
	public AudioQueue() {
		queue = new ArrayList<Audio>();
	}
	
	public void playNext() {
		Audio audio = getNext();
		if (audio == null) {
			DiscordBot.getInstance().getDiscord().getAudioPlayer().playTrack(null);
			return;
		}
		
		DiscordBot.getInstance().getDiscord().getAudioPlayer().playTrack(audio.getAudioTrack());
		
		EmbedBuilder embedBuilder = new EmbedBuilder();
		embedBuilder.setAuthor(audio.getTextChannel().getJDA().getSelfUser().getName(), null, audio.getTextChannel().getJDA().getSelfUser().getEffectiveAvatarUrl());
		embedBuilder.setColor(DiscordUtil.DEFAULT);
		embedBuilder.addField("Now playing", audio.getAudioTrack().getInfo().title, false);
		DiscordBot.getInstance().getDiscord().getMessageSender().sendMessage(audio.getTextChannel(), embedBuilder.build(), true);
	}
	
	private Audio getNext() {
		if (getQueue() == null || getQueue().isEmpty()) {
			return null;
		}
		
		if (getQueue().get(0).hasPlayed()) {
			if (!isRepeatQueue() && !isRepeatSong()) {
				getQueue().remove(0);
			} else if (isRepeatQueue()) {
				getQueue().add(getQueue().remove(0));
			} else if (isRepeatSong()) {
				getQueue().set(0, new Audio(getQueue().get(0).getTextChannel(), getQueue().get(0).getMember(), getQueue().get(0).getAudioTrack().makeClone()));
			}
		}
		
		if (getQueue().isEmpty()) {
			return null;
		}
		return getQueue().get(0).setPlayed(true);
	}
	
	public List<Audio> getQueue() {
		return queue;
	}
	
	public boolean isRepeatQueue() {
		return repeatQueue;
	}
	
	public void setRepeatQueue(boolean repeatQueue) {
		this.repeatQueue = repeatQueue;
		if (isRepeatQueue() && isRepeatSong()) {
			setRepeatSong(false);
		}
	}
	
	public boolean isRepeatSong() {
		return repeatSong;
	}
	
	public void setRepeatSong(boolean repeatSong) {
		this.repeatSong = repeatSong;
		if (isRepeatSong() && isRepeatQueue()) {
			setRepeatQueue(false);
		}
	}
}