
while True:
    user_action = input("Select an option, add, edit, show, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            todo = f"{index + 1}. {item}"
            print(todo)
                
    elif user_action.startswith("edit"):
        number = int(user_action[5:]) - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        existing_todo = todos[number]

        todos[number] = input("Editing '" + existing_todo.strip("\n") + "' : ") + "\n"
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        number = int(user_action[9:])
        index = number - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todo = todos[index].strip("\n")
        print(f"Removing {todo} from list as it is complete.")
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input is entered")

print("Bye")
