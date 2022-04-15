from narcissistic import is_narcissistic


def test_narcissistic():
    assert is_narcissistic(153) == True
    assert is_narcissistic(201) == False
    assert is_narcissistic(259) == False
    assert is_narcissistic(371) == True
    assert is_narcissistic(407) == True
    assert is_narcissistic(595) == False
    assert is_narcissistic(825) == False
    assert is_narcissistic(1634) == True