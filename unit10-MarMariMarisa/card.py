class Card:
    #static fields, part of the class
    suit = ""
    rank = 0
    attr = []

card1 = Card()
card1.append(10)
print(card1.attr)
card2 = Card()
card2.attr.append(20)
print(card2.attr)