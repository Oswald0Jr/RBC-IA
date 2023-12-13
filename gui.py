#instale o PySimpleGUI antes de rodar este arquivo:
# para mac/linux
# pip3 install PySimpleGUI
import PySimpleGUI as sg
from paginas import pag_1

sg.theme('Reddit')

def pag_inicial():
    buttons = [
        [sg.Button('Cadastrar Caso'),
         sg.Button('Sair')],
    ]

    layout = [
        [sg.Text('Bem vindo ao sistema de recomendação de produtos para o controle de doenças em plantações!', font=('Arial Bold',13), justification='center')],
        [sg.Text('')],
        [sg.Column(buttons, element_justification='right', expand_x=True)]
    ]

    window = sg.Window('Sistema de Recomendação', layout)

    while True:
        event, values = window.read()
        cnf = 0
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            break

        elif event == 'Cadastrar Caso':
            window.close()
            pag_1.pag_1()



pag_inicial()