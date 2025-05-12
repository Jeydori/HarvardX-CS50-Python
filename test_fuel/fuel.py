number = ""

def main():
    number = str(input("Fraction: ")).strip()
    result = convert(number)
    print(gauge(result))

def convert(number):

    while True:
        try:
            x, y = number.split("/")
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

def gauge(result):
    if result <= 1:
        return f"E"
    elif 100 >= result >= 99:
        return f"F"
    else:
        return f"{result}%"


if __name__ == "__main__":
    main()
