
def main():
    plate = str(input("Plate: ")).strip().upper()

    plate

    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    try:
        if ((s[0].isalpha() and s[1].isalpha())
            and (2 <= len(s) <= 6)
            and (digits_at_end(s) == True)
            and (special(s) == True)
            and (first_zero(s) == True)):
            return True

        else:
            return False
    except IndexError:
        return False

def digits_at_end(s):
    seen_digit = False
    for char in s:
        if char.isdigit():
            seen_digit = True
        elif seen_digit and char.isalpha():
            return False
    return True

def first_zero(num):
    num_str = ''.join(num)
    digits = ''.join([c for c in num_str if c.isdigit()])
    return not digits.startswith("0")

def special(s):
    for c in s:
        match c:
            case "," | "." | "/" | ";" | ":" | "'" | "!" | "@" | "#" | "$" | "%" | "^" | "&" | "*" | "-" | "_" | "+" | "|" | "?" | "<" | ">":
                return False
    return True

if __name__ == "__main__":
    main()
