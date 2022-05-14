import random

def code_to_choice(n):
    '''it maps the choices to int'''
    if n == 0:
        return 'Rock'
    elif n == 1:
        return 'Paper'
    elif n == 2:
        return 'Scissor'
    elif n == 3:
        return 'Lizard'
    elif n == 4:
        return 'Spock'
    else:
        return 'Input Error'

def choice_to_code(s):
    ''' it converts number to name'''
    s = s.lower()
    if s == 'rock':
        return 0
    elif s == 'paper':
        return 1
    elif s == 'scissor':
        return 2
    elif s == 'lizard':
        return 3
    elif s == 'spock':
        return 4

def who_won(guess):
    ''' this will generate cpu choice and determine winner'''
    player_choice = choice_to_code(guess)
    cpu_choice = random.randrange(0,5)
    
    #compute cpu-winner modulo 5 now
    winner = (cpu_choice - player_choice)%5

    # using if/else to determine who won
    if winner < 3:
        player_win = False
    else:
        player_win = True
    print(cpu_choice)
    # convert cpu choice from number to name
    cpu_name = code_to_choice(cpu_choice)

    # print results
    print(f"You chose {guess}, CPU chose {cpu_name} ", end=" ")
    if player_win:
        print("You WON !!!")
    elif cpu_choice == player_choice:
        print("It's a Tie")
    else:
        print("CPU Wins :(")

player_guess = input("Enter your choice .. Options: rock, paper, scissor, lizard, spock\n")

who_won(str(player_guess))






