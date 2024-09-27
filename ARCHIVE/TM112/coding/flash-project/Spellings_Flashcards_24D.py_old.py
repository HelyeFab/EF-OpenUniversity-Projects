# Starter file for TM112 2024D TMA03 Q2

"""
This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks an entry from all glossary
entries. It shows the entry. After the user presses return, the
program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program instead of seeing
another entry.
"""

from random import *

# IMPORTANT

# Q2 (a)(iii) Make changes only to

# -- the docstring for the program as a whole;

# -- the docstring of the show_flashcard() function;

# -- the body of the show_flashcard() function.

def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    random_key = choice(list(words))
    print('Define:', random_key)
    input('Press return to see the definition')
    print(words[random_key])

# Set up the dictionary

words =    {'accommodate':'accomodate',
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
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
                       
