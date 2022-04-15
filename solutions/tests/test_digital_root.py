from digital_root import digital_root

def test_digital_root():
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2