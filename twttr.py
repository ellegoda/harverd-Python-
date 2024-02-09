def main():
    user_input = input("Input: ")
    result = shorten(user_input)
    print("Output:", result)


def shorten(word):
    if word is None:
        return None

    vowels = "AEIOUaeiou"
    result_text = ''.join(char for char in word if char not in vowels)
    return result_text


if __name__ == "__main__":
    main()
