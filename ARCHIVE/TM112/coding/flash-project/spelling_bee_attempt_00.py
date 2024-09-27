# Starter file for TM112 2024D TMA03 Q2

"""
This spelling flashcard program allows the user to practice identifying correct spellings.
The program randomly selects a word pair from a dictionary
of commonly misspelled words. It displays both the correct and incorrect spellings in
random order, labelled as A and B. The user is then prompted to choose which spelling
they believe is correct by entering either A or B.

After the user makes their choice, the program informs them whether they were correct
or not. If incorrect, the program reveals the correct answer.

The user can repeatedly ask for new word pairs to practice with, and also has the
option to quit the program at any time instead of seeing another word pair.
"""

from random import *

# IMPORTANT

# Q2 (a)(iii) Make changes only to

# -- the docstring for the program as a whole;

# -- the docstring of the show_flashcard() function;

# -- the body of the show_flashcard() function.


def pick_random_word_pair(words_dict):
    """
    Randomly selects and returns a word pair from the given dictionary.

    This function takes a dictionary where keys are correct spellings
    and values are corresponding common misspellings. It randomly
    chooses one key-value pair and returns it as a list.

    Parameters:
    words_dict (dict): A dictionary of correct spellings (keys) 
                       and their common misspellings (values).

    Returns:
    list: A randomly selected [correct_spelling, misspelling] pair.
    """
    random_key = choice(list(words_dict.keys()))
    return [random_key, words_dict[random_key]]

def show_word_pair():
    """ 
    Show the user a random word pair and ask them
    to choose the correct spelling.
    """
    word_pair = pick_random_word_pair(words)
    correct_word = word_pair[0]
    incorrect_word = word_pair[1]
    
    # Randomly decide which word to show first
    if choice([True, False]):
        first_word = correct_word
        second_word = incorrect_word
        correct_answer = 'A'
    else:
        first_word = incorrect_word
        second_word = correct_word
        correct_answer = 'B'
    
    print('Which spelling is right? A ' + first_word + ' B ' + second_word)
    user_input = input('Enter A or B: ')
    
    if user_input.upper() == correct_answer:
        print("Well done!")
    else:
        print("Sorry, the answer is " + correct_answer)
        
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
        print('Thanks for playing! Come back soon!')
        exit = True
    elif user_input == 's':
        show_word_pair()
    else:
        print('You need to enter either q or s.')
                       
