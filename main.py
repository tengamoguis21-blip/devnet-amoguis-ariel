import requests
import random
pokemon1 = requests.get("https://pokeapi.co/api/v2/pokemon/1")
pokemon2 = requests.get("https://pokeapi.co/api/v2/pokemon/4")
pokemon3 = requests.get("https://pokeapi.co/api/v2/pokemon/6")
pokemon4 = requests.get("https://pokeapi.co/api/v2/pokemon/7")
pokemon5 = requests.get("https://pokeapi.co/api/v2/pokemon/25")


name1 = pokemon1.json()['name']
height1  = pokemon1.json()['height']
weight1 = pokemon1.json()['weight']  

name2 = pokemon2.json()['name']
height2  = pokemon2.json()['height']
weight2 = pokemon2.json()['weight']  

name3 = pokemon3.json()['name']
height3  = pokemon3.json()['height']
weight3 = pokemon3.json()['weight']  

name4 = pokemon4.json()['name']
height4  = pokemon4.json()['height']
weight4 = pokemon4.json()['weight']  

name5 = pokemon5.json()['name']
height5  = pokemon5.json()['height']
weight5 = pokemon5.json()['weight']  


# print(f'Name: {name1}')
# print(f'Height: {height1}')
# print(f'Weight: {weight1}')

pokemon_list = [name1, name2, name3, name4, name5]

random_pokemon = random.choices(pokemon_list)

print("Who's that Pokemon? Guess the pokemon to win, you only have 3 guess, goodluck!")
