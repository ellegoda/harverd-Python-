def camel_to_snake(variable_name):
    snake_case = ''
    for char in variable_name:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')


def main():
    camel_case_variable = input("camelCase: ")
    snake_case_variable = camel_to_snake(camel_case_variable)
    print(f"The corresponding snake case variable is: {snake_case_variable}")


if __name__ == "__main__":
    main()
