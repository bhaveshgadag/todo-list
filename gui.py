import functions
import PySimpleGUI as psg

label = psg.Text('Type in a todo:')
user_input = psg.InputText(tooltip='Enter todo')
button = psg.Button('Add')

window = psg.Window('To-do list', layout=[[label],[user_input, button]])

window.read()