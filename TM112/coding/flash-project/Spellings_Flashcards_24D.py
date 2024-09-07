# Starter file for TM112 2024D TMA03 Q2

"""
This spelling flashcard program allows users to practice identifying correct spellings.
The program randomly selects a word pair from a dictionary of commonly misspelled words.
It displays both the correct and incorrect spellings in random order, labeled as A and B.
The user is then prompted to choose which spelling they believe is correct by entering
either A or B.

After the user makes their choice, the program informs them whether they were correct
or not. If incorrect, the program reveals the correct answer.

Users can repeatedly ask for new word pairs to practice with, and they also have the
option to quit the program at any time instead of seeing another word pair.
"""

from random import *

# IMPORTANT

# Q2 (a)(iii) Make changes only to

# -- the docstring for the program as a whole;

# -- the docstring of the show_flashcard() function;

# -- the body of the show_flashcard() function.

def show_flashcard():
    """
    Display a randomly selected word pair and prompt the user to choose
    the correct spelling.

    This function fetches a word pair from the global dictionary `words`,
    randomly determines the order in which the correct and incorrect spellings
    are shown, and prompts the user to identify the correct spelling by entering
    either 'A' or 'B'. It then provides feedback based on the user's input.
    """
    # Pick a random word pair from the dictionary
    random_key = choice(list(words.keys()))
    correct_word = random_key
    incorrect_word = words[random_key]
    
    # Randomly decide the order of the words
    if choice([True, False]):
        first_word = correct_word
        second_word = incorrect_word
        correct_answer = 'A'
    else:
        first_word = incorrect_word
        second_word = correct_word
        correct_answer = 'B'
    
    print(f"Which spelling is correct? A: {first_word} B: {second_word}")
    user_input = input("Enter A or B: ").strip().upper()
    
    if user_input == correct_answer:
        print("Well done!")
    else:
        print(f"Sorry, the correct answer is {correct_answer}: {correct_word}")

# Example usage
words = {'accommodate':'accomodate',
         'acquire':'aquire',
         'asthma':'athsma',
         'calendar':'calender',
         'cemetery':'cemetary',
         'consensus':'concensus',
         'exhilarating':'exilerating',
         'maintenance':'maintainance',
         'mischievous':'mischievious',
         'plagiarism': 'plagarism',
         'pronunciation':'pronounciation',
         'separate':'seperate'
        }
            
# The interactive loop
exit = False
while not exit:
    user_input = input('Enter s to show a word and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
