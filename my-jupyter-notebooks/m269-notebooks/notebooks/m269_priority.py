
class ArrayPriorityQueue:
# question

    """A dynamic array implementation of a fair max-priority queue.

    Items with the same priority are retrieved in FIFO order.
    """

    def __init__(self):
        """Create a new empty priority queue."""
        self.priorities = []    # in ascending order
        self.items = []

    def length(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)

    def find_max(self) -> object:
        """Return the oldest item with the highest priority.

        Preconditions: self.length() > 0
        """
        return self.items[-1]

    def remove_max(self) -> None:
        """Remove the oldest item with the highest priority.

        Preconditions: self.length() > 0
        """
        self.items.pop(-1)
        self.priorities.pop(-1)
# /question

    def insert(self, item: object, priority: object) -> None:
        # question
        """Add item with the given priority to the queue.

        Preconditions:
        - priority is comparable to the priorities of all existing items
        """
        index = 0
        # compute the index where to insert the item
        # /question
        # answer
        index = 0
        while index < len(self.priorities) and self.priorities[index] < priority:
            index = index + 1
        # /answer
        self.items.insert(index, item)
        self.priorities.insert(index, priority)
