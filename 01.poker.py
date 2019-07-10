# -*- coding: UTF-8 -*-

import random
import codecs
import copy
# ------------
cardJokers = ('♚', '♔')
cardMarks = ('♠', '♥', '♦', '♣')
cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')
# ------------
list = []
for i in cardJokers:
    list.append(i)

for n in cardNumbers:
    for m in cardMarks:
        Cards = n + m
        list.append(Cards)
# -------------
print('--debug: Create my list, total cards is %d, detail is :\n%s' %
      (len(list), list))
# -------------
f = codecs.open('list-poker.txt', 'w', 'utf-8')
for Cards in list:
    f.write(Cards)
    f.write('\t')
f.close()
# -----------------------------
'''
shuffledList = []
count = len(list)
for i in range(count):
    pickedCards = random.choice(list)
    shuffledList.append(pickedCards)
    list.remove(pickedCards)
'''
shuffledList = copy.copy(list)
random.shuffle(shuffledList)
print('--debug: Shuffled my list,remained cards is %d, detail is : \n%s' %
      (len(list), list))
print('--debug: Shuffled my list,new List cards is %d, detail is : \n%s' %
      (len(shuffledList), shuffledList))
f = codecs.open('list-shuffled.txt', 'w', 'utf-8')
for Cards in shuffledList:
    f.write(Cards)
    f.write('\n')
f.close()

numOfPlayers = 3
cardsForPlayers = int(len(shuffledList)/numOfPlayers)

player1 = []
for i in range(cardsForPlayers):
    pickedCards = random.choice(shuffledList)
    player1.append(pickedCards)
    shuffledList.remove(pickedCards)

player2 = []
for i in range(cardsForPlayers):
    pickedCards = random.choice(shuffledList)
    player1.append(pickedCards)
    shuffledList.remove(pickedCards)

player3 = []
for cards in shuffledList:
    player3.append(Cards)
