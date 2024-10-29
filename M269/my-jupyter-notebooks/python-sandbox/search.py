def first_index(text: str, character: str) -> int:
    """Return the lowest index of character in text.

    Preconditions: len(character) = 1
    Postconditions: if text includes character, then the output is
    the lowest index such that text[index] = character,
    otherwise the output is len(text)
    """
    for index in range(len(text)):
        if text[index] == character:
            return index
    return len(text)










print(first_index('abracadabra', 'd'))


