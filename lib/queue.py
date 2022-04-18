
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class ArrayQueue:
    """FIFO queue implementation using a Python list as a underlying storage"""

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self): # O(1)
        """Return the number of elements in the queue"""
        return self._size
    
    def is_empty(self): # O(1)
        """Return True if Queue is empty"""
        return self._size == 0
    
    def first(self): # O(1)
        """Return (but do not remove) the element at the front of the stack
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
    def dequeue(self): # O(1) -> Amortized
        """Remove and return the first element of the queue 
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]

        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, element): # O(1) -> Amortized
        """Add an element to the back of the queue"""

        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1

    def _resize(self, capacity):
        """Resize a new list of capacity >= len(self) """

        old = self._data
        self._data = [None] * capacity
        index = self._front
        for k in range(self._size):
            self._data[k] = old[index]
            index = (1 + index) % len(old)
        
        self._front = 0

