def get_todos(filepath):
	with open(filepath, 'r') as file_local:
		todos_local = file_local.readlines()
	return todos_local

		
def write_todos(filepath,todos_local):
	with open(filepath, 'w') as file_local:
            file_local.writelines(todos_local)
            

while True:
    user_action = input("Select an option, add, edit, show, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos('files/todos.txt')

        todos.append(todo + "\n")

        write_todos('files/todos.txt',todos)

    elif user_action.startswith("show"):
        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            todo = f"{index + 1}. {item}"
            print(todo)
                
    elif user_action.startswith("edit"):
         try:
         	number = int(user_action[5:]) - 1
         	todos = get_todos('files/todos.txt')
         	existing_todo = todos[number]
         		
         	todos[number] = input("Editing '" + existing_todo.strip("\n") + "' : ") + "\n"
         		
         	write_todos('files/todos.txt',todos)
         	
         except ValueError:
         	print("Incorrect use of command")
         	continue

    elif user_action.startswith("complete"):
         try:
         	number = int(user_action[9:])
         	index = number - 1
         	
         	todos = get_todos('files/todos.txt')
         	
         	todo = todos[index].strip("\n")
         	print(f"Removing {todo} from list as it is complete.")
         	todos.pop(index)
         	
         	write_todos('files/todos.txt',todos)
         		
         except IndexError:
         	print("Value out of range.")
         	continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input is entered")

print("Bye")
