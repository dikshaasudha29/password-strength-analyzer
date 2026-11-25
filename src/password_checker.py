
# Password Strength Checker

def check_password(password):

    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    score = 0

    # Check password length
    if length >= 8:
        score += 1

    # Check uppercase letters
    if has_uppercase:
        score += 1

    # Check numbers
    if has_digit:
        score += 1

    # Check special symbols
    if has_symbol:
        score += 1

    # Classify password strength
    if length < 8:
        strength = "Weak"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print("\n----- PASSWORD ANALYSIS -----")
    print("Password Length:", length)
    print("Contains Uppercase:", has_uppercase)
    print("Contains Number:", has_digit)
    print("Contains Symbol:", has_symbol)
    print("Strength:", strength)


# Main program
password = input("Enter your password: ")
check_password(password)
