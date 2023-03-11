todo_list = []

while True:
    user_action = input("Select an option, add, edit, show, complete or exit : ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a TODO : ") + '\n'
            
            file = open('files/todos.txt','r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open('files/todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('files/todos.txt','r')
            todo_list = file.readlines()
            file.close()
            for index, item in enumerate(todo_list):
                item = item.replace('\n','')
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
