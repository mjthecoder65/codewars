import ctypes

class DynamicArray:

    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array"""
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._size
    
    def __getitem__(self, k):
        """Return element at index k."""
        if 0 <= k < self._size:
            raise IndexError("Invalid index")
        return self._A[k]

    def append(self, value):
        """Add object to the end of the array"""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._size] = value
        self._size += 1
    def _resize(self, c):
        """Resize internal array to a capacity of size c"""
        B = self._make_array(c)
        for k in range(self._size):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()


# Demostrating dynamism of a Python list
import sys

data = []

for i in range(40):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b) )
    data.append(None)