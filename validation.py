import re


def validate_name(name: str) -> bool:
    return bool(re.match(r"^[a-zA-Z\s]+$", name))

def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)) # the re.match could return none so we wrap it with bool to return true or false

def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^(01[0125]\d{8})$", phone))

def validate_password(password: str) -> bool:
    return len(password) >= 8