import random
import csv
import json
import requests 
from bs4 import BeautifulSoup
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
def MeanScore(data, full_name):
  student = data.get(full_name)
  if student and 'grades' in students:
    scores = students['grades']
    return sum(scores) / len(scores)
  return "we did not find such student"
print(students)
print(FindStudent(students, "Ramiel"))
print(f"mean score of Maqa:{MeanScore(students, 'Salimli Maqa')} ")

# task2

def TestYourLuck():
  RandomNumber = random.randint(1, 100)
  Tries = 0
  winning = False
  while Tries < 7:
    UserNumber = int(input("Write Your Number:"))
    Tries += 1
    if UserNumber == RandomNumber:
     print('You get it')
     winning = True
     break
    elif UserNumber < RandomNumber:
      print('a little bit more, mate')
    else:
      print('a little bit less, dude')
  if not winning:
    print(f'Sorry bro you loose, correct answer was {RandomNumber}')
TestYourLuck()
def PlayGames():
  while True:
    TestYourLuck()
    Question = input('Do you want play a game y/n')
    if Question == 'n':
      break;
PlayGames()
# task 3
products = [
  ['product', 'category', ' price', 'data', 'count'],
  ['laptop', 'technology', 1000, '2025-10-06', 50],
  ['phone', 'technology', 300, '2024-03-21', 60],
  ['tabel', 'furniture', 100, '2023-12-19', 322]
]
sales = {}
products[0].append('revenue')
for row in products[1:]:
  price = row[2]
  count = row[4]
  row.append(price * count)
for row in products[1:]:
  category = row[1]
  revenue = row[5]
  sales[category] = sales.get(category, 0) + revenue
bestOne = products[1]
for row in products[2:]:
  if row[5] > bestOne[5:]:
    bestOne = row
newData = [['category', 'revenue']]
for category, total in sales.items():
  newData.append9([category, total])
with open('newData.csv', 'w', newline='', encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerows(newData)
jsonData = []
all = products[0]
for row in products[1:]:
  item=dict(zip(all, row))
  jsonData.append(item)
with open('data.json', 'w',encoding='utf-8') as f:
  json.dump(jsonData, f, indent=4, ensure_ascii=False)
  

with open('products_updated.csv', 'w', newline='' ,encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerows(products)
print('file ready','sales', sales)
print(f"The best sell one:{bestOne[0]}(income: {bestOne[5]})")
print("you can see the data in 'products_updated.csv' ")
# task 4
url = ' http://books.toscrape.com'
answer = requests.get(url)
if answer.status_code == 200:
  html = answer.text
soup = BeautifulSoup(html, 'lxml')
