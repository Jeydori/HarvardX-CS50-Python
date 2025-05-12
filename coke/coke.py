

def main():

    amount_due = 50

    while amount_due > 0:
        coin = int(input("Insert a coin: ").strip())

        if coin in [25, 10, 5]:
            if coin >= amount_due:
                change = coin - amount_due
                print(f"Change Owed: {change}")
                break
            else:
                amount_due = amount_due - coin
                print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {amount_due}")


if __name__ == "__main__":
    main()
