food_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def display_total_cost(order):
    total_cost = sum(food_menu[item] for item in order)
    print(f"${total_cost:.2f}")


def main():
    order = []
    try:
        while True:
            item_input = input("Enter an item (Ctrl-D to finish): ").strip().title()

            if item_input in food_menu:
                order.append(item_input)
                display_total_cost(order)
            else:
                print("Invalid item. Please enter a valid menu item.")
    except EOFError:
        print("Order complete. Total cost:")
        display_total_cost(order)


if __name__ == "__main__":
    main()
