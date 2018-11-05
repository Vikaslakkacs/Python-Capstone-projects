'''
Created on Oct 1, 2018
Game of rolling dice
Select how many players you want.
ask them to roll the dice.
For every round of dice program will ask you to quit the game.
Asks to reset the game or add a player and reset the game or add a player for the existing game.
@author: Lavikas
'''
'''importing packages'''
from random import randint
''' Create the players
Store it in a dictionary and inside the disctionary store it in a list with name points whether in or out'''
total_player={}
''' List of players to be stored in the list'''
players_list=[]
'''Boolean for add player'''
add_player=True
'''Inviting for the game and asking to start'''
print('Welcome to the game of dice\n')
start_game=input('Are you ready to start the game?(Y/N)')
'''When the user is ready we will start the game'''
if start_game.upper() == 'Y':
    host_name=input('Please enter your name:\n')
    players_list=[host_name]
    print('Welcome {}\n'.format(host_name))
    '''Add players'''
    check_add_play=input('Do you want to add the player?(Y/N)')
    print('\n')
    '''If he accepts to add the player'''
    if check_add_play.upper()=='Y':
        #While loop to add the players and when he says N then stop the loop#
        while add_player==True:
            player_name=input('Enter the player name')
            players_list +=[player_name]
            ask_add_player=input('Do you want to add another player(Y/N)')
            print('\n')
            if ask_add_player.upper() == 'Y':
                add_player=True
            elif ask_add_player.upper() == 'N':
                add_player=False
                print('Lets Start the game!')
                print('\n\n')

    else:
            print('Thanks for playing')
else:
    print('Quitting game Thank you! Visit again')

'''Lets start the game'''
        #Giving summary of the list of players
'''list_of_players=''
for num_player in players_list:
    list_of_players +=','+num_player
print('Players are {}'.format(list_of_players.lstrip(',')))
'''
'''Rolling the dice start'''
roll_dice=input('Do you want to roll the dice (Y/N)')
in_game=True
'''Continue the game untill they tell to end the game'''
while in_game==True:
    for player in players_list:
        roll_player_dice=input('\nPress any key to Roll dice to {}'.format(player))
        domino_num=randint(1,6)
        print('Dice number {domino} for {name}'.format(domino=domino_num,name=player))
    repeat=input('\nDo you want to Roll the dice again? (Y/N)')
    if repeat.upper()=='N':
        in_game=False#End game
print('Thanks for Playing!')