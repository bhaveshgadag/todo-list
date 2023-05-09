FILEPATH = 'files/todos.txt'

def get_todos(filepath=FILEPATH):
	"""Function to read to-do list from file"""
	with open(filepath, 'r') as file_local:
		todos_local = file_local.readlines()
	return todos_local

		
def write_todos(todos_local,filepath=FILEPATH):
	"""Function to write to-do list to file"""
	with open(filepath, 'w') as file_local:
            file_local.writelines(todos_local)