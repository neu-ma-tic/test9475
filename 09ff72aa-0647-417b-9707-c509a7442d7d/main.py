import discord
import random
#import global_var
#import BlackJack.py

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
      #waits for user to say =hello and it will send a message back hello
    if message.content.startswith('=hello'):
        await message.channel.send('Hello!')
      #waits for user to say =leaderboard and it will send a message back a list of the leaderboard
    channel = (813456023636672564)

    if message.content.startswith('=leaderbaord'):
      await message.channel.send(leaderboard)

    if message.content.startswith('=playblackjack'):
      (Blackjack())


#Blackjack game. still in the works




class Deck():
        
    def __init__(self):
        self.deck = ['A','K','Q','J','10','9','8','7','6','5'
                 ,'4','3','2','A','K','Q','J','10','9','8','7','6'
                 ,'5','4','3','2','A','K','Q','J','10','9','8'
                 ,'7','6','5','4','3','2','A','K','Q','J','10','9'
                 ,'8','7','6','5','4','3','2'] 
        
    def shuffle(self):
        random.shuffle(self.deck)
    def draw(self):
        drawdeck = self.deck
        card = drawdeck.pop()
        self.deck = drawdeck
        return card
    def getDeck(self):
        print (self.deck)
    def resetDeck(self):
        self.deck = ['A','K','Q','J','10','9','8','7','6','5'
                 ,'4','3','2','A','K','Q','J','10','9','8','7','6'
                 ,'5','4','3','2','A','K','Q','J','10','9','8'
                 ,'7','6','5','4','3','2','A','K','Q','J','10','9'
                 ,'8','7','6','5','4','3','2']


def Blackjack():
    hands = 2
    global play_deck
    global playertotal
    global dealertotal
    global list_of_hands
    global dealerdeck
    global PlayerAce
    global DealerAce
    play_deck = Deck()
    playertotal = 0
    dealertotal = 0 
    play_deck.shuffle()
    list_of_hands = []
    dealerdeck = []
    continueplaying = True
    PlayerAce = False
    DealerAce = False
    
    
    for i in range(hands):
        
        b = play_deck.draw()
        
        if b == 'A':
            list_of_hands.append(b)
            PlayerAce = True
        elif b == "K" or b == 'Q' or b == 'J':
            list_of_hands.append(b)
        else:
            list_of_hands.append(int(b))
        
        b = play_deck.draw()
        
        if b == 'A':
            dealerdeck.append(b)
            DealerAce = True
        elif b == "K" or b == 'Q' or b == 'J':
            dealerdeck.append(b)
        else:
            dealerdeck.append(int(b))
    
    
    
    print("Dealer's Card")
    print(dealerdeck[0])
    
    
    playnumber = 0
    #________________________________________________________________________________________________________________
    while (continueplaying):

        playertotal = 0
    
        
        for i in list_of_hands:
            if i == "A":
                playertotal += 11
            elif i == "K" or i == 'Q' or i == 'J':
                playertotal += 10
            else:
                playertotal += i
        
        if(playertotal > 21):
            if PlayerAce == True:
                playertotal -= 10
                
            else:
                break
        
        if playertotal == 21:
            break
        print('Player Hand: ')
        print(list_of_hands) 
        print("Player Total: " + str(playertotal))       
        if playnumber == 0:
            playtime = str(input('Type Hit, Stand, Double\n'))
        else:
            playtime = str(input('Type Hit, Stand\n'))
        
        if playtime == 'Hit':
            c = play_deck.draw()
            playnumber += 1
            if c == 'A':
                list_of_hands.append(c)
                PlayerAce = True
            elif c == "K" or c == 'Q' or c == 'J':
                list_of_hands.append(c)
            else:
                list_of_hands.append(int(c))
        
        elif playtime == 'Stand':
            continueplaying = False
        elif playtime == 'Double' and playnumber == 0:
            c = play_deck.draw()
            if c == 'A':
                list_of_hands.append(c)
                PlayerAce = True
            elif c == "K" or c == 'Q' or c == 'J':
                list_of_hands.append(c)
            else:
                list_of_hands.append(int(c))
            continueplaying = False
        
            
        else:
            playtime = ' '
    #_________________________________________________________________________________________________________________________
    playertotal = 0
  
    playertotal = getFinal_player_total(list_of_hands, playertotal, PlayerAce)
    
    dealertotal = getDealerTotal(dealerdeck, dealertotal)
    while dealertotal < 17:
        d = play_deck.draw()
        if d == 'A':
            dealertotal += 11
            dealerdeck.append(d)
            DealerAce = True
        elif d == "K" or d == 'Q' or d == 'J':
            dealertotal += 10
            dealerdeck.append(d)
        else:
            dealertotal += int(d)
            dealerdeck.append(int(d))
        if dealertotal > 21 and DealerAce == True:
            dealertotal -= 10
            DealerAce = False   
    
    print('Player Hand: ')
    print(list_of_hands)
    
    
    
    print('Dealer Hand: ')
    print(dealerdeck)
    
    print("")
    print("Player's Total: " + str(playertotal))
    print("")
    print("Dealers's Total: " + str(dealertotal))

    check_winner(playertotal, dealertotal)


def getFinal_player_total(list_of_hands, playertotal, PlayerAce):
  for i in list_of_hands:
      if i == "A":
        playertotal += 11
            
      elif i == "K" or i == 'Q' or i == 'J':
          playertotal += 10
      else:
          playertotal += i
      if playertotal > 21 and PlayerAce == True:
          playertotal -= 10
          PlayerAce = False  
  return playertotal

def check_winner(playertotal, dealertotal):
  if playertotal > 21:
    if dealertotal > 21:
        print('draw')
    else:
        print ('you lose')
  elif dealertotal > 21:
    print('you win')
  elif playertotal > dealertotal:
    print('you win')
  elif playertotal == dealertotal:
    print('Draw')
  else:
    print('you lose')
        
def getDealerTotal(dealerdeck,dealertotal): 
    for i in dealerdeck:
        if i == "A":
            dealertotal += 11
        elif i == "K" or i == 'Q' or i == 'J':
            dealertotal += 10
        else:
            dealertotal += i
    return dealertotal  








client.run('ODEyMzg2ODMyNTgzMDk4NDU5.YDAAMg.i9eGdQvW-YKs9dNWSbcvJLe2TtU')