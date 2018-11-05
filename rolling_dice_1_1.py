'''
Created on Oct 4, 2018
In this program we are creating rolling dice game using functions
@author: LAVIKAS
'''
'''Getting the Host details and host name'''
def player_details():
    add_player=True
    players_list=[]
    host_name=input('Please enter your name:\n')
    players_list.append(host_name)
    print('Welcome {}\n'.format(host_name))
    '''Add players'''
    check_add_play=input('Do you want to add the player?(Y/N)')
    print('\n')
    '''If he accepts to add the player'''
    if check_add_play.upper()=='Y':
        #While loop to add the players and when he says N then stop the loop#
        while add_player==True:
            player_name=input('Enter the player name')
            players_list.append(player_name)
            ask_add_player=input('Do you want to add another player(Y/N)')
            print('\n')
            if ask_add_player.upper() == 'Y':
                add_player=True
            elif ask_add_player.upper() == 'N':
                add_player=False
                print('Lets Start the game!')
                print('\n\n')
    '''Returning the list of players'''
    return players_list
'''Function for rolling the dice
Input:players_list
'''
def roll_dice(players_list):
    from random import randint
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
            
            
            
'''Function to add the player'''
def add_player(players_list):
    bool_add_player = True
    while bool_add_player==True:
        player=input('Please enter the players name')
        players_list.append(player)
        add_player=input('Do you want to add player?(Y/N)')
        print('\n')
        if add_player.upper() == 'Y':
            bool_add_player=True
        elif add_player.upper() == 'N':
            bool_add_player=False
            print('Lets Start the game!')
            print('\n\n')   
    players_list1=players_list 
    return players_list1
    
    
    
'''Starting the code for the game'''
'''Inviting for the game and asking to start'''
play_game= False
players_list=[]
print('Welcome to the game of dice\n')
start_game=input('Are you ready to start the game?(Y/N)')


'''When the user is ready we will start the game'''
if start_game.upper() == 'Y':
    players_list=player_details()
    
    '''Asking the players to enter atleast two ppl to play the game'''
    while play_game==False:
        if players_list.__len__() >1:
            play_game = True
        else:
            print('Not enough players,Please enter more than one player to play the game ')
            players_list=add_player(players_list)
else:
    print('Quitting game Thank you! Visit again')

'''Asking to roll the dice again'''
roll_dice(players_list)
print('Thanks for Playing. Please play again!')