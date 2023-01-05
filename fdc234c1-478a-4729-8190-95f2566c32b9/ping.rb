# frozen_string_literal: true

require 'discordrb'

bot = Discordrb::Bot.new token: '<token goes here>'

bot.message(with_text: 'Ping!') do |event|
  event.respond 'Pong!'
end

bot.message(with_text: 'Poggers') do |event|
  event.respond 'Pogchamp'
end

bot.run
