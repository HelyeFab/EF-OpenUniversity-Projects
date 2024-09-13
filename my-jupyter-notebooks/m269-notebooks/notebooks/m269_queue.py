
class Queue:
    """A last-in, first-out sequence of objects, implemented with a linked list."""

    class Node:
        """A node in a linked list."""

        def __init__(self, item: object):
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self):
        """Initialise the queue to be empty."""
        self.head = None
        self.last = None
        self.length = 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return self.length

    def front(self) -> object:
        """Return the item at the front of the queue.

        Preconditions: self.size() > 0
        """
        return self.head.item

    def enqueue(self, item) -> None:
        """Add item to the back of the queue."""
        node = Queue.Node(item)
        if self.length == 0:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length = self.length + 1

    def dequeue(self):
        """Remove and return the item at the front of the queue.

        Preconditions: self.size() > 0
        """
        item = self.front()
        self.head = self.head.next
        if self.head == None:
            self.last = None
        self.length = self.length - 1
        return item
