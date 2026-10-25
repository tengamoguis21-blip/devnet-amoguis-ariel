import requests
import random
pokemon1 = requests.get("https://pokeapi.co/api/v2/pokemon/1")
name1 = pokemon1.json()['name']
height1  = pokemon1.json()['height']
weight1 = pokemon1.json()['weight']
pokemon1ablitiy1 = pokemon1.json()['abilities'][0]['ability']['name']
pokemon1ablitiy2 = pokemon1.json()['abilities'][1]['ability']['name']

pokemon2 = requests.get("https://pokeapi.co/api/v2/pokemon/4")
name2 = pokemon2.json()['name']
height2  = pokemon2.json()['height']
weight2 = pokemon2.json()['weight']
pokemon2ablitiy1 = pokemon2.json()['abilities'][0]['ability']['name']
pokemon2ablitiy2 = pokemon2.json()['abilities'][1]['ability']['name']  

pokemon3 = requests.get("https://pokeapi.co/api/v2/pokemon/6")
name3 = pokemon3.json()['name']
height3  = pokemon3.json()['height']
weight3 = pokemon3.json()['weight']  
pokemon3ablitiy1 = pokemon3.json()['abilities'][0]['ability']['name']
pokemon3ablitiy2 = pokemon3.json()['abilities'][1]['ability']['name']

pokemon4 = requests.get("https://pokeapi.co/api/v2/pokemon/7")
name4 = pokemon4.json()['name']
height4  = pokemon4.json()['height']
weight4 = pokemon4.json()['weight'] 
pokemon4ablitiy1 = pokemon4.json()['abilities'][0]['ability']['name']
pokemon4ablitiy2 = pokemon4.json()['abilities'][1]['ability']['name'] 

pokemon5 = requests.get("https://pokeapi.co/api/v2/pokemon/25")
name5 = pokemon5.json()['name']
height5  = pokemon5.json()['height']
weight5 = pokemon5.json()['weight']  
pokemon5ablitiy1 = pokemon5.json()['abilities'][0]['ability']['name']
pokemon5ablitiy2 = pokemon5.json()['abilities'][1]['ability']['name']

pokemon_list = [
    [name1, height1, weight1, pokemon1ablitiy1, pokemon1ablitiy2],
    [name2, height2, weight2, pokemon2ablitiy1, pokemon2ablitiy2],
    [name3, height3, weight3, pokemon3ablitiy1, pokemon3ablitiy2],
    [name4, height4, weight4, pokemon4ablitiy1, pokemon4ablitiy2],
    [name5, height5, weight5, pokemon5ablitiy1, pokemon5ablitiy2],
]

random_pokemon = random.choice(pokemon_list)
pokemon_to_guess = random_pokemon[0][0]

attempt = 1

def height_weight():
    print(f"\n height is: {random_pokemon[0][1]}")
    print(f"Pokemon weight is: {random_pokemon[0][2]}")

def abilities():
    print(f"Pokemon first ability is: {random_pokemon[0][3]}")
    print(f"Pokemon second ability is: {random_pokemon[0][4]}\n")

def menu():
    print("1: Play ")
    print("2: Exit ")

print("Who's that Pokemon? Guess the pokemon to win, you only have 3 guess, GOODLUCK!")

def play():
    global attempt
    abilities()
    while attempt != 4:

        guess = input("Enter pokemon name to guess, enter 'q' to exit: ")

        if guess == 'q':
            print("Exiting...")
            break
        elif guess == pokemon_to_guess:
            print("Correct! Nice one!")
            break
        elif guess != pokemon_to_guess:
            print("Nah, try again")
            attempt += 1

            if attempt == 2:
                height_weight()
                abilities()
                continue
            elif attempt == 3:
                print("Last chance to guess!")
                height_weight()
                abilities()
            else:
                print("\nNice try! ")
                print(f"The pokemon is {pokemon_to_guess}\n")

def main():
    global attempt, random_pokemon, pokemon_to_guess
    while True:
        menu()
        try:
            choice = int(input("Enter 1 or 2 > "))

        except ValueError:
            print("Invalid input! Please enter 1 or 2.\n")
            continue

        if choice == 1:
            random_pokemon = random.choice(pokemon_list)
            pokemon_to_guess = random_pokemon[0][0]
            attempt = 1
            play()

        elif choice == 2:
            break
        else:
            print("Invalid input. Enter 1 or 2")

main()