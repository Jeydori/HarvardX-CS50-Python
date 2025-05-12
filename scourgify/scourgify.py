import sys
import csv

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        if (sys.argv[1][-3:] == "csv") and (sys.argv[2][-3:] == "csv"):
            readnwrite(sys.argv[1], sys.argv[2])
        else:
            sys.exit("File is not a csv file")

def readnwrite(file_input, file_output):
    try:
        with open(file_input, "r") as csv_file_input, open(file_output, "w") as csv_file_output:
            file_read = csv.DictReader(csv_file_input)
            file_write = csv.DictWriter(csv_file_output, fieldnames=["first", "last", "house"])
            file_write.writeheader()

            for row in file_read:
                name = row["name"]
                last, first = name.split(", ")
                house = row["house"]
                file_write.writerow(
                    {
                        "first": first,
                        "last": last,
                        "house": house
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
