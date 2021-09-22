#   Utilizado o writerow:

from csv import writer # Gera um objeto para que possamos escrever em um arquivo CSV

with open('filmes.csv', 'w', newline='') as arquivo: # newline utilizado apenas em windows
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração']) # writerow
    while filme != 'sair': # Loop para preenchimento das linhas. Sair irá parar o loop
        filme = input('informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme em minutos: ')
            escritor_csv.writerow([filme, genero, duracao])

"""
from csv import DictWriter

with open('filmes.csv', 'w', newline='') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração'] # Criando o cabeçalho
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho) #fieldnames é um kwargs para o cabeçalho
    escritor_csv.writeheader() # Método para esrever o cabeçalho
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair'
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme: ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero}, {"Duração": duracao})
"""


