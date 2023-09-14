from gvt import *

def main():
    # card1 = Card("Hary","Goat",COMMON,5,3,7)
    # card2 = Card("Trollzord","Troll",RARE,6,12,18)
    # print(card1)
    # print(card2)

    # print(card2.get_health()) 
    # amount = card1.get_attack_power()
    # card2.damage(amount)
    # print(card2.get_health())
    # print(card2.is_concious())
    troll_deck = make_deck("Troll")
    goat_deck = make_deck("Goat")
    # print(troll_deck)
    # print(goat_deck)

    player = Player("Marisa",goat_deck)
    print(player.__repr__())
    
main()