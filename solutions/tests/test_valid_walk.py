from valid_walk import is_valid_walk


def test_is_valid_walk():
    assert is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True
    assert is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False
    assert is_valid_walk(['w']) == False
    assert is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False
    