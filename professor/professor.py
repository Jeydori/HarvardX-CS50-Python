import random

def main():
    level = get_level()
    score = 0
    numbers = []

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        numbers.append(x)
        numbers.append(y)

        z = x + y
        tries = 3

        while tries > 0:
            try:
                answer = int(input(f"{x} + {y} = ").strip())
                if answer == z:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries -= 1

        if tries == 0:
            print(f"{x} + {y} = {z}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
