import emoji

def main():
    text = str(input("Input: ")).strip()
    print(f"Output: {convert(text)}")

def convert(text):
    try:
        for n in text:
            if n == "_":
                new_text = emoji.emojize(text)
            else:
                new_text = emoji.emojize(text, language='alias')

        return new_text
    except KeyError:
        print("KeyError")
        pass

if __name__ == "__main__":
    main()
