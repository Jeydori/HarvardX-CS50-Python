

def main():
    final = prompt()
    print("\n".join(final))



def prompt():
    lists = []
    result = []
    sorted_result = []

    while True:
        try:
            item = str(input()).strip().upper()
            lists.append(item)
            result = number(lists)
        except (ValueError, KeyError):
            pass
        except EOFError:
            sorted_result = sorted(result, key=lambda x: x.split()[1])
            return sorted_result

def number(lists):
    result = []
    for l in set(lists):
        num = lists.count(l)
        result.append(f"{num} {l}")
    return result


if __name__ == "__main__":
    main()
