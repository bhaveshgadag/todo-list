
while True:
    user_action = input("Select an option, add, edit, show, complete or exit : ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            todo = f"{index + 1}. {item}"
            print(todo)
                
    elif 'edit' in user_action:
        number = int(input("Which TODO to edit : ")) - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        existing_todo = todos[number]

        todos[number] = input("Editing " + existing_todo.strip("\n") + " : ") + "\n"
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(input("TODO to set as complete :"))
        index = number - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todo = todos[index].strip("\n")
        print(f"Removing {todo} from list as it is complete.")
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'exit' in user_action:
        break

print("Bye")
