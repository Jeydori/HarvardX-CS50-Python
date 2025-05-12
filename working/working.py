import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(hours):
    matches = re.search(r"^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$", hours, re.IGNORECASE)

    if matches:
        if matches.group(3) == "AM":
            matches_1 = matches.group(1)
            if matches_1 == "12":
                matches_1 = f"00"
            else:
                matches_1 = matches_1
        else:
            if matches.group(1) == "12":
                matches_1 = matches.group(1)
            else:
                matches_1 = int(matches.group(1)) + 12

        if matches.group(6) == "AM":
            matches_4 = matches.group(4)
            if matches_4 == "12":
                matches_4 = f"00"
            else:
                matches_4 = matches_4
        else:
            if matches.group(4) == "12":
                matches_4 = matches.group(4)
            else:
                matches_4 = int(matches.group(4)) + 12

        if len(str(matches_1)) == 2:
            matches_1 = matches_1
        else:
            matches_1 = f"0{matches_1}"

        if len(str(matches_4)) == 2:
            matches_4 = matches_4
        else:
            matches_4 = f"0{matches_4}"

        try:
            if len(matches.group(2)) == 2:
                matches_2 = matches.group(2)

        except TypeError:
            matches_2 = f"00"

        try:
            if len(matches.group(5)) == 2:
                matches_5 = matches.group(5)

        except TypeError:
            matches_5 = f"00"

        return f"{matches_1}:{matches_2} to {matches_4}:{matches_5}"
    else:
        raise(ValueError)
if __name__ == "__main__":
    main()
