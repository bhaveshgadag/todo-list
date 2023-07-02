import functions
import PySimpleGUI as sg

label = sg.Text('Type in a todo:')
user_input = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')

window = sg.Window('To-do list',
                   layout=[[label],[user_input, add_button]],
                   font=('Helvetica',20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todo = values['todo']
            todos = functions.get_todos()
            todos.append(todo + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
