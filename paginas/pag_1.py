import json
import PySimpleGUI as sg
from paginas.pag_2 import pag_2

def pag_1():
    area_damaged = ["Areas baixas", "Espalhado", "Campo inteiro", "Areas superiores", "Desconhecido"]

    canker_lesion = ["Bronzeado a marrom", "Marrom", "Marrom escuro", "Desconhecido"]

    crop_hist = ["Dif-1 ano", "Mesmo-1 ano", "Mesmo-2 ano", "Mesmo-7 ano", "Desconhecido"]

    date = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro",
            "Dezembro", "Desconhecido"]

    external_decay = ["Ausente", "Firme-seco", "Desconhecido"]

    fruit_spots = ["Ausente", "Colorido", "Escuro", "Desconhecido"]

    fruiting_bodies = ["Ausente", "Presente", "Desconhecido"]

    fruit_pods = ["Normal", "Poucos presentes", "Doente", "Desconhecido"]

    germination = ["90-100%", "80-89%", "Lt-80%", "Desconhecido"]

    hail = ["Sim", "Nao", "Desconhecido"]

    int_discolor = ["Nenhuma", "Marrom", "Preto", "Desconhecido"]

    leaf_malf = ["Ausente", "Presente", "Desconhecido"]

    leaf_mild = ["Ausente", "Superficial", "Abundante", "Desconhecido"]

    leaf_shread = ["Ausente", "Presente", "Desconhecido"]

    leafspots_halo = ["Ausente", "Sem Aereolado", "Com Aereolado", "Desconhecido"]

    leafspot_size = ["Tam menor 1/8", "Tam maior 1/8", "Desconhecido"]

    leafspot_marg = ["Sem marg", "Com marg", "Desconhecido"]

    leaves = ["Normal", "Anormal", "Desconhecido"]

    lodging = ["Sim", "Nao", "Desconhecido"]

    mold_growth = ["Ausente", "Presente", "Desconhecido"]

    mycelium = ["Ausente", "Presente", "Desconhecido"]

    plant_growth = ["Normal", "Anormal", "Desconhecido"]

    plant_stand = ["Normal", "Lt-normal", "Desconhecido"]

    precip = ["Gt-normal", "Lt-normal", "Normal", "Desconhecido"]

    roots = ["Normal", "Podre", "Cortadas-off", "Desconhecido"]

    sclerotia = ["Ausente", "Presente", "Desconhecido"]

    seed = ["Normal", "Anormal", "Desconhecido"]

    seed_discolor = ["Ausente", "Presente", "Desconhecido"]

    seed_size = ["Normal", "Lt-normal", "Desconhecido"]

    seed_tmt = ["Nenhuma", "Fungicida", "Outros", "Desconhecido"]

    severity = ["Leve", "Serio", "Muito serio", "Desconhecido"]

    shriveling = ["Ausente", "Presente", "Desconhecido"]

    stem = ["Normal", "Anormal", "Desconhecido"]

    stem_cankers = ["Ausente", "Acima do solo", "Abaixo do solo", "Acima do segundo", "Desconhecido"]

    temp = ["Lt-normal", "Normal", "Gt-normal", "Desconhecido"]

    sz1 = (25, 1)
    sz2 = (15, 0)

    col1 = [
        # Transforma todos os sg.combo readonly=True
        [sg.Text('Área danificada', size=sz1,background_color='light grey'), sg.Combo(area_damaged, key='area_damaged', size=sz2, readonly=True)],
        [sg.Text('Lesão de cancro', size=sz1,background_color='light grey'), sg.Combo(canker_lesion, key='canker_lesion', size=sz2, readonly=True)],
        [sg.Text('Histórico da cultura', size=sz1,background_color='light grey'), sg.Combo(crop_hist, key='crop_hist', size=sz2, readonly=True)],
        [sg.Text('Data', size=sz1,background_color='light grey'), sg.Combo(date, key='date', size=sz2, readonly=True)],
        [sg.Text('Decaimento externo', size=sz1,background_color='light grey'), sg.Combo(external_decay, key='external_decay', size=sz2, readonly=True)],
        [sg.Text('Descoloração interna', size=sz1,background_color='light grey'), sg.Combo(int_discolor, key='int_discolor', size=sz2, readonly=True)],
        [sg.Text('Malformação de folhas', size=sz1,background_color='light grey'), sg.Combo(leaf_malf, key='leaf_malf', size=sz2, readonly=True)],
        [sg.Text('Manchas foliares',size=sz1,background_color='light grey'), sg.Combo(leaf_mild, key='leaf_mild',size=sz2, readonly=True)],
        [sg.Text('Rasgo de folhas',size=sz1,background_color='light grey'), sg.Combo(leaf_shread, key='leaf_shread',size=sz2, readonly=True)],
        [sg.Text('Halo de manchas foliares',size=sz1,background_color='light grey'), sg.Combo(leafspots_halo, key='leafspots_halo',size=sz2, readonly=True)],
        [sg.Text('Micélio',size=sz1,background_color='light grey'), sg.Combo(mycelium, key='mycelium',size=sz2, readonly=True)],
        [sg.Text('Crescimento da planta',size=sz1,background_color='light grey'), sg.Combo(plant_growth, key='plant_growth',size=sz2, readonly=True)],
        [sg.Text('Precipitado',size=sz1,background_color='light grey'), sg.Combo(precip, key='precip',size=sz2, readonly=True)],
        [sg.Text('Raízes',size=sz1,background_color='light grey'), sg.Combo(roots, key='roots',size=sz2, readonly=True)],
        [sg.Text('Murchando', size=sz1,background_color='light grey'), sg.Combo(shriveling, key='shriveling', size=sz2, readonly=True)],
        [sg.Text('Caule', size=sz1,background_color='light grey'), sg.Combo(stem, key='stem', size=sz2, readonly=True)],
        [sg.Text('Temperatura', size=sz1,background_color='light grey'), sg.Combo(temp, key='temp', size=sz2, readonly=True)]
    ]

    col2 = [
        [sg.Text('Manchas de frutas', size=sz1,background_color='light grey'), sg.Combo(fruit_spots, key='fruit_spots', size=sz2, readonly=True)],
        [sg.Text('Corpos de frutificação', size=sz1,background_color='light grey'), sg.Combo(fruiting_bodies, key='fruiting_bodies', size=sz2, readonly=True)],
        [sg.Text('Vagens de frutas', size=sz1,background_color='light grey'), sg.Combo(fruit_pods, key='fruit_pods', size=sz2, readonly=True)],
        [sg.Text('Germinação', size=sz1,background_color='light grey'), sg.Combo(germination, key='germination', size=sz2, readonly=True)],
        [sg.Text('Granizo', size=sz1,background_color='light grey'), sg.Combo(hail, key='hail', size=sz2, readonly=True)],
        [sg.Text('Tamanho das manchas foliares', size=sz1,background_color='light grey'), sg.Combo(leafspot_size, key='leafspot_size', size=sz2, readonly=True)],
        [sg.Text('Margem das manchas foliares', size=sz1,background_color='light grey'), sg.Combo(leafspot_marg, key='leafspot_marg', size=sz2, readonly=True)],
        [sg.Text('Folhas', size=sz1,background_color='light grey'), sg.Combo(leaves, key='leaves', size=sz2, readonly=True)],
        [sg.Text('Lodging', size=sz1,background_color='light grey'), sg.Combo(lodging, key='lodging', size=sz2, readonly=True)],
        [sg.Text('Crescimento de mofo', size=sz1,background_color='light grey'), sg.Combo(mold_growth, key='mold_growth', size=sz2, readonly=True)],
        [sg.Text('Esclerócio', size=sz1,background_color='light grey'), sg.Combo(sclerotia, key='sclerotia', size=sz2, readonly=True)],
        [sg.Text('Semente', size=sz1,background_color='light grey'), sg.Combo(seed, key='seed', size=sz2, readonly=True)],
        [sg.Text('Descoloração da semente', size=sz1,background_color='light grey'), sg.Combo(seed_discolor, key='seed_discolor', size=sz2, readonly=True)],
        [sg.Text('Tamanho da semente', size=sz1,background_color='light grey'), sg.Combo(seed_size, key='seed_size', size=sz2, readonly=True)],
        [sg.Text('Seed Tmt', size=sz1,background_color='light grey'), sg.Combo(seed_tmt, key='seed_tmt', size=sz2, readonly=True)],
        [sg.Text('Severidade', size=sz1,background_color='light grey'), sg.Combo(severity, key='severity', size=sz2, readonly=True)],
        [sg.Text('Suporte para plantas', size=sz1,background_color='light grey'), sg.Combo(plant_stand, key='plant_stand', size=sz2, readonly=True)],
        [sg.Text('Cancro no caule', size=sz1,background_color='light grey'), sg.Combo(stem_cankers, key='stem_cankers', size=sz2, readonly=True)],
    ]


    next_button= [
        [sg.Button('Proximo')],
    ]

    layout = [
        [sg.Text('Caso Problema:'), sg.Text()],
        [sg.Column(col1), sg.Column(col2)], [sg.Text('CNF  Minima:'), sg.Spin([i for i in range(1, 101)], initial_value=75, key='cnf_min', size=(5, 1))],
        [sg.Column(next_button, element_justification='right', expand_x=True)],
    ]

    window = sg.Window('Cadastro de Produtos', layout)

    # Cria um dicionario armazenar os valores do novo caso
    novo_caso = {}
    
    # Cnf_minimo é igual ao valor inserido
    cnf = 0

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        elif event == 'Proximo':
            novo_caso = values.copy()
            # Transforma os valores nulos em "Desconhecido"
            for key in novo_caso:
                if novo_caso[key] == '':
                    novo_caso[key] = "Desconhecido"
    
            # drop cnf_min do novo_caso
            novo_caso.pop('cnf_min')

            # Salva o novo caso em um arquivo json
            with open('novo_caso.json', 'w') as f:
                json.dump(novo_caso, f)

            # Salva o cnf minimo
            cnf = values['cnf_min']
            window.disappear()
            retorno = pag_2(cnf)
            if retorno != 0:
                break
            window.reappear()

    window.close()


    # for key in novo_caso:
    #     novo_caso[key] = similaridade[key][novo_caso[key]]

    

    