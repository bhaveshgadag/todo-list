todo_list = []

while True:
    user_action = input("Select an option, add, edit, show, complete or exit : ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a TODO : ") + '\n'
            
            with open('files/todos.txt','r') as file:
            	todos = file.readlines()
            
            todos.append(todo)
            
            with open('files/todos.txt','w') as file:
            	file.writelines(todos)
            	
        case 'show':
            with open('files/todos.txt','r') as file:
            	todos = file.readlines()
            	
            for index, item in enumerate(todos):
                item = item.strip('\n')
                todo = f"{index + 1}. {item}"
                print(todo)
                
        case 'edit':
            number = int(input("Which TODO to edit : ")) - 1
            
            with open('files/todos.txt','r') as file:
            	todos = file.readlines()
            	
            existing_todo = todos[number]
            	
            todos[number] = input("Editing " + existing_todo.strip("\n") + " : ") + "\n"
            with open('files/todos.txt','w') as file:
            	file.writelines(todos)
            	
        case 'complete':
            number = int(input("TODO to set as complete :"))
            index = number - 1
            
            with open('files/todos.txt','r') as file:
            	todos = file.readlines()
            	
            todo = todos[index].strip("\n")
            print(f"Removing {todo} from list as it is complete.")
            todos.pop(index)
            
            with open('files/todos.txt','w') as file:
            	file.writelines(todos)
            	
        case 'exit':
            break

print("Bye")
