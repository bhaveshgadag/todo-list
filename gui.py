import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists('todos.txt'):
    with open('files/todos.txt', 'w') as file:
        pass

timestamp = sg.Text(key='timestamp')
label = sg.Text('Type in a todo:')
user_input = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('To-do list',
                   layout=[
                   [timestamp],
                   [label],
                   [user_input, add_button],
                   [list_box,edit_button, complete_button],
                   [exit_button]],
                   font=('Helvetica',20))

while True:
    event, values = window.read(timeout=200)
    window['timestamp'].Update(time.strftime('%d %b %Y, %H:%M:%S'))
    match event:
        case "Add":
            #try:
            todo = values['todo']
            todos = functions.get_todos()
            todos.append(todo + "\n")
            functions.write_todos(todos)
        
            # Clear input box and update list
            window['todo'].Update(value='')
            window['todos'].Update(values=todos)
            #except:
               # sg.popup('Please enter a todo')
        case "Edit":
            try:
                todo = values['todos'][0]
                new_todo = values['todo'] + "\n"
    
                todos = functions.get_todos()
                todo_index = todos.index(todo)
                todos[todo_index] = new_todo
    
                functions.write_todos(todos)
                # Clear input box and update list
                window['todo'].Update(value='')
                window['todos'].Update(values=todos)
            except IndexError:
                sg.popup('Please select a todo.')
        case 'Complete':
            try:
                selected_todo = values['todos'][0]
                
                todos = functions.get_todos()
                todos.remove(selected_todo)
                functions.write_todos(todos)
                # Clear input box and update list
                window['todo'].Update(value='')
                window['todos'].Update(values=todos)
            except IndexError:
                sg.popup('Please select a todo')
        case 'Exit':
            break
        case 'todos':
            # update input box with user selection
            todo = values['todos'][0]
            todo = todo.strip()
            window['todo'].Update(value=todo)
        case sg.WIN_CLOSED:
            break

window.close()
