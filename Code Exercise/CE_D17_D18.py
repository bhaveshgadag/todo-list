import PySimpleGUI as sg

def convert(feet_local,inch):
	meters_local = feet_local * 0.3048 + inch * 0.0254
	return meters_local

# D18 - add theme black	
sg.theme('Black')

label1 = sg .Text('Enter feet:')
input1 = sg.InputText(key='feet')

label2 = sg .Text('Enter inches:')
input2 = sg.InputText(key='inches')

convert_button  = sg.Button('Convert')
exit_button = sg .Button('Exit') # D 18 add exit button
output_msg = sg.Text(key='output')

window = sg.Window('Converter', layout=[
[label1,input1],
[label2,input2],
[convert_button,exit_button,output_msg]])

while True:
	event, values = window.read()
	if event in (sg.WIN_CLOSED, 'Exit'):
		break
	if event == 'Convert':
		feet = float(values['feet'])
		inches = float(values['inches'])
		meters = convert(feet, inches)
		window['output'].Update(value=f'{meters} meters')
		

window.close()