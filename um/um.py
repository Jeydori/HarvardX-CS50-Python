import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)

    if matches:
        return len(matches)
    else:
        return

if __name__ == "__main__":
    main()
