def convert(input):
    input = input.replace(":)", "🙂").replace(":(", "🙁")
    return input

def main():
    user_input = input("Input a text with smiley: ").strip()
    result = convert(user_input)

    print(f"{result}")

main()
