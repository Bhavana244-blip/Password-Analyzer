from password_analyzer import analyze_password

def main():
    print(" Welcome to Password Strength Checker")
    password = input("Enter your password: ")

    strength, feedback = analyze_password(password)

    print(f"\nStrength: {strength}")
    print("Feedback:")
    for item in feedback:
        print(f" - {item}")

if __name__ == "__main__":
    main()
