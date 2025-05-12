import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1][-4:] == ".csv":
            file_name = sys.argv[1]
            rows, headers = tabulator(file_name)
            print(tabulate(rows, headers = "keys", tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")

def tabulator(file_name):
    rows = []
    try:
        with open(file_name) as csv_file:
            file_read = csv.DictReader(csv_file)
            headers = file_read.fieldnames
            for row in file_read:
                rows.append(row)

            return rows, headers

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
