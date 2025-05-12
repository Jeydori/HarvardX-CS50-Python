def main():
    greeting = []
    greeting = str(input("Type a greeting: ")).strip().lower()
    first_letter = greeting[:1]
    first_hello = greeting[:5]
    check(first_letter, first_hello)

def check(first_letter, first_hello):
    if first_hello == "hello":
        print(f"$0")
    elif first_letter == "h":
        print(f"$20")
    else:
        print(f"$100")

main()
