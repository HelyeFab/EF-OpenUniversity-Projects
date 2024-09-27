
# /question
class Sequence:
    """The sequence ADT."""
# question

    def capacity(self) -> float:
        """Return how many items the sequence can hold.

        Postconditions: if the capacity is only limited by memory,
        the output is math.inf,
        otherwise it's the non-negative integer set at creation time
        """
        pass

    def length(self) -> int:
        """Return the number of items in the sequence.

        Postconditions: 0 <= self.length() <= self.capacity()
        """
        pass

    def get_item(self, index: int) -> object:
        """Return the item at position index.

        Preconditions: 0 <= index < self.length()
        Postconditions: the output is the n-th item of self, with n = index + 1
        """
        pass

    def set_item(self, index: int, item: object) -> None:
        """Replace the item at position index with the given one.

        Preconditions: 0 <= index < self.length()
        Postconditions: post-self.get_item(index) == item
        """
        pass

    def insert(self, index: int, item: object) -> None:
        """Insert item at position index.

        Preconditions: 0 <= index <= self.length() < self.capacity()
        Postconditions: post-self is the sequence
        pre-self.get_item(0), ..., pre-self.get_item(index - 1),
        item, pre-self.get_item(index), ...,
        pre-self.get_item(pre-self.length() - 1)
        """
        pass

    def append(self, item: object) -> None:
        """Add item to the end of the sequence.

        Preconditions: self.length() < self.capacity()
        Postconditions: post-self is the sequence
        pre-self.get_item(0), ..., pre-self.get_item(pre-self.length() - 1), item
        """
        self.insert(self.length(), item)

    def remove(self, index: int) -> None:
        """Remove the item at the given index.

        Preconditions: 0 <= index < self.length()
        Postconditions: post-self is the sequence
        pre-self.get_item(0), ..., pre-self.get_item(index - 1),
        pre-self.get_item(index + 1), ...,
        pre-self.get_item(pre-self.length() - 1)
        """
        pass
# /question
# answer

    def has(self, item: object) -> bool:
        """Return True if and only if item is a member of self."""
        for index in range(self.length()):
            if self.get_item(index) == item:
                return True
        return False
# /answer
# question

    def __str__(self) -> str:
        """Return a string representation of the sequence.

        Postconditions: the output uses Python's syntax for lists
        """
        items = []
        for index in range(self.length()):
            items.append(self.get_item(index))
        return str(items)
# /question

def test_items(test: str, items: Sequence) -> None:
    """Check that items is the sequence 0, 1, 2, ..., length - 1."""
    for index in range(items.length()):
        check(test + ': n-th item',
            items.get_item(index), index, items)
    check(test + ': length <= capacity',
          items.length() <= items.capacity(), True, items)

def test_init(items: Sequence) -> None:
    """Check that items is the empty sequence."""
    check('init length', items.length(), 0, items)
    test_items('init', items)

def test_append(items: Sequence, length: int) -> None:
    """Check a sequence created with successive appends.

    Preconditions: items is empty; 0 <= length < items.capacity()
    """
    for number in range(length):
        items.append(number)
    test_items('append', items)

def test_insert_start(items: Sequence, length: int) -> None:
    """Check a sequence created by successive inserts at index 0.

    Preconditions: items is empty; 0 <= length <= items.capacity()
    """
    for number in range(length - 1, -1, -1):
        items.insert(0, number)
    test_items('insert at 0', items)

def test_set_item(items: Sequence, length: int) -> None:
    """Check a sequence created by replacing all items.

    Preconditions: items is empty; 0 <= length <= items.capacity()
    """
    for number in range(length):
        items.append(None)
    for number in range(length):
        items.set_item(number, number)
    test_items('set item', items)

def test_remove(items: Sequence, length: int) -> None:
    """Check removal at the start, middle and end of a sequence.

    Preconditions: items is empty; 0 <= length <= items.capacity()
    """
    for number in range(length):
        items.append(number)
    if length > 0:
        middle = length // 2
        items.remove(middle)
        check('length decreased', items.length(), length - 1, items)
        check('middle removed', items.has(middle), False, items)
    if items.has(0):            # if first number still exists
        pre_length = items.length()
        items.remove(0)
        check('length decreased', items.length(), pre_length - 1, items)
        check('first removed', items.has(0), False, items)
    if items.has(length - 1):   # if last number still exists
        pre_length = items.length()
        items.remove(items.length() - 1)
        check('length decreased', items.length(), pre_length - 1, items)
        check('last removed', items.has(length - 1), False, items)

import math

class ArraySequence(Sequence):
    """A dynamic array implementation of the sequence ADT."""

    def __init__(self):
        """Create an empty sequence."""
        self.items = DynamicArray(1)
        self.size = 0

    def capacity(self) -> float:
        return math.inf     # infinite capacity

    def length(self) -> int:
        return self.size

    def get_item(self, index: int) -> object:
        return self.items.get_item(index)

    def set_item(self, index: int, item: object) -> None:
        self.items.set_item(index, item)

    def insert(self, index: int, item: object) -> None:
        if self.size == self.items.length():    # array full
            self.items.resize(2 * self.size)    # double the capacity

        for position in range(self.size - 1, index - 1, -1):
            self.items.set_item(position + 1, self.items.get_item(position))
        self.items.set_item(index, item)
        self.size = self.size + 1
