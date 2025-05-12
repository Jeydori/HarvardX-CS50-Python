
def main():
    print(convert())

def convert():
    names = []
    while True:
        try:
            name = str(input("Name: ")).strip().title()
            names.append(name)

        except EOFError:
            if len(names) > 2:
                last_name = names[-1]
                names.remove(last_name)
                return f"Adieu, adieu, to {", ".join(names)}, and {last_name}"
            elif len(names) == 2:
                return f"Adieu, adieu, to {" and ".join(names)}"
            else:
                return f"Adieu, adieu, to {name}"

if __name__ == "__main__":
    main()
