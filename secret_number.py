import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print("Sorry! Too low.")
        elif guess > random_number:
            print("Whoops! Too high.")
    print(f"Hooray! You have guessed the random number {random_number}!")
    
def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high: 
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Huzzah! I have secured victory by guessing your number {x}")
              
guess(50)

comp_guess(1000)