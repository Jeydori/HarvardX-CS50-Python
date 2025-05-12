import sys

def main():
    if len(sys.argv) < 2:
        sys.exit(f"Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit(f"Too many command-line arguments")
    else:
        if sys.argv[1][-3:] == ".py":
            file_name = sys.argv[1]
            print(splitter(file_name))
        else:
            sys.exit(f"Not a Python file")

def splitter(file_name):
    count = 0
    try:
        with open(file_name) as file:
            file_read = file.readlines()
            for f in file_read:
                f_strip = f.strip()
                if not (f_strip == "" or f_strip.startswith("#")):
                    count += 1
                else:
                    continue

            return count

    except FileNotFoundError:
        sys.exit(f"File does not exist")


if __name__ == "__main__":
    main()
