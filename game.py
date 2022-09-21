human_turn = input('Input human turn: ')
computer_turn = input ('input computer turn: ')

if human_turn == computer_turn :
    print ('draw!')
elif human_turn == 'r' and computer_turn == 's':
    print('Human wins!')
elif human_turn == 'p' and computer_turn == 'r':
    print('Human wins!')
elif human_turn == 's' and computer_turn == 'p':
    print('Human wins!')
else:
        print('computer wins!')
