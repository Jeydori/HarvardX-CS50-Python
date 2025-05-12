def main():
    text = str(input("What is the answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()

    if not (text == "42" or text == "forty-two" or text == "forty two"):
        print("No")
    else:
        answer()

def answer():
    print("Yes")

main()
