from datetime import date
import inflect
import sys


class convertToMinutes:
    def __init__(self, birthday):
        self.birthday = birthday
        self.today = date.today()

    def __str__(self):
        try:
            self.birthday = date.fromisoformat(self.birthday)
        except ValueError:
            sys.exit("Not a valid format.")

        min = (self.today-self.birthday).days * 24 * 60
        converter = inflect.engine().number_to_words
        return converter(min, andword="").capitalize()+" minutes"


def main():
    print(convertToMinutes(input("Date of Birth: ")))

if __name__ == "__main__":
    main()
