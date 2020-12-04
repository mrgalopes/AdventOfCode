from day2 import is_valid_password, is_valid_password_2

def test_valid():
    assert is_valid_password(1, 3, 'a', 'abcde') == True
    assert is_valid_password(1, 3, 'b', 'cdefg') == False
    assert is_valid_password(2, 9, 'c', 'ccccccccc') == True

def test_valid_2():
    assert is_valid_password_2(1, 3, 'a', 'abcde') == True
    assert is_valid_password_2(1, 3, 'b', 'cdefg') == False
    assert is_valid_password_2(2, 9, 'c', 'ccccccccc') == False
