def main():
    time = input("What time is it (00:00)? ")
    converted = str(time).strip().split(":")
    time_hour = int(converted[0])
    time_minute = int(converted[-1])

    if not (0 <= time_hour < 24 and 0 <= time_minute < 60):
        print("Input a valid time in a 24-hour format")
        return

    result = convert(time)

    if 7.00 <= result <= 8.00:
        print("breakfast time")
    elif 12.00 <= result <= 13.00:
        print("lunch time")
    elif 18.00 <= result <= 19.00:
        print("dinner time")
    else:
        return


def convert(time):
    time_hour, time_minute = str(time).strip().split(":")
    time_hour, time_minute = float(time_hour), float(time_minute)
    minute = (time_minute/60)
    complete = time_hour + minute
    return complete


if __name__ == "__main__":
    main()
