"""
Utilizando o reader:

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo: #encoding é utilizado para o windows
    leitor_scv = reader(arquivo)
    next(leitor_scv) # pular o cabeçalho
    for linha in leitor_scv: # cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros.')
"""

"""
# Utilizando o DictReader:

from csv import DictReader

with open('C:\\Users\\PC\\OneDrive\\Área de Trabalho\\lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv: # cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']} centímetros")
"""



