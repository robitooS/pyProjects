import random
import os

bot, player = 0, 0
moves = ['Papel', 'Pedra', 'Tesoura']

def getPlayerMove():
    while True:
        player_move = int(input('Escolha sua jogada:\n\n0 - Papel\n1 - Pedra\n2 - Tesoura\n'))
        if player_move not in [0, 1, 2]:
            print('O número selecionado não serve, tente 0, 1 ou 2')
        else:
            return moves[player_move]
            
def getBotMove():
    return random.choice(moves)

while True:

    print('\n==================================\n')
    print('PONTUAÇÃO:\n\nBOT : {}\nPLAYER : {}\n'.format(bot, player))

    player_move = getPlayerMove()
    bot_move = getBotMove()
    os.system('cls')

    print(f'\nO PLAYER escolheu {player_move}')
    print(f'O BOT escolheu {bot_move}')


    if player_move == 'Pedra':
        
        if bot_move == 'Tesoura':
            player += 1
            print('\nO PLAYER Ganhou !')

        elif bot_move == 'Pedra':
            print('\nEmpate! Ninguém ganhou :D')

        elif bot_move == 'Papel':
            bot += 1
            print('\nO BOT Ganhou!')

    elif player_move == 'Tesoura':

        if bot_move == 'Tesoura':
            print('\nEmpate! Ninguém ganhou :D')

        elif bot_move == 'Pedra':
            bot += 1
            print('\nO BOT Ganhou!')

        elif bot_move == 'Papel':
            player += 1 
            print('\nO PLAYER Ganhou !')

    elif player_move == 'Papel':

        if bot_move == 'Tesoura':
            bot += 1
            print('\nO BOT Ganhou!')

        elif bot_move == 'Pedra':
            player += 1
            print('\nO PLAYER Ganhou !')

        elif bot_move == 'Papel':
            print('\nEmpate! Ninguém ganhou :D')

    print('\n==================================\n')
    print('PONTUAÇÃO:\n\nBOT : {}\nPLAYER : {}\n'.format(bot, player))
    
    print('Você deseja continuar? \n0 - Não \n1 - Sim ')
    choice = int(input())
    os.system('cls')

    if choice == 0:
        break