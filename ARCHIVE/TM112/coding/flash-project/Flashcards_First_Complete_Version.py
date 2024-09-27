# Flashcards_First_Complete_Version
""" This is a simple flashcard program that allows 
    the user to view flashcards and test themselves.
    A new flashcard is randomly selected each time the user presses the 's' key.
    The program runs until the user presses the 'q' key to exit.
"""

import random
import csv




# Create a dictionary containing the flashcards and their answers

def file_to_dictionary(filename):
    """ Return a dictionary with the contents of a file.
    """
    file = open(filename, 'r')
    reader = csv.reader(file)
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = row[1]
    return dictionary


# Create a dictionary to store the flashcards and their answers
flashcards = file_to_dictionary('data/TM112_Glossary.csv')

# Load flashcards from a file
def show_flashcard():
    """Display a random flashcard"""
    question, answer = random.choice(list(flashcards.items()))
    print("Define: " + question)
    input("Press Enter to see the answer...")
    print("Answer: " + answer)


def main():
    """Run the flashcard program"""
    print("Welcome to the Flashcard Program!")
    while True:
        choice = input("Press 's' to see a flashcard, 'q' to quit: ")
        if choice == 's':
            show_flashcard()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
