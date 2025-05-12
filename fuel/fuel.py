number = ""

def main():
    result = convert(number)

    if result <= 1:
        print(f"E")
    elif 100 >= result >= 99:
        print(f"F")
    else:
        print(f"{result}%")


def convert(number):

    while True:
        try:
            number = str(input("Fraction: ")).strip().split("/")
            x, y = number
            x = int(x)
            y = int(y)
            div = round((x / y), 2) * 100
            div = int(div)

            if div > 100:
                pass
            else:
                return div

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()
