import validators

def main():
    print(validate(input("What's your email address? ").strip().lower()))

def validate(email):
    validated = validators.email(email)

    if validated:
        return f"Valid"
    else:
        return f"Invalid"

if __name__ == "__main__":
    main()
