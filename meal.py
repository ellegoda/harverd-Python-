def main():
    time_input = input("Enter the time in 24-hour format (HH:MM): ")

    time_in_hours = convert(time_input)

    if 7.0 <= time_in_hours <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= time_in_hours <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= time_in_hours <= 19.0:
        print("It's dinner time!")


def convert(time):
    hours, minutes = map(int, time.split(':'))

    return hours + minutes / 60.0


if __name__ == "__main__":
    main()
