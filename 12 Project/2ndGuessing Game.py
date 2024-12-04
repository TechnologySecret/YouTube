# In this program we are create a small game where, where fight between one Computer and human. 

import random 

def guess(x): 
    random_num = random.randint(1, x)
    guess = 0 

    while guess  != random_num:
        guess = int (input(f'Guess a number between 1 and x {x}: '))
        if guess< random_num:
            print(" Sorry ,guess again. Too low.")
        elif guess > random_num:
            print("Sorry , guess again. Tow High")

    print(f'Yay!, Congrats.You have guess the number is {random_num}, Hurry Correctly. ') 


def computer_ges(x):
    low =1 
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess= random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H),  too low (L) , or correct (C)?? :- ')
        if feedback == 'h':
            high= guess -1
        elif feedback == 'l':
            low = guess +1

        print(f'Yay! The Computer guessed your number, {guess}, correctly! ')

computer_ges(10)




