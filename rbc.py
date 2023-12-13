import PySimpleGUI as sg
from partes import parte_1

sg.theme('LightBrown6')

def pag_inicial():
    buttons = [
        [sg.Button('Cadastrar Caso'),
         sg.Button('Sair')],
    ]

    layout = [
        [sg.Text('Olá, seja bem vindo!', font=('Times New Roman',12), justification='center')],
        [sg.Text('Esse é um sistema de raciocinio baseado em casos (RBC) feito em python!', font=('Times New Roman', 12), justification='center')],
        [sg.Column(buttons, element_justification='right', expand_x=True)]
    ]

    window = sg.Window('Sistema RBC', layout)


    while True:
        event, values = window.read()
        cnf = 0
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            break

        elif event == 'Cadastrar Caso':
            window.close()
            parte_1.parte_1()



pag_inicial()