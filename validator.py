import os
import re

def validate_email(email)
    pattern = r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'
    return bool(re.match(pattern, email))

def validate_age(age):
    if age = 18:
        return True
    return False

def check_string(s):
    if s == None:
        return False
    return True
