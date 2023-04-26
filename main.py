def get_todos(filepath='files/todos.txt'):
	"""Function to read to-do list from file"""
	with open(filepath, 'r') as file_local:
		todos_local = file_local.readlines()
	return todos_local

		
def write_todos(todos_local,filepath='files/todos.txt'):
	"""Function to write to-do list to file"""
	with open(filepath, 'w') as file_local:
            file_local.writelines(todos_local)
            
print(help(get_todos))
print(help(write_todos))
while True:
    user_action = input("Select an option, add, edit, show, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            todo = f"{index + 1}. {item}"
            print(todo)
                
    elif user_action.startswith("edit"):
         try:
         	number = int(user_action[5:]) - 1
         	todos = get_todos()
         	existing_todo = todos[number]
         		
         	todos[number] = input("Editing '" + existing_todo.strip("\n") + "' : ") + "\n"
         		
         	write_todos(todos)
         	
         except ValueError:
         	print("Incorrect use of command")
         	continue

    elif user_action.startswith("complete"):
         try:
         	number = int(user_action[9:])
         	index = number - 1
         	
         	todos = get_todos()
         	
         	todo = todos[index].strip("\n")
         	print(f"Removing {todo} from list as it is complete.")
         	todos.pop(index)
         	
         	write_todos(todos)
         		
         except IndexError:
         	print("Value out of range.")
         	continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input is entered")

print("Bye")
