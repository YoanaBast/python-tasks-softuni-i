import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

user_move = input('Choose [r]ock, [p]aper, or [s]cissors: ')

if user_move == 'r':
    user_move = rock
elif user_move == 'p':
    user_move = paper
elif user_move == 's':
    user_move = scissors
else:
    raise SystemExit('Invalid input. Please try again.')

pc_random_num = random.randint(1, 3)
pc_move = ''

if pc_random_num == 1:
    pc_move = rock
elif pc_random_num == 2:
    pc_move = paper
elif pc_random_num == 3:
    pc_move = scissors
print(f"The computer chose {pc_move}.")

if user_move == rock and pc_move == rock \
        or user_move == paper and pc_move == paper\
        or user_move == scissors and pc_move == scissors:
    print('Draw')
elif user_move == rock and pc_move == paper \
        or user_move == paper and pc_move == scissors \
        or user_move == scissors and pc_move == rock:
    print('You lose!')
elif user_move == rock and pc_move == scissors \
        or user_move == paper and pc_move == rock\
        or user_move == scissors and pc_move == paper:
    print('You win!')
