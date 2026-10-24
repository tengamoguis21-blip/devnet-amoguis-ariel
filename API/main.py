import requests
import random
pokemon1 = requests.get("https://pokeapi.co/api/v2/pokemon/1")
name1 = pokemon1.json()['name']
height1  = pokemon1.json()['height']
weight1 = pokemon1.json()['weight']

pokemon2 = requests.get("https://pokeapi.co/api/v2/pokemon/4")
name2 = pokemon2.json()['name']
height2  = pokemon2.json()['height']
weight2 = pokemon2.json()['weight']  

pokemon3 = requests.get("https://pokeapi.co/api/v2/pokemon/6")
name3 = pokemon3.json()['name']
height3  = pokemon3.json()['height']
weight3 = pokemon3.json()['weight']  

pokemon4 = requests.get("https://pokeapi.co/api/v2/pokemon/7")
name4 = pokemon4.json()['name']
height4  = pokemon4.json()['height']
weight4 = pokemon4.json()['weight']  

pokemon5 = requests.get("https://pokeapi.co/api/v2/pokemon/25")
name5 = pokemon5.json()['name']
height5  = pokemon5.json()['height']
weight5 = pokemon5.json()['weight']  

pokemon_list = [
    [name1, height1, weight1],
    [name2, height2, weight2],
    [name3, height3, weight3],
    [name4, height4, weight4],
    [name5, height5, weight5],
]

random_pokemon = random.choices(pokemon_list)
print(random_pokemon)
print(f"Pokemon height is: {random_pokemon[0][1]}")
print(f"Pokemon weight is: {random_pokemon[0][2]}")

pokemon_to_guess = random_pokemon[0][0]

print(pokemon_to_guess)

print("Who's that Pokemon? Guess the pokemon to win, you only have 3 guess, goodluck!\n")

attempt = 1

while True:

    guess = input("Enter pokemon name to guess, enter 'q' to exit: ")
    print(f"Pokemon height is: {random_pokemon[0][1]}")
    print(f"Pokemon weight is: {random_pokemon[0][2]}")

    if guess == 'q':
        print("Exiting...")
        break
    elif guess == pokemon_to_guess:
        print("Correct! Nice one!")
    elif guess != pokemon_to_guess:
        print("Nah, try again")
        attempt += 1

        if attempt <4:
            continue
        else:
            print("\nNice try! ")
            print(f"The pokemon is {pokemon_to_guess}\n")
            attempt = 1
    else:
        print("Invalid input")
