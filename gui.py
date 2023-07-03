import functions
import PySimpleGUI as sg

label = sg.Text('Type in a todo:')
user_input = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button('Edit')

window = sg.Window('To-do list',
                   layout=[[label],[user_input, add_button],[list_box,edit_button]],
                   font=('Helvetica',20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo = values['todo']
            todos = functions.get_todos()
            todos.append(todo + "\n")
            functions.write_todos(todos)

            # Clear input box and update list
            window['todo'].Update(value='')
            window['todos'].Update(values=todos)
        case "Edit":
            todo = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            todo_index = todos.index(todo)
            todos[todo_index] = new_todo

            functions.write_todos(todos)
            # Clear input box and update list
            window['todo'].Update(value='')
            window['todos'].Update(values=todos)
        case 'todos':
            # update input box with user selection
            todo = values['todos'][0]
            todo = todo.strip()
            window['todo'].Update(value=todo)
        case sg.WIN_CLOSED:
            break

window.close()
