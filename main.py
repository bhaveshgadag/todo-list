import functions
import time

while True:
    now = time.strftime('%d %b %Y, %H:%M:%S')
    print(f"Timestamp : {now}")
    user_action = input("Select an option, add, edit, show, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            todo = f"{index + 1}. {item}"
            print(todo)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = functions.get_todos()
            existing_todo = todos[number]

            todos[number] = input("Editing '" + existing_todo.strip("\n") + "' : ") + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Incorrect use of command")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo = todos[index].strip("\n")
            print(f"Removing {todo} from list as it is complete.")
            todos.pop(index)

            functions.write_todos(todos)

        except IndexError:
            print("Value out of range.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input is entered")

print("Bye")
