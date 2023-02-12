todo_list = []

while True:
    user_action = input("Select an option, add, edit, show or exit : ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a TODO : ")
            todo_list.append(todo)
        case 'show':
            for item in todo_list:
                print(item)
        case 'edit':
            for item in todo_list:
                print(item)
            number = int(input("Which Todo to edit : ")) - 1
            existing_todo = todo_list[number]
            todo_list[number] = input("Editing " + existing_todo + " : ")
        case 'exit':
            break

print("Bye")
