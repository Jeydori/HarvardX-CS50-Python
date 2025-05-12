months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    result = process()
    print(result)


def process():
    while True:
        try:
            raw_date = str(input("Date: ")).strip()
            date = raw_date.replace("/", " ").replace(", ", " ").split(" ")
            month, day, year = date

            if not (len(year) == 4):
                pass
            else:
                for m in months:
                    if day.isalpha():
                        pass
                    else:
                        if 0 < int(day) <= 30:
                            if month.isalpha():
                                if (raw_date == f"{month} {day}, {year}"):
                                    if month.capitalize() == m:
                                        month = str(months.index(m) + 1)
                                        if  len(month) == 1:
                                            month = "0" + month
                                            if len(day) == 1:
                                                day = "0" + day
                                                return f"{year}-{month}-{day}"
                                            else:
                                                return f"{year}-{month}-{day}"
                                        else:
                                            if len(day) == 1:
                                                day = "0" + day
                                                return f"{year}-{month}-{day}"
                                            else:
                                                return f"{year}-{month}-{day}"
                                    else:
                                        pass
                                else:
                                    pass
                            elif month.isnumeric():
                                if (raw_date == f"{month}/{day}/{year}"):
                                    if 0 < int(month) <= 12:
                                        if  len(month) == 1:
                                            month = "0" + month
                                            if len(day) == 1:
                                                day = "0" + day
                                                return f"{year}-{month}-{day}"
                                            else:
                                                return f"{year}-{month}-{day}"
                                        elif len(month) >= 2:
                                            if len(day) == 1:
                                                day = "0" + day
                                                return f"{year}-{month}-{day}"
                                            else:
                                                return f"{year}-{month}-{day}"
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass

        except (KeyError, ValueError):
            pass

if __name__ == "__main__":
    main()
