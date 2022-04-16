def insertion_sort(array):
    """Sort list of comparable elements into nondecreasing order."""

    for i in range(1, len(array)):
        current = array[i]
        j = i

        while j > 0 and array[j-1] > current:
            array[j] = array[j-1]
            j -= 1
        
        array[j] = current

        