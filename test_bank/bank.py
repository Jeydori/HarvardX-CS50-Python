def main():
    greeting = []
    greeting = str(input("Type a greeting: ")).strip().lower()

    print(f"${value(greeting)}")

def value(greeting):
    answer = 0
    first_letter = greeting[:1]
    first_hello = greeting[:5]
    if first_hello == "hello":
        answer = 0
    elif first_letter == "h":
        answer = 20
    else:
        answer = 100

    return answer

if __name__ == "__main__":
    main()
