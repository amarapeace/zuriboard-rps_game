from random import choice
exit = False

while exit == False:
    choices=['R','P','S']
    user_input=input('Choose either R for Rock, P for Paper or S for Scissors: ')
    computer_input=(choice(choices))


    if user_input == 'R':
        if computer_input == 'R':
            print('Player(Rock):CPU(Rock)')
            print('A tie')
            exit = False   #Try again
        elif computer_input =='S':
            print('Player(Rock):CPU(Scissors)')
            print('Player wins')
            exit = True    
        elif computer_input =='P':
            print('Player(Rock):CPU(Paper)')
            print('CPU wins')
            exit = True
                
    elif user_input == 'P':
        if computer_input == 'P':
            print('Player(Paper):CPU(Paper)')
            print('A tie')
            exit = False   #Try again
        elif computer_input == 'R':
            print('Player(Paper):CPU(Rock)')
            print('Player wins')
            exit = True    
        elif computer_input =='S':
            print('Player(Paper):CPU(Scissors)')
            print('CPU wins')
            exit = True

    elif user_input == 'S':
        if computer_input == 'S':
            print('Player(Scissors):CPU(Scissors)')
            print('A tie')
            exit = False    #Try again
        elif computer_input =='P':
            print('Player(Scissors):CPU(Paper)')
            print('Player wins')
            exit = True
        elif computer_input =='R':
            print('Player(Scissors):CPU(Rock)')
            print('CPU wins')
            exit = True    

    else:
        print('Invalid entry')
        exit = False    #Try again


    
