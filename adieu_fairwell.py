def bid_adieu(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        formatted_names = ", ".join(names[:-1]) + f", and {names[-1]}"
        return f"Adieu, adieu, to {formatted_names}"


def main():
    names = []
    print("Name: ")

    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    for i in range(1, len(names) + 1):
        print(bid_adieu(names[:i]))


if __name__ == "__main__":
    main()
