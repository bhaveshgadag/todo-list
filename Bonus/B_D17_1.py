import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_btn1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_msg = sg.Text(key='output_msg')

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_btn1], [label2, input2, choose_btn2], [compress_button, output_msg]])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Compress':
        files = values['files'].split(';')
        make_archive(files, values['folder'])
        window['output_msg'].Update(value='Compression completed.')


window.close()
