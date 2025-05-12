import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^(?:<iframe).*src=\"https?://(?:www\.)?(youtube)\.com/embed/([a-z0-9]+)\".*(?:></iframe>)$", s, re.IGNORECASE)
    if matches:
        return f"https://{matches.group(1).removesuffix("be")}.be/{matches.group(2)}"
    else:
        return


if __name__ == "__main__":
    main()
