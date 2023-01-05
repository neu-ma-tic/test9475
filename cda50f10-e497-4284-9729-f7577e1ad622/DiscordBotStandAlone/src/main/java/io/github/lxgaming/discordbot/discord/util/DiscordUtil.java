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

import java.awt.Color;
import java.net.MalformedURLException;
import java.net.URL;

import org.apache.commons.lang3.StringUtils;
import org.joda.time.Duration;
import org.joda.time.Period;
import org.joda.time.format.PeriodFormatter;
import org.joda.time.format.PeriodFormatterBuilder;

import io.github.lxgaming.discordbot.util.LogHelper;

public class DiscordUtil {
	
	public static final Color DEFAULT = Color.decode("#7289DA");
	public static final Color SUCCESS = Color.decode("#46A84B");
	public static final Color WARNING = Color.decode("#EAA245");
	public static final Color ERROR = Color.decode("#C13737");
	
	public static String getTimestamp(long duration) {
		PeriodFormatter periodFormatter = new PeriodFormatterBuilder()
				.appendYears().appendSuffix("y ")
				.appendMonths().appendSuffix("m ")
				.appendWeeks().appendSuffix("w ")
				.appendDays().appendSuffix("d ")
				.appendHours().appendSuffix("h ")
				.appendMinutes().appendSuffix("m ")
				.appendSeconds().appendSuffix("s")
				.toFormatter();
		return periodFormatter.print(new Period(new Duration(duration)).normalizedStandard());
	}
	
	public static String filter(String message) {
		if (StringUtils.isNotBlank(message)) {
			return message.replaceAll("[^\\x20-\\x7E\\r\\n]", "");
		}
		return "Filter error!";
	}
	
	public static URL encodeURL(String url) {
		try {
			if (StringUtils.isBlank(url)) {
				return null;
			}
			
			return new URL(url);
		} catch (MalformedURLException ex) {
			LogHelper.error("Failed to encode URL!");
		}
		return null;
	}
}