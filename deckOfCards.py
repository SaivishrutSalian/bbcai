import random

cardFaces = []
deck = []
Royals = ['J','K','Q','A']
Suits = ['Hearts','Spades','Clubs','Diamonds']

for i in range(2,11):
    cardFaces.append(str(i))

for j in range(4):
    cardFaces.append(Royals[j])


for k in range(4):
    for x in range(13):
        card = (cardFaces[x] + " Of " + Suits[k])
        deck.append(card)

random.shuffle(deck)
for m in range(52):
    print(deck[m])

    