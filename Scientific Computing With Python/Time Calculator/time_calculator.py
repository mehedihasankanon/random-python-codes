def get_day(time):
    ans = 0
    while time > 24 * 60:
        ans += 1
        time -= 24 * 60
    return ans


def add_time(start, duration, weekday=""):

    days = [
        "saturday",
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
    ]
    days_better = [
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
    ]

    day_num = 0
    if weekday:
        while weekday.lower() != days[day_num]:
            day_num += 1

    init_time, period = start.split(" ")
    init_hr, init_min = init_time.split(":")

    add_hr, add_min = duration.split(":")

    init = 12 * 60 * (period == "PM") + int(init_hr) * 60 + int(init_min)
    add = int(add_hr) * 60 + int(add_min)

    ans = init + add
    day = get_day(ans)

    ans -= 24 * 60 * day
    new = "AM"
    if ans > 12 * 60:
        ans -= 12 * 60
        new = "PM"

    last_hr = ans // 60
    if last_hr == 0:
        last_hr += 12
    last_min = ans % 60

    last_day = day_num
    day_num += day
    day_num %= 7

    hr_str = str(last_hr)
    min_str = "0" + str(last_min) if last_min < 10 else str(last_min)

    new_str = hr_str + ":" + min_str + " " + new
    if weekday:
        new_str += ", " + days_better[day_num]

    if day:
        if day_num == 1:
            new_str += " (next day)"
        else:
            new_str += f" ({day} days later)"

    new_time = "".join([new_str])

    return new_time


def main():
    print("Time Calculator")
    print("Starting time format: HH:MM AM")
    start = input("Enter a time: ")
    print("Duration time format: HH:MM")
    duration = input("Enter duration: ")

    add_day = input("Wanna add weekday? (y/n): ").lower() == "y"
    if add_day:
        weekday = input("Enter weekday: ")
    else:
        weekday = ""

    print(add_time(start, duration, weekday))


main()
