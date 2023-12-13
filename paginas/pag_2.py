import psycopg2
import os
import sys
from dotenv import load_dotenv
import json
import PySimpleGUI as sg
from paginas.pag_3 import pag_3

# importa a funcao de calculo do arquivo conexao.py

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from calculo import similaridade_global

load_dotenv()


#Conecta com o banco de dados
conexao = psycopg2.connect(database = 'RBC', host = 'localhost', user= 'postgres', password = 'admin123', port = 5432)

def pag_2(cnf):
    toprow = ['ID', 'Objetivo', 'Simlaridade']
    rows = []
    
    # Cria um cursor para executar comandos SQL
    cur = conexao.cursor()

    # Cria um vetor dinamico para armazenar os valores de similaridade global
    similaridade_global_dic = {}

    # Calcula a similaridade global
    similaridade_global_dic = similaridade_global(conexao, cur, 'novo_caso.json')
    
    print(similaridade_global_dic)

    
    # Mutiplica a similaridade global por 100 para facilitar a visualização
    for i in range(1, len(similaridade_global_dic)+1):
        similaridade_global_dic[i] = round(similaridade_global_dic[i]*100,2)
        if similaridade_global_dic[i] > 100:
            similaridade_global_dic[i] = 100


    opcoes_objetivo = []

    # Se a similaridade global for maior que a cnf minima, o caso é recomendado
    for i in range(1, len(similaridade_global_dic)+1):
        if similaridade_global_dic[i] >= cnf:
            cur.execute(f"SELECT desc_doenca FROM public.casos_casospt WHERE caso = {i}")
            objetivo = cur.fetchall()
            rows.append([i, objetivo[0][0], similaridade_global_dic[i]])
            if objetivo[0][0] not in opcoes_objetivo:
                opcoes_objetivo.append(objetivo[0][0])
    
    # Ordena os casos recomendados por similaridade global
    rows = sorted(rows, key=lambda x: x[2], reverse=True)
    

    

    
    

    
    # Cria a tabela
    tabela = sg.Table(values=rows, headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

    botoes = [
        [sg.Button('Continuar')],
        [sg.Button('Voltar')],
        [sg.Button('Sair')],
    ]
    layout = [[tabela],
              [sg.Column(botoes, element_justification='right', expand_x=True)]]
    window = sg.Window('Tabela', layout, grab_anywhere=False)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Sair':
            window.close()
            break
        elif event == 'Voltar':
            window.close()
            return 0
        if event == 'Continuar':
            if values['-TABLE-'] == []:
                sg.popup('Selecione um caso para continuar', title='Erro')
                continue
            id = rows[values['-TABLE-'][0]]
            teste = pag_3(cur, id[0], opcoes_objetivo, 'novo_caso.json')
            if teste == 1:
                conexao.commit()
                break

            
            

    # Fecha o cursor e a conexão com o banco de dados

    cur.close()
    conexao.close()   
    window.close()
