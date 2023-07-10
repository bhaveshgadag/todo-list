import PySimpleGUI as sg
from zip_extractors import extract_archive

label1 = sg.Text("Select archive")
input1 = sg.Input()
choose_btn1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_msg = sg.Text(key='output_msg')

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_btn1], 
                   [label2, input2, choose_btn2], 
                   [extract_button, output_msg]])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Extract':
        extract_archive(values['archive'], values['folder'])
        window['output_msg'].Update(value='Extraction completed!')


window.close()