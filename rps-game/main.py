from random import choice

choices=['R','P','S']
user_input=input('Choose R for Rock, P for Paper or S for Scissors: ')
computer_input=(choice(choices))

if user_input == 'R':
    if computer_input == 'R':
        print('You chose R and computer chose R too')
        print('A tie')
    elif computer_input =='S':
        print('You chose R and computer chose S')
        print('User wins')
    elif computer_input =='P':
        print('You chose R and computer chose P')
        print('Computer wins')
elif user_input == 'P':
    if computer_input == 'P':
        print('You chose P and computer chose P too')
        print('A tie')
    elif computer_input =='S':
        print('You chose P and computer chose S')
        print('User wins')
    elif computer_input =='R':
        print('You chose P and computer chose R')
        print('Computer wins')
elif user_input == 'S':
    if computer_input == 'S':
        print('You chose S and computer chose S too')
        print('A tie')
    elif computer_input =='P':
        print('You chose S and computer chose P')
        print('User wins')
    elif computer_input =='R':
        print('You chose S and computer chose R')
        print('Computer wins')
else:
    print('Invalid entry')

    
