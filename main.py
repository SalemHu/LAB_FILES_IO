while True:
    user_input = input("do you want to add a new To-Do item? if yes enter (Y) if no enter (N), and (exit) to exit the program: ")
    if user_input.upper() == "Y":
        file = open("to-do.txt", "a", encoding = "utf-8")
        list_input = input("please enter your to-do list: ")
        file.write(list_input + "\n")
        file.close()
    elif user_input.lower() == "exit":
        print("See you later.")
        break
    else:
        refuse = input("do you want to list your To-Do items ?if yes enter (Y) if no enter (N): ")
        if refuse.upper() == "Y":
            file = open("to-do.txt", "r", encoding = "utf-8")
            todo_list = file.read()
            print(todo_list)
        else:
            print("Good bye.")
