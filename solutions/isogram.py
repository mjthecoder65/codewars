def is_isogram(string: str):
    string = string.upper()

    checkpoint = set()

    for letter in string:
        if letter in checkpoint:
            return False
        checkpoint.add(letter)
    
    return True

# Optimal solutioin.