import PySimpleGUI as sg
import waapi-database as wd
import wd_client as wc

def gui():
    sg.theme('Dark Blue 14')

    layout = [  [sg.Text('WAAPI Database')],
                [sg.Output(size=(70, 20), font=("宋体", 10))],
                [sg.Button('Get it'), sg.Button('Cancel')] ]

    window = sg.Window('WAAPI Database', layout)

    while True:
        event, values = window.read()

    window.close()

def main():    
    gui()

if __name__ == '__main__':
    main()