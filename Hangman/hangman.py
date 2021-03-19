import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list of words.
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has already guessed
    
    lives = 7
    
    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Incorrect guess.")

        elif user_letter in used_letters:
            print("You've already guessed that.")

        else:
            print("Invalid input.")
            
    # Gets here once all the letters have been guessed
    if lives == 0:
        print("")
        print("Sorry sucker, you're dead! the word was", word)
    else:
        print('You guessed the word', word, '!!')

    
user_input = input('Guess a letter: ').upper()

hangman()