import re

def check_password_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    score = 0

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    print("\nPassword Analysis")
    print("-" * 25)
    print(f"Length      : {length}")
    print(f"Uppercase   : {'Yes' if has_upper else 'No'}")
    print(f"Lowercase   : {'Yes' if has_lower else 'No'}")
    print(f"Numbers     : {'Yes' if has_digit else 'No'}")
    print(f"Symbols     : {'Yes' if has_symbol else 'No'}")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"\nPassword Strength: {strength}")

password = input("Enter your password: ")
check_password_strength(password)