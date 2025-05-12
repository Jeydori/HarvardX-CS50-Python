def main():
    i = str(input("Expression: ")).strip().split(" ")
    if not (len(i) == 3):
        print("Put some spaces")
        return
    
    y = i[1]
    x = int(i[0])
    z = int(i[-1])

    result = operation(x, y, z)
    print(result)

def operation(x, y, z):
    match y:
        case "+":
            result = float(x + z)
            return result
        case "-":
            result = float(x - z)
            return result
        case "/":
            result = float(x / z)
            return result
        case "*":
            result = float(x * z)
            return result
        case _:
            print("invalid operation!")
            return

main()

