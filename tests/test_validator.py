import sys
sys.path.insert(0, '.')

from src.validator import validate_email, validate_age

def test_valid_email():
    assert validate_email("test@example.com") == True

def test_invalid_email():
    assert validate_email("notanemail") == False

def test_validate_age():
    assert validate_age(20) == True
    assert validate_age(16) == False