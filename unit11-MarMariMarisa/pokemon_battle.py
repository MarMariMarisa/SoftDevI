import pokedex
import pokemon
def battle(party_1,party_2,round_num = 1):
    print("Roumd:",round)
    print("Party One:")
    for elt in party_1:
        print("\t",str(elt))
    print("Party Two:")
    for elt in party_2:
        print("\t",str(elt))
    pokemon_1 = party_1.pop()
    pokemon_2 = party_2.pop()
    
    print(str(pokemon_1),"is battling",str(pokemon_2))
    if pokemon_1 > pokemon_2:
        print(pokemon_1,"has won the battle!")
        party_1.add(pokemon_1)
        print(pokemon_2,"has been defeated and loses",pokemon_1.get_damage_points(),"health points")
        pokemon_2.lose_round(pokemon_1.get_damage_points())
        if pokemon_2.is_fainted() == True:
            print(pokemon_2, "has been knocked out!")
        else:
            party_2.add(pokemon_2)
    
    if pokemon_1 < pokemon_2:
        print(pokemon_2,"has won the battle!")
        party_2.add(pokemon_2)
        print(pokemon_1,"has been defeated and loses",pokemon_2.get_damage_points(),"health points")
        pokemon_1.lose_round(pokemon_2.get_damage_points())
        if pokemon_1.is_fainted() == True:
            print(pokemon_1, "has been knocked out!")
        else:
            party_1.add(pokemon_1)

    if pokemon_2 == pokemon_1:
        print(pokemon_1,"and",pokemon_2),"have battled to a draw!"
        party_2.add(pokemon_2)
        party_1.add(pokemon_1)
    
    if len(party_1) == 0:
        print("Party 2 has won!")
        for elt in party_2:
            print("\t",str(elt))
    elif len(party_2) == 0:
        print("Party 1 has won!")
        for elt in party_1:
            print("\t",str(elt))
    else:
        input("Enter to continue battling!")
        battle(party_1,party_2,round_num +1)

def main():
    poke_dex = pokedex.Pokedex()
    poke_dex.load("data/pokemon.csv")
    party_1,party_2 = poke_dex.create_parties()
    battle(party_1,party_2)

main()
