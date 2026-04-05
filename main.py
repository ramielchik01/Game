import random
def TestYourLuck():
  RandomNumber = random.randint(1, 100)
  Tries = 0
  while Tries < 7:
    UserNumber = int(input("Write Your Number:"))
    Tries += 1
    if UserNumber == RandomNumber:
     print('You get it')
     break;
    elif UserNumber < RandomNumber:
      print('a little bit more, mate')
    else:
      print('a little bit less, dude')
  print(f'Sorry bro you loose, correct answer was {RandomNumber}')
TestYourLuck()
def PlayGames():
  while True:
    TestYourLuck()
    Question = input('Do you want play a game y/n')
    if Question == 'n':
      break;
PlayGames()