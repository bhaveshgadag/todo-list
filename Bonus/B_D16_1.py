import PySimpleGUI as psg

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
choose_btn1 = psg.FileBrowse()

label2 = psg.Text("Select destination folder:")
input2 = psg.Input()
choose_btn2 = psg.FolderBrowse()

compress_button = psg.Button("Compress")

window = psg.Window("File Compressor", layout=[[label1,input1,choose_btn1],[label2,input2,choose_btn2],[compress_button]])

window.read()
window.close()