import random

# word_list = ["ardvark", "baboon", "camel"]

import Hangman_art , Hangman_words
from Hangman_words import word_list
from Hangman_art import logo , stages
# from Hangman_art import stages


lives = 6
# print(Hangman_art.logo)
print(logo)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# chosen_word = random.choice(Hangman_words.word_list)
chosen_word = random.choice(word_list)
# print(chosen_word)

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

#for char in chosen_word:
for _ in chosen_word:
    display += '_'

# for char in range(len(chosen_word)):
#     display += '_'
#     # display[char] = '_'


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

end_of_game = False
# end_of_game = True
# while end_of_game:
while not end_of_game:
    guess = input("Guess a letter?\t").lower()
    
    if guess in display:
        print(f'You already guessed that letter! {guess}')

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    for i in range (len(chosen_word)):
        if (guess == chosen_word[i]):
            display[i] = guess
                 

    # for letter in chosen_word:
    #     if (letter == guess):
    #         display = letter   
            
    if guess not in chosen_word:
        print(f"You gussesd {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            # end_of_game = False
            end_of_game = True
            print("YOU LOOOSSSEEEE!!!!!!!!!!!!!!!!!!!!")

    #TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    print(' '.join(display))    # The join() method basically is used to join the input string by another set of separator/string elements. It accepts iterables such as set, list, tuple, string, etc and another string(separable element) as parameters.

    if '_' not in display:
        end_of_game = True
        # end_of_game = False
        print("YOU WIN")


    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(stages[lives])