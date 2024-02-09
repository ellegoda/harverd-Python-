def great_question_of_life():
    user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything ?")
    if user_input.lower() in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

great_question_of_life()