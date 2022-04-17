from max_subarray_sum import max_sequence

def test_max_sequence():
    assert max_sequence([]) == 0
    assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6