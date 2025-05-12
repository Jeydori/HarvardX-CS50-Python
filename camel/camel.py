def main():
    camel_case = str(input("camelCase: ")).strip()
    snake_case = splitter(camel_case)
    print(snake_case)

def splitter(camel_case):
    result = ""
    for char in camel_case:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result

if __name__ == "__main__":
    main()
