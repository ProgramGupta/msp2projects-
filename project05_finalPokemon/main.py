import sys
import time
import random

# This is a function meant to slowly print a string
# This was copied from: https://www.codegrepper.com/code-examples/python/python+slow+print
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)



#Move Damage Output
move_damage = {
    'tackle': 4,
    'tail_whip': 0,
    'growl': 0,
    'scratch': 5,
    'nasty_plot': 0,
    'shock': 5,
    'whirlwind': 7,
    'gust': 4,
    'rock_throw': 7,
    'slam': 8
}

#Setup
party_members = []
number_of_pokeballs = 5
pokemon_in_battle = []
pokedollers = 500

# Enemy Trainer Teams
garys_team = []
trainer_2_team = ['Pikachu', 'Pidgey']
trainer_3_team = ['Squirtle', 'Charmander']
gym_trainer_1_team = ['Geodude']
gym_trainer_2_team = ['Oynx']
gym_leader_brock = ["Brocks_Geodude", "Brocks_Oynx"]

#pokemon
charmander = {
    "name" : 'charmander',
    "level": 0,
    'current_health': 10,
    'max_health': 10,
    'Move_1': 'scratch',
    'Move_2': 'growl'
}

squirtle = {
    "name" : 'squirtle',
    "level": 0,
    'current_health': 10,
    'max_health': 10,
    'Move_1': 'tackle',
    'Move_2': 'tail_whip'
}

bulbasaur = {
    "name" : 'bulbasaur',
    "level": 0,
    'current_health': 10,
    'max_health': 10,
    'Move_1': 'scratch',
    'Move_2': 'growl'
}

rattata = {
    "name" : 'rattata',
    "level": 0,
    'current_health': 25,
    'max_health': 25,
    'Move_1': 'scratch',
    'Move_2': 'nasty_plot'
}

pikachu = {
    "name" : 'pikachu',
    "level": 0,
    'current_health': 40,
    'max_health': 40,
    'Move_1': 'shock',
    'Move_2': 'tail_whip'
}

pidgey = {
    "name" : 'pidgey',
    "level": 0,
    'current_health': 25,
    'max_health': 25,
    'Move_1': 'whirlwind',
    'Move_2': 'gust'
}

geodude = {
    "name" : 'geodude',
    "level": 0,
    'current_health': 27,
    'max_health': 27,
    'Move_1': 'rock_throw',
    'Move_2': 'scratch'
}
oynx = {
    "name" : 'oynx',
    "level": 0,
    'current_health': 40,
    'max_health': 40,
    'Move_1': 'rock_throw',
    'Move_2': 'slam'
}




# Important Functions
def catch(n_pokeballs, pokemon, party_members):
    catch = input(
        f'You have {n_pokeballs} pokeballs do you want to catch the {pokemon} y/n '
    )
    if catch == 'y':
        party_members.append(pokemon)
        print(f'You cuahgt a {pokemon}!')
    return party_members


def wild_pokemon_battle(pokemon):
    return pokemon

def print_member_list(party_members):
     for party_member in party_members:
      print(party_member.get('name'))

  
def trainer_battle(trainer_name, opponent_name, party_members, opponent_party_members):
  slowprint(f'{trainer_name} vs. {opponent_name} ')
  while (party_members[0]['current_health'] > 0 
            and opponent_party_members[0]['current_health'] > 0):
  
    print_members(trainer_name, party_members)
    print_members(opponent_name, opponent_party_members)

    move1 = party_members[0]['Move_1']
    move2 = party_members[0]['Move_2']
    selected_move_1 = int(input(f' Which move would you like to use 1) {move1}; 2) {move2}; '))

    if selected_move_1 == 1:
          party_members_move = 'Move_1'
    else:
          party_members_move = 'Move_2'

                           
    selected_move_2 = random.randint(1,2)

    if selected_move_2 == 1:
          opponent_party_members_move = 'Move_1'
    else:
          opponent_party_members_move = 'Move_2'


    pokemon1 = party_members[0].get('name') 
    pokemon1_move =   party_members[0].get(party_members_move)
    pokemon1_move_damage = move_damage[pokemon1_move]
    
    slowprint(f'{trainer_name} {pokemon1}  used  {pokemon1_move} and delt {pokemon1_move_damage} points of damage!')
    
    pokemon2 = opponent_party_members[0].get('name')
    pokemon2_move =   opponent_party_members[0].get(opponent_party_members_move)
    pokemon2_move_damage = move_damage[pokemon2_move]        
    slowprint(f'{opponent_name}  {pokemon2}  used  {pokemon2_move} and delt {pokemon2_move_damage} points of damage!')      
    
    party_members[0]['current_health'] = party_members[0].get('current_health') - pokemon2_move_damage
    opponent_party_members[0]['current_health'] = opponent_party_members[0].get('current_health') - pokemon1_move_damage

    

  if party_members[0]['current_health'] > 0:
      slowprint("Congratulations on your win !")
  else:
      slowprint("Sorry you lost !")

                              
