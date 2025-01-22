answer = ''

while True:

    if answer in ('2','no','No', 'NO'):
        print('Goodbye!')
        break

    import random

    comp_number = random.randint(1, 100)

    while True:
        user_guess = input('Guess the number (1-100): ')

        if not user_guess.isdigit():
            print('Invalid input. Please enter a number!')
            continue

        user_guess = int(user_guess)

        if user_guess == comp_number:
            print('You guessed it! Yay!')
            break

        elif user_guess > comp_number:
            print('Too high!')
        else:
            print('Too low!')

    print('Play again?')
    print("Select your answer:")
    print("1. Yes")
    print("2. No")
    answer = input()

    if answer in ('2','no','No', 'NO'):
        print('Goodbye!')
        break

    elif answer in ('1','yes','Yes', 'YES', 'yea', 'Yea', 'YEA', 'yeah', 'Yeah', 'YEAH', 'ok', 'Ok', 'OK',
                    'okay', 'Okay', 'OKAY', 'sure', 'Sure', 'SURE'):
        continue

    else:
        print("I didn't understand that!")
        print('(☉_ ☉)')
        print('')
        print('Play again?')
        print("Select your answer:")
        print("1. Yes")
        print("2. No")
        answer = input()