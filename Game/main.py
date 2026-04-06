students = {
  'Manjari Ramiel':{
    'name':"Ramiel",
    'surname':"Manjari",
    'class':'10f',
    'grades': [5, 5, 5, 5]
  },
  'Salimli Maqa':{
    'name':"Maqa",
    'surname':"Salimli",
    'class':'10f',
    'grades': [5, 5, 4, 5]
  },
  'Huseyn Kerimli':{
    'name':"Huseyn",
    'surname':"Kerimli",
    'class':'10f',
    'grades': [3, 3, 4, 5]
  }
}
students['Aliyev Aladdin'] = {'name':'Aladdin',"surname":'Aliyev','class':'10f','grades': [3, 3, 3, 4]}

def FindStudent(data, name):
  search = data.get(name)
  if search:
    return f'We find student {name}'
  else:
    return 'we could not recognize'
def MeanScore(data, name):
  mean = data.get(name)
  if mean and 'grades' in students:
    scores = students['grades']
    average = sum(scores) / len(scores)
  else:
    "we did not find such student"
print(students)
print(FindStudent(students, "Ramiel"))
print(f'mean score of {'name'}:{MeanScore(students, 'Maqa')} ')

# task2





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