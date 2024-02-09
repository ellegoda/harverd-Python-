from collections import Counter


def main():
    grocery_list = []

    try:
        while True:
            item = input("")
            grocery_list.append(item.lower())
    except EOFError:
        pass  # End of input

    item_counts = Counter(grocery_list)

    sorted_items = sorted(item_counts.items(), key=lambda x: x[0])

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
