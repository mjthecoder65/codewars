from pangram import is_pangram

def test_pangram():
    pangram = "The quick, brown fox jumps over the lazy dog!"
    assert is_pangram(pangram) == True