def heal(party_members):
    for party_member in party_members:
      pokemon_data[party_member['current_health']] = pokemon_data[party_member['max_health']]
      return party_members


def buy_pokeballs(poke_dollers, n_pokeballs):
    n_pokeballs_to_buy = input(
        f'How many pokeball do you want to buy you have {poke_dollers} pokedollers! Each pokeball costs 100 pokedollers; '
    )
    if n_pokeballs_to_buy * 100 > pokedollers:
        print("You don't have enough")
        return poke_dollers, n_pokeballs
    else:
        n_pokeballs += n_pokeballs_to_buy
        pokedollers -= n_pokeballs_to_buy * 100
    return poke_dollers, n_pokeballs

def print_members(name, members):
    for member in members:
      print (name,' pokemon ',member.get('name'),'has',member.get('current_health'),' HP')
      return 

def choose_action(party_members, pokemon_in_battle, n_pokeballs, pokemon,
                  poke_dollers):
    action = input(
        'What do you want to do? \n 1) Go battle on Route 1;\n 2) Catch pokemon on Route 1;\n 3) Heal Pokemon;\n 4) Buy Pokeballs'
    )
    if action == 1:
        pokemon_in_battle = trainer_battle(party_members, pokemon_in_battle)
    elif action == 2:
        party_members = catch(n_pokeballs, pokemon)
    elif action == 3:
        party_members = heal(party_members)
    elif action == 4:
        poke_dollers, n_pokeballs = buy_pokeballs(poke_dollers, n_pokeballs)


#start of Game/Choose Starter
slowprint(f'Hello! Welcome to the world of Pokemon!')
trainer_name = input(f'What is your name? ')
starter = input(
    f' What will your starter be?: (C)harmander, (S)quirtle, or (B)ulbasaur - '
)
if starter.lower() == 'c':
    slowprint("You selected Charmander")
    starter = charmander
elif starter.lower() == 's':
    slowprint("You selected Squirtle")
    starter = squirtle
else:
    slowprint("You selected Bulbasaur")
    starter = bulbasaur

party_members.append(starter)
#print_members(party_members)

# First Battle with Gary
slowprint(f'It is time for your first battle')

if party_members[0].get('name') == 'charmander':
    garys_team.append(squirtle)
elif party_members[0].get('name') == 'squirtle':
    garys_team.append(bulbasaur)
else:
    garys_team.append(charmander)

#print_members(garys_team)
trainer_battle(trainer_name, "Gary", party_members, garys_team)

slowprint(f'Congratluations you have completed your first battle!')

slowprint(
    f'Now you should make your way through veridian forest and get to Veridian City'
)
slowprint("I am gifting you 5 pokeballs and 500 Pokedollars!")

#Route 1
slowprint(
    'On your way to viridian city youll run into pokemon in patches of grass.')
slowprint(f'Entered Route 1')
pokemon_found = ['Pidgey', "Rattata", "Pikachu"]
for pokemon in pokemon_found:
    catch_or_battle = input(
        f"You have found a {pokemon} would you like to catch it : y/n ")
    if catch_or_battle == 'y':
        catch(n_pokeballs, pokemon, party_members)
    else:
        wild_pokemon_battle(pokemon)

#Trainer Battles on route 1
slowprint('On your way to Pewder_city you see some trainers on the path')
contiunue = input(
    f'Do you want to continue on the path or go back and heal; (c)ontinue or (h)eal '
)
if contiunue == c:
    trainer_battle(trainer_2_team)
else:
    for pokemon in party_members:
        current_health = 100
        slowprint('Now your party Members are healed')
        trainer_battle(trainer_2_team)

fight = True
while fight == True:
    go_to_gym = input(
        'Do you want to fight the gym leader or do something else?; 1) Fight Brock, 2)Something else'
    )
if go_to_gym == '2':
    choose_action(party_members, pokemon_in_battle, n_pokeballs, pokemon,
                  poke_dollers)

else:
    slowprint('You have chozen to fight the gym!')
    slowprint('Welcome to Pewder Gym!')
    trainer_battle(gym_trainer_1_team)
    heal()
    trainer_battle(gym_trainer_2_team)
    heal()
    trainer_battle(gym_leader_brock)
    heal()


slowprint(
    'Congratulations you have finished this portion of the game! Thanks for Playing'
)


