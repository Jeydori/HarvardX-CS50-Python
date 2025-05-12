
def rmv(letter):
    match letter:
        case "a":
            removed = letter.replace("a", "")
            return removed
        case "e":
            removed = letter.replace("e", "")
            return removed
        case "i":
            removed = letter.replace("i", "")
            return removed
        case "o":
            removed = letter.replace("o", "")
            return removed
        case "u":
            removed = letter.replace("u", "")
            return removed
        case "A":
            removed = letter.replace("A", "")
            return removed
        case "E":
            removed = letter.replace("E", "")
            return removed
        case "I":
            removed = letter.replace("I", "")
            return removed
        case "O":
            removed = letter.replace("O", "")
            return removed
        case "U":
            removed = letter.replace("U", "")
            return removed
        case _:
            return letter

def main():
    text = str(input("Input: ").strip())

    shortened = shorten(text)

    print(f"Output: " + shortened)

def shorten(text):
    shortened_chars = []

    chars = list(text)

    for char in chars:
        extracted = rmv(char)
        shortened_chars.append(extracted)

    return "".join(shortened_chars)

if __name__ == "__main__":
    main()
