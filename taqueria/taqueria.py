taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    item()


def add(list):
    total = 0
    for i in list:
        price = taqueria.get(i)
        total += price

    return total

def item():
    order = []

    while True:
        try:
            items = str(input("Item: ")).strip().title()
            order.append(items)
            total = add(order)
            print(f"${total:.2f}\n", end = "")

        except EOFError:
            print()
            break
        except (KeyError, ValueError, TypeError):
            pass

if __name__ == "__main__":
    main()
