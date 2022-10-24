import random
random_index = random.randint(0,len(letters)-1)



#Setup
possible_pokemon = [
    'charmander'
    'squirtle'
    'bulbasaur'
    'rattata'
    'pikachu'
    'pidgey'
    'geodude'
    'oynx']


possible_moves = [
    'tackle'
    'tail_whip'
    'growl'
    'scratch'
    'nasty_plot'
    'shock'
    'whirlwind'
    'gust'
    'rock_throw'
    'slam'
]

pokedex = {}


#Functions
#Pokemon
def get_pokemon():
  random_pokemon_chosen = possible_pokemon[random_index]
  return 
#Move
def get_move():
  random_pokemon_move = possible_pokemon[random_index]
  return 

#Catch

def catch_pokemon(pokedex, pokemon_name,):
  print (f'You encounter a {pokemon_name}')
  catch = input(f'Do you want to catch {pokemon_name}!; y/n')
  if catch == 'y': 
    pass
  else: 
    continue
    
#Train
def train_pokemon(pokedex, pokemon_name, pokemon_move):
  for pokemon in pokedex:
    print(f"You're {pokemon} wants to learn {pokemon_move}")
    move = input (f'Will you allow it to learn this move; y/n')
    if move == 'y': 
      pokedex[pokemon] = random_pokemon_move
    else:
      continue
      
    
  
#Release
def release_pokemon(pokedex):
  release = input(f' Do you wish to release any of your pokemon?; y/n ')
  if release == 'y':
    for pokemon in pokedex:
      delete = input(f'Do you want to delete {pokemon} from pokedex; y/n ')
      if delete == 'y':
        del pokedex{pokemon}
      else:
        continue
  else:
    continue
  
#List them All!
def list_pokemon(pokedex):
  print(pokedex)


# Loop of Pokemon!
game = on
while game = on:
  pokemon_name = get_pokemon()
  print (f'You encounter a {pokemon_name}')
  catch_pokemon(pokedex, pokemon_name,):
  pokemon_move = get_move()
  
    release_pokemon(pokedex)

  
  
  
  
      
  







