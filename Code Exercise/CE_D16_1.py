import PySimpleGUI as psg

label1 = psg .Text('Enter feet:')
input1 = psg.InputText()

label2 = psg .Text('Enter inches:')
input2 = psg.InputText()

convert_button  = psg.Button('Convert')

window = psg.Window('Converter', layout=[[label1,input1],[label2,input2],[convert_button]])

window.read()
window.close()