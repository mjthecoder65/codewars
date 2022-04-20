from delete_nth import delete_nth 

def test_delete_nth():
    assert delete_nth([20,37,20,21], 1) == [20,37,21]
    assert delete_nth([1,1,3,3,7,2,2,2,2], 3) == [1, 1, 3, 3, 7, 2, 2, 2] 