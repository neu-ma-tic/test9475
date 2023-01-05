import discord
from discord.ext import commands
import random
import pygame


player_score1 = 0
bot_score1 = 0
tries = 0
tries1 = 0
words = ['car', 'orthographic', 'small', 'large', 'cock', 'house', 'mater', 'unbelievable', 'computer', 'bot',
         'pythonisbestlol', 'island', 'power', 'satan', 'beds', 'invert', 'up', 'sewer', 'street', 'anthropology',
         'geology', 'otolaryngology']
word = random.choice(words)
message = ''


class Rock(commands.Cog):

    def __init__(self, client, player_score1, bot_score1):
        self.client = client
        self.player_score1 = player_score1
        self.bot_score1 = bot_score1

    @commands.command()
    async def rps(self, ctx, *, question):
        list = ['rock', 'paper', 'scissors']
        choice = random.choice(list)

        await ctx.send(f'Bot rolled: {choice}')

        if question == "rock" and choice == "paper":
            await ctx.send('Bot wins!')
            self.bot_score1 += 1
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question == "rock" and choice == "scissors":
            await ctx.send('Player wins!')
            self.player_score1 += 1
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question == "rock" and choice == "rock":
            await ctx.send('Its a tie!')
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question == "paper" and choice == "paper":
            await ctx.send('Its a tie!')
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question == "paper" and choice == "scissors":
            await ctx.send('Bot wins!')
            self.bot_score1 += 1
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question == "paper" and choice == "rock":
            await ctx.send('Player wins!')
            self.player_score1 += 1
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question == "scissors" and choice == "paper":
            await ctx.send('Player wins!')
            self.player_score1 += 1
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question == "scissors" and choice == "rock":
            await ctx.send('Bot wins!')
            self.bot_score1 += 1
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question == "scissors" and choice == "scissors":
            await ctx.send('Its a tie!')
            await ctx.send(f'Bot: {self.bot_score1} || Player: {self.player_score1}')

        if question != "quit":
            await Rock.rps()


class Guess(commands.Cog):

    num = random.randint(1, 10)
    num2 = random.randint(1, 100)

    def __init__(self, client, tries, tries1):
        self.client = client
        self.tries = tries
        self.tries1 = tries1

    @commands.command()
    async def guesser10(self, ctx, *, guess):

        if (int(Guess.num) - int(guess)) == 0:
            await ctx.send('You guessed the number, you won!')
            Guess.num = random.randint(1, 10)
        elif (int(Guess.num) - int(guess)) != 0:
            await ctx.send(f"Number {guess} isn't correct, try again.")
            self.tries += 1

        if self.tries >= 5:
            await ctx.send('You lost!')
        else:
            await Guess.guesser10()

    @commands.command()
    async def guesser100(self, ctx, *, guess1):

        if (int(Guess.num2) - int(guess1)) == 0:
            await ctx.send('You guessed the number, you won!')
            Guess.num2 = random.randint(1, 100)
        elif (int(Guess.num2) - int(guess1)) != 0:
            await ctx.send(f"Number {guess1} isn't correct, try again.")
            self.tries1 += 1

        if self.tries1 >= int(100 / 2):
            ctx.send('You lost!')
        else:
            await Guess.guesser100()


class HangMan(commands.Cog):

    def __init__(self, client, guessing, missed):
        self.client = client
        self.guessing = guessing
        self.missed = missed

    @commands.command()
    async def game(self, ctx):
        self.client.add_cog(Game(self.client))

    @commands.command(aliases=['hang', 'man'])
    async def hangman(self, ctx, message):
        guessed = []
        i = 0

        await ctx.send('Not working yet')

        if message.lower() in word.lower():
            guessed.append(message)
            self.guessing += message
            await ctx.send(self.guessing)
        elif message.lower() == word:
            await ctx.send('YOU WON!')
        else:
            self.missed += 1
            await ctx.send('YOU MISSED!')

        if self.missed == 0:
            await ctx.send("""
___________________  
|                |  
|               0  
|              /|\\
|                |  
|              / \\
---""")

        elif self.missed == 1:
            await ctx.send("""
___________________
|                |  
|               0  
|              /|\\
|                |  
|                \\
---""")

        elif self.missed == 2:
            await ctx.send("""
            ___________________
            |                |  
            |               0  
            |              /|\\
            |                |  
            |                \\
            ---""")


class Game(commands.Cog):

    def __init__(self, client):
        self.client = client
        pygame.init()
        self.win = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("A game")

        self.player = pygame.Rect(200, 200, 50, 200)
        self.tiles = []
        self.collisions = []
        self.p_mov = (0, 0)

        while True:

            self.win.fill((0, 0, 0))
            pygame.draw.rect(self.win, (255, 255, 255), self.player)
            for i in range(800 // 50):
                self.tiles.append(pygame.Rect(i * 50, 750, 50, 50))

            for tile in self.tiles:
                pygame.draw.rect(self.win, (255, 255, 0), tile)
                if tile.colliderect(self.player):
                    self.collisions.append(tile)

            self.gravity()
            self.movement()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

    def gravity(self):
        self.player.y += 2

    def movement(self):
        self.player.x += self.p_mov[0]
        for tile in self.collisions:
            if self.p_mov[0] > 0:
                self.player.right = tile.left
            if self.p_mov[0] < 0:
                self.player.left = tile.right
        self.player.y += self.p_mov[1]
        for tile in self.collisions:
            if self.p_mov[1] > 0:
                self.player.bottom = tile.top
            if self.p_mov[1] < 0:
                self.player.top = tile.bottom


def setup(client):
    client.add_cog(Rock(client, bot_score1, player_score1))
    client.add_cog(Guess(client, tries, tries1))
    client.add_cog(HangMan(client, message, 0))


