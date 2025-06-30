import re

common_passwords = [
    "123456", "123456789", "12345678", "12345", "1234567",
    "password", "123123", "000000",  "abc123",
    "1q2w3e4r", "admin", "letmein", "welcome1", "qwerty123",
    "passw0rd", "login", "user", "test", "default",
    "admin123", "admin@123", "root", "123qwe", "P@ssw0rd"
]


def analyze_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append(" Consider using more than 12 characters.")
    else:
        feedback.append(" Password is too short! Minimum 8 characters.")
    
    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append(" Add uppercase letters.")

    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(" Add lowercase letters.")
    
    # Digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append(" Add numbers (0-9).")
    
    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append(" Add special characters like !@#.")

    # Common password check
    if password.lower() in common_passwords:
        score = 0
        feedback = [" This is a common password! Avoid using it."]

    # Final result
    if score >= 6:
        strength = "💪 Very Strong"
    elif score >= 4:
        strength = "✅ Strong"
    elif score >= 2:
        strength = "⚠️ Weak"
    else:
        strength = "❌ Very Weak"

    return strength, feedback
