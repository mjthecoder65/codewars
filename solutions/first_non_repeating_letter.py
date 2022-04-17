from collections import Counter

def first_non_repeating_letter(string: str):
    """Return the first non repeating character in a string"""
    temp = string.lower()
    counter = Counter(temp)

    for index, letter in enumerate(temp):
        if counter[letter] == 1:
            return string[index]
    
    return ""
        
