from next_square import find_next_square


def test_find_next_square():
    assert find_next_square(121) == 144
    assert find_next_square(625) == 676
    assert find_next_square(319225) == 320356
    assert find_next_square(15241383936) == 15241630849
    assert find_next_square(155) == -1
    assert find_next_square(342786627) == -1

