def main():

    try:
        fruit = str(input("Item: ")).strip().lower().split(" ")
        fruit = "".join(fruit)
    except ValueError:
        pass

    cal = calories(fruit)

    if calories(fruit) != None:
        print(f"Calories: {cal}")
    else:
        return


def calories(fruit):
    match fruit:
        case "apple":
            return 130
        case "avocado":
            return 50
        case "banana":
            return 110
        case "cantaloupe":
            return 50
        case "grapefruit":
            return 60
        case "grapes":
            return 90
        case "honeydewmelon":
            return 50
        case "kiwifruit":
            return 90
        case "lemon":
            return 15
        case "lime":
            return 20
        case "nectarine":
            return 60
        case "orange":
            return 80
        case "peach":
            return 60
        case "pear":
            return 100
        case "pineapple":
            return 50
        case "plums":
            return 70
        case "strawberries":
            return 50
        case "sweetcherries":
            return 100
        case "tangerine":
            return 50
        case "watermelon":
            return 80
        case _:
            return

if __name__ == "__main__":
    main()
