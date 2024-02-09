def bank_program():
    user_greeting = input("Please enter a greeting: ").lstrip()

    if user_greeting.lower().startswith("hello"):
        print("$0")
    elif user_greeting.lower().startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    bank_program()


def value(param):
    return None