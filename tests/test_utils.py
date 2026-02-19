import sys
sys.path.insert(0, '.')

from src.utils import add_numbers, get_user

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_get_user():
    user = get_user("Alice")
    assert user["name"] == "Alice"
    assert user["active"] == True

def test_process_list():
    from src.utils import process_list
    result = process_list([1, 2, 3])
    assert len(result) == 3
