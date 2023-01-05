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

package io.github.lxgaming.discordbot.discord.listeners;

import com.sedmelluq.discord.lavaplayer.player.AudioPlayer;
import com.sedmelluq.discord.lavaplayer.player.event.AudioEventAdapter;
import com.sedmelluq.discord.lavaplayer.tools.FriendlyException;
import com.sedmelluq.discord.lavaplayer.track.AudioTrack;
import com.sedmelluq.discord.lavaplayer.track.AudioTrackEndReason;

import io.github.lxgaming.discordbot.DiscordBot;
import io.github.lxgaming.discordbot.util.LogHelper;

public class AudioListener extends AudioEventAdapter {
	
	@Override
	public void onPlayerPause(AudioPlayer audioPlayer) {
		LogHelper.debug("Player pause.");
	}
	
	@Override
	public void onPlayerResume(AudioPlayer audioPlayer) {
		LogHelper.debug("Player resume.");
	}
	
	@Override
	public void onTrackEnd(AudioPlayer audioPlayer, AudioTrack audioTrack, AudioTrackEndReason audioTrackEndReason) {
		if (audioTrackEndReason.equals(AudioTrackEndReason.FINISHED) && audioTrackEndReason.mayStartNext) {
			LogHelper.debug("Track Finished, Playing next.");
			DiscordBot.getInstance().getDiscord().getAudioQueue().playNext();
			return;
		}
		
		if (audioTrackEndReason.equals(AudioTrackEndReason.STOPPED)) {
			LogHelper.debug("Track stopped.");
			return;
		}
		
		if (audioTrackEndReason.equals(AudioTrackEndReason.REPLACED)) {
			LogHelper.debug("Track replaced.");
		}
	}
	
	@Override
	public void onTrackException(AudioPlayer audioPlayer, AudioTrack audioTrack, FriendlyException friendlyException) {
		LogHelper.debug("Track Exception!");
		LogHelper.error(friendlyException.getMessage());
		friendlyException.printStackTrace();
		
		DiscordBot.getInstance().getDiscord().getAudioQueue().playNext();
	}
	
	@Override
	public void onTrackStart(AudioPlayer audioPlayer, AudioTrack audioTrack) {
		LogHelper.debug("Track start!");
	}
	
	@Override
	public void onTrackStuck(AudioPlayer audioPlayer, AudioTrack audioTrack, long time) {
		LogHelper.debug("Track stuck.");
	}
}