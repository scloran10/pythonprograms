#!/usr/bin/env python3

if __name__ == '__main__':
    import itertools, random

    print("Creating pack of cards ...")
    deck = list(itertools.product(range(1, 14), ['S', 'H', 'D', 'C']))
    print("Shuffling and Dealing ... ")
    random.shuffle(deck)
    length = len(deck)
    hand1 = deck[:13]
    hand2 = deck[13:26]
    hand3 = deck[26:39]
    hand4 = deck[39:52]
    print(length)
    print(deck)
    print("Four Hands ...")
    print("Hand 1 --> ", hand1)
    print("Hand 2 --> ", hand2)
    print("Hand 3 --> ", hand3)
    print("Hand 4 --> ", hand4)
