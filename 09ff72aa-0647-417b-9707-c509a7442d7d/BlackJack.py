
import random

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
    play_deck = Deck()
    playertotal = 0
    dealertotal = 0
    incase = []
    play_deck.shuffle()
    list_of_hands = []
    dealerdeck = []
    continueplaying = True
    PlayerAce = False
    DealerAce = False
    
    channel = (813456023636672564)
    
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
    
    playertotal = 0
    
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
    

            secondtotal = 0
    
        
            for i in incase:
                if i == "A":
                    secondtotal += 11
                elif i == "K" or i == 'Q' or i == 'J':
                    secondtotal += 10
                else:
                    secondtotal += i
        
            if(secondtotal > 21):
                if PlayerAce == True:
                    secondtotal -= 10
                    PlayerAce = False
                
                else:
                    break
        
            if secondtotal == 21:
                break
            print('Player Hand: ')
            print(incase)        
            if playnumber == 0:
                playtime = str(input('Type Hit, Stand, or Double\n'))
            else:
                playtime = str(input('Type Hit, Stand\n'))
        
            if playtime == 'Hit':
                g = play_deck.draw()
                playnumber += 1
                if g == 'A':
                    incase.append(g)
                    PlayerAce = True
                elif g == "K" or g == 'Q' or g == 'J':
                    incase.append(g)
                else:
                    incase.append(int(g))
        
            elif playtime == 'Stand':
                continueplaying = False
            elif playtime == 'Double' and playnumber == 0:
                c = play_deck.draw()
                if c == 'A':
                    incase.append(c)
                    PlayerAce = True
                elif c == "K" or c == 'Q' or c == 'J':
                    incase.append(c)
                else:
                    incase.append(int(c))
                continueplaying = False
            else:
                playtime = ' '
    
        
    
   
     
    for i in dealerdeck:
        if i == "A":
            dealertotal += 11
        elif i == "K" or i == 'Q' or i == 'J':
            dealertotal += 10
        else:
            dealertotal += i
        
    
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
    print("Player's Total: " + str(dealertotal))
           
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
        
def Split(hand):
    if len(hand) != 2 or hand[0] != hand[1]:
        print ('Cannot Split')
        return False
    else:
        return True
