import random

def gibErfolge(input: str) -> int:
  isEdged = '+' in input
  anzahlWürfel = bestimmeAnzahlWürfel(input, isEdged)
  anzahlBonusWürfel = 0
  anzahlErfolge = 0
  
  for würfel in range(anzahlWürfel):
    nummer = random.randint(1, 6)
    if (nummer >= 5):
      anzahlErfolge += 1
      if(nummer >= 6 and isEdged):
        anzahlBonusWürfel += 1

  while(anzahlBonusWürfel != 0):
    bonusAnzahl = anzahlBonusWürfel
    anzahlBonusWürfel = 0
    
    for würfel in range(bonusAnzahl):
      nummer = random.randint(1, 6)
      if (nummer >= 5):
        anzahlErfolge += 1
        if(nummer >= 6 and isEdged):
          anzahlBonusWürfel += 1
  
  return anzahlErfolge
  
def bestimmeAnzahlWürfel(input: str, isEdged: bool) -> int:
  anzahlWürfel = 0

  if(isEdged):
    anzahlArray = input.split('+')
    anzahlWürfel += int(anzahlArray[0])
    anzahlWürfel += int(anzahlArray[1])
  else:
    anzahlWürfel += int(input)

  return anzahlWürfel

def machLustigeNachricht(erfolge: int) -> str:
  nachricht = f'{erfolge} Erfolge'

  rng = random.randint(0, 6)

  if(rng == 0):
   nachricht = nachricht + ', super'
  if(rng == 1):
   nachricht = nachricht + ', ganz klasse'
  if(rng == 2):
   nachricht = nachricht + ', stark'
  if(rng == 3):
   nachricht = nachricht + ', wirklich was ganz Besonderes'
  if(rng == 4):
   nachricht = nachricht + ', toll gemacht'
  if(rng == 5):
   nachricht = nachricht + ', spitzenklasse'
  if(rng == 6):
   nachricht = nachricht + ', schwach'

  return nachricht