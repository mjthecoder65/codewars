"""
Using Adapter Pattern to implement stack.

Stack                     List  
S.push(element)           L.append(element)
S.pop()                   L.pop()
S.top()                   L[-1]
S.is_empty()              len(L) == 0
len(S)                    len(L)

"""


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """LIFO Stack implementation using Python list as underlying storage"""

    def __init__(self):
        """create an empty stack"""
        self._data = []

    def __len__(self): # O(1)
        """Return the number of elements in the stack"""
        return len(self._data)
    
    def is_empty(self): # O(1)
        """Return True if the stack is empty"""
        return len(self._data) == 0
    
    def push(self, element): # O(1) -> Amortized
        """Add element to the top of the stack"""
        self._data.append(element)

    def top(self): # O(1)
        """Return (but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    def pop(self): # O(1) -> Amortized
        """Remove and the return the element from the top of the stack
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

# Problem: To be implemented.

# Reverse items of the sequences
# Matching parenthesis
# Matching parenthesis and HTML tags
