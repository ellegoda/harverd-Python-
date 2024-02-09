def main():
    while True:
        date = input("Date: ")

        if "/" in date:
            s = date.split("/")
            if len(s) == 3:
                try:
                    year = int(s[2])
                    month = int(s[0])
                    day = int(s[1])

                    if month > 12:
                        continue

                    if day > 31:
                        continue

                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
                except:
                    continue
            else:
                continue
        elif " " in date:
            s = date.split(" ")
            if len(s) == 3:
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

                try:
                    month = months.index(s[0]) + 1
                    year = int(s[2])

                    if "," not in s[1]:
                        continue

                    day = int(s[1].replace(",", ""))

                    if month > 12:
                        continue

                    if day > 31:
                        continue

                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
                except:
                    continue
            else:
                continue
        else:
            continue


main()
