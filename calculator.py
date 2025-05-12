def main():
    x = input("input 2: ")
    squares = square(x)
    print(squares)

def square(input):
    if 2 in input:
        return input**2
    else:
        return "That's not 2"

main()
