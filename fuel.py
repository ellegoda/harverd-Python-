def main():
    while True:
        fraction_input = input("Fractions: ")

        try:
            numerator, denominator = fraction_input.split('/')
            x = int(numerator)
            y = int(denominator)

            if x > y or y == 0:
                continue

            fuel_percentage = round((x / y) * 100)

            if fuel_percentage <= 1:
                print("E")
                break
            elif fuel_percentage >= 99:
                print("F")
                break
            else:
                print(f"{fuel_percentage}%")
                break
        except ValueError:
            continue
        except ZeroDivisionError:
            break


if __name__ == "__main__":
    main()
