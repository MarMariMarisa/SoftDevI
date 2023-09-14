import goatils
import random
COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    LEGENDARY : ORANGE + "L"}

class Card:
    __slots__ = ["__name","__cost","__rarity","__faction","__attack_power","__health_points"]
    def __init__(self,name,faction,rarity,cost,attack_power,health_points):
        self.__name = name
        self.__cost = cost
        self.__rarity = rarity
        self.__faction = faction
        self.__attack_power = attack_power
        self.__health_points = health_points

    def get_name(self):
        return self.__name
    def get_cost(self):
        return self.__cost
    def get_rarity(self):
        return self.__rarity
    def get_faction(self):
        return self.__faction
    def get_attack_power(self):
        return self.__attack_power
    def get_health_points(self):
        return self.__health_points
    def set_health(self,health):
        self.__health_points = health
    def __repr__(self):
        a_string = str(self.__name) + "\nRarity: " + RARITY_STRINGS[self.__rarity] +  RESET + "\nFaction: " + self.__faction + "\nResource Cost: " + str(self.__cost) + "\nAttack Power: " + str(self.__attack_power) + "\nHealth Points: " + str(self.__health_points)
        return a_string
    def __str__(self):
        return "[" + self.__faction[0] + self.__name[0] + " " + "{:02}".format(self.__cost) + " " +  "{:02}".format(self.__attack_power)  + " " + "{:02}".format(self.__health_points) + "]"

    def damage(self,amount):
        if amount < self.__health_points:
            self.__health_points -= amount
            return 0
        else:
            excess_damage = amount - self.__health_points
            self.__health_points = 0
            return excess_damage

    def is_concious(self):
        return self.__health > 0

    def __eq__(self,other):
        if type(self) == type(other):
            return self.__cost == other.__cost and self.__rarity == other.__rarity and \
                 self.__faction == other.__faction and self.__attack_power == other.__attack_power
        return False

    def __lt__(self,other):
        if type(self) == type(other):
            return self.__cost < other.__cost
        return False
class Player:
    slots = ["__name", "__score", "__max_resource_points",
    "__resource_points", "__deck", "__hand", "__battalion",
    "__discarded","__turn_num"]
    def __init__(self, name, deck):
        self.__name = name
        self.__score = 20
        self.__max_resource_points = 0
        self.__resource_points = self.__max_resource_points
        self.__deck = deck
        self.__hand = []
        self.__battalion = []
        self.__discarded = []
        self.__turn_num = 0
        for i in range(5):
            self.__hand.append(self.__deck.pop())
            self.__hand.sort()
    def set_score(self,score):
        self.__score += score
    def set_turn_num(self):
        if self.__turn_num < 10:
            self.__turn_num += 1
    def get_hand(self):
        return self.__hand
    def get_battalion(self):
        return self.__battalion
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def __str__(self):
        return "Player: " + self.__name
    def __repr__(self):
        hand_str = ""
        for value in self.__hand:
            hand_str += value.__str__()
        batallion_str = ""
        for value in self.__battalion:
            batallion_str += value.__str__()
        return  "Player: " + self.__name + "\nScore: " +str(self.__score) +  "\nResource Points: " + str(self.__resource_points) + "/" + str(self.__turn_num + 1) + "\nDeck: " + str(len(self.__deck)) + "\nDiscarded: " + str(len(self.__discarded)) + "\nBattalion: "  + batallion_str + "\nHand: "  + hand_str
    def start_turn(self):
        if self.__resource_points < 10 and self.__turn_num <= 10:
            self.__resource_points = self.__turn_num + 1
        else:
            self.__resource_points = 10
            self.__turn_num = 10
        self.__hand.append(self.__deck.pop())
        self.__hand.sort()
    def play_card(self,num):
        if self.__hand[num - 1].get_cost() <= self.__resource_points:
            self.__battalion.append(self.__hand[num - 1])
            self.__resource_points -= self.__hand[num - 1].get_cost()
            self.__hand.pop(num - 1)
            return True
        return False
    def discard(self,card):
        self.__discarded.insert(0,card)

TROLL_NAMES = ["Trollzord","Troll Jr","Troll Sr","Sr. Troll","St Troll","Trollina","Troll O'Riley","Troll Trollingson","Trolly","Rolly Trolly","Trolland"]
def make_card(faction,rarity):
    if faction == "Goat":
        name = goatils.make_goat_name()
    else:
        name = TROLL_NAMES[random.randint(0,len(TROLL_NAMES)) - 1]
    cost = 0
    attack_power = 0
    health = 0
    if rarity == COMMON:
        cost = random.randint(1,3)
        health = random.randint(1,8)
        attack_power = 8 - health
    elif rarity == UNCOMMON:
        cost = random.randint(2,5)
        health = random.randint(1,12)
        attack_power = 12 - health
    elif rarity == RARE:
        cost = random.randint(4,7)
        health = random.randint(1,15)
        attack_power = 15 - health
    elif rarity == LEGENDARY:
        cost = 10
        health = random.randint(16,24)
        attack_power = 24 - health
    else:
        print("Invalid Rarity")
        return
    return Card(name,faction,rarity,cost,attack_power,health)

def make_deck(faction):
    deck = []
    for i in range(20):
        deck.append(make_card(faction, COMMON))
    for i in range(10):
        deck.append(make_card(faction, UNCOMMON))
    for i in range(8):
        deck.append(make_card(faction, RARE))
    for i in range(2):
        deck.append(make_card(faction, LEGENDARY))
    random.shuffle(deck)
    return deck