WINNER = False
import gvt
def print_players(player, opponent):
    print(repr(opponent))
    print()
    print(repr(player))
def calculate_damage(player,opponent):
    attacking = 0
    for i in player.get_battalion():
        attacking += i.get_attack_power()
    while attacking > 0:
        for i in reversed(opponent.get_battalion()):
            if opponent.get_score() <= 0:
                break
            if i.get_health_points() < attacking:
                attacking -= i.get_health_points()
                i.set_health(0)
                opponent.discard(opponent.get_battalion().pop())
        if len(opponent.get_battalion()) == 0 and opponent.get_score() > 0:
            opponent.set_score(0 - attacking)  
            attacking = 0
def play_turn(player, opponent):
    player.start_turn()
    print_players(player, opponent)
    playing = True
    while playing == True:
        command = input(str(player) + " >> ")  # "P 2"
        tokens = command.split()  # ["P", "2"]
        if tokens:
            if tokens[0].upper() == "Q":
                calculate_damage(player,opponent)
                print(player.get_name(),"attacks",opponent.get_name())
                print("")
                if opponent.get_score() <= 0:
                    print(opponent.get_name(),"is defeated!",player.get_name(),"wins!")
                    WINNER = True
                else:
                    player.set_turn_num()
                    playing = False
            elif tokens[0].upper() == "H":
                if int(tokens[1]) <= len(player.get_hand()) and int(tokens[1]) != 0:
                    print(player.get_hand()[int(tokens[1])-1].__repr__())
                else:
                    print("Invalid Card")
            elif tokens[0].upper() == "B":
                if int(tokens[1]) <= len(player.get_battalion()) and int(tokens[1]) != 0:
                    print(player.get_battalion()[int(tokens[1])-1].__repr__())
                else:
                    print("Invalid Card")
            elif tokens[0].upper() == "E":
                if int(tokens[1]) <= len(opponent.get_battalion()) and int(tokens[1]) != 0:
                    print(opponent.get_battalion()[int(tokens[1])-1].__repr__())
                else:
                    print("Invalid Card")
            elif tokens[0].upper() == "I":
                print("H # - show a detailed string for the specified card in the player's hand. # is a number from 1-length.\nB # - show a detailed string for the specified card in the player's battalion. \nE # - show a detailed string for the specified card in the enemy player's battalion.\nP # - play the card from the player's hand. If the card is successfully played, print the detailed string representation for both players, otherwise print an error message.\nQ - end the player's turn. At this point, the player attacks the opposing player\nI - displays a list of available commands.")
            elif tokens[0].upper() == "P":
                number = int(tokens[1])
                if player.play_card(number)== True:
                    print_players(player, opponent)
                else:
                    print("Invalid card.")
            else:
                print("Invalid command.")
        else:
            print("Please enter a command or type I for a list of commands")
def main():
    p1_name = input("Enter player 1 name: ")
    player1 = gvt.Player(p1_name, gvt.make_deck("Goat"))

    p2_name = input("Enter player 2 name: ")
    player2 = gvt.Player(p2_name, gvt.make_deck("Troll"))

    player = player1
    opponent = player2

    # Repeat the following until one of the players is defeated.
    while WINNER == False:
        play_turn(player, opponent)
        temp = opponent
        opponent = player
        player = temp

if __name__ == "__main__":
    main()
