todo_list = []

while True:
    user_action = input("Select an option, add, edit, show, complete or exit : ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a TODO : ")
            todo_list.append(todo)
        case 'show':
            for index, item in enumerate(todo_list):
                todo = f"{index + 1}. {item}"
                print(todo)
        case 'edit':
            number = int(input("Which TODO to edit : ")) - 1
            existing_todo = todo_list[number]
            todo_list[number] = input("Editing " + existing_todo + " : ")
        case 'complete':
            todo = input("TODO to set as complete :")
            todo_list.remove(todo)
        case 'exit':
            break

print("Bye")
