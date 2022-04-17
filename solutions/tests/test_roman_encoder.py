from roman_encoder import solution

def test_roman_encoder():
    assert solution(1) == 'I' 
    assert solution(4) == 'IV'
    assert solution(6) == 'VI'
    assert solution(14) == 'XIV' 
    assert solution(21) == 'XXI'
    assert solution(89) == 'LXXXIX'
    assert solution(91) == 'XCI'
    assert solution(984) == 'CMLXXXIV'
    assert solution(1000) == 'M'
    assert solution(1889) == 'MDCCCLXXXIX'
    assert solution(1989) == 'MCMLXXXIX'
