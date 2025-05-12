import random

def main():
    while True:
        try:

            level = int(input("Level: ").strip())
            if level > 0:
                print(guess(level))
                break
            else:
                pass

        except ValueError:
            pass

def guess(level):

    generated_num = random.randint(1, level)

    while True:
        try:
            guessed_num = int(input("Guess: ").strip())

            if guessed_num == generated_num:
                return f"Just right!"
            elif guessed_num > generated_num:
                print(f"Too large!")
                pass
            else:
                if guessed_num < 0:
                    pass
                else:
                    print(f"Too small!")
                    pass

        except ValueError:
            pass

if __name__ == "__main__":
    main()
