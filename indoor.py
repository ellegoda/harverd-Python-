def arithmetic_interpreter(expression):
    try:
        x, operator, z = expression.split()

        x = int(x)
        z = int(z)

        if operator == '+':
            result = x + z
        elif operator == '-':
            result = x - z
        elif operator == '*':
            result = x * z
        elif operator == '/':
            result = x / z
        else:
            raise ValueError("Invalid operator")

        print(f"{result:.1f}")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero")


def interpreter_program():
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ").strip()

    arithmetic_interpreter(expression)


if __name__ == "__main__":
    interpreter_program()
