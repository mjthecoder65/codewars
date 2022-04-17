def is_pangram(string: str):
    """Return true if a string contain every letter of alphabet at least one"""
    string = set(string.lower())
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in string:
            return False

    return True
