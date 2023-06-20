from itertools import *
from random import *


def print_deck(deck):
    for i in range(4):
        print(deck[i:i + 4])

def is_similar(a,b,c):
    sum = 0
    shape = set()
     = set()
    shape = set()
    shape = set()
    for i in range(3):





shape = ['◊', '~', 'O']
quantity = [1, 2, 3]
color = ['purple', 'green', 'red']
pattern = ['empty', 'striped', 'full']
deck = []
'''for card in product(shape, quantity, color, pattern):
    deck.append(card)'''
for i in shape:
    for j in quantity:
        for q in color:
            for z in pattern:
                deck.append((i, j, q, z))
shuffle(deck)
past_cards = []
future_cards = deck
present_cards = [('', 0, '', '')] * 12
for i in range(12):
    present_cards[i] = future_cards[i]
print(print_deck(present_cards))
a, b, c = map(int, input().split())
picked_cards = set()
picked_cards |= {a, b, c}
if len(picked_cards) == 3 and max(picked_cards) <= 12 and min(picked_cards) >= 1:
    print(present_cards[a - 1], present_cards[b - 1], present_cards[c - 1])

