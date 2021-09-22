"""
O algoritmo abaixo está sendo criado com o objetivo de facilitar a importação de arquivos CSV para
a área de Oportunidades do Wepipe. A ideia é que o cliente passe por três etapas:
    1 - Selecionar o arquivo em Excel contendo os dados;
    2 - Apresentar quais as colunas estão relacionadas aos campos a serem preenchidos;
    3 - Selecionar o local onde será salvo o arquivo CSV para exportação.
"""
# Passo 1: cliente selecionar o arquivo em Excel que será lido
"""Passo já testado"""

from tkinter import filedialog, Tk, Frame, Label, Entry, Button, N, W
"""from pathlib import Path
import pandas as pd

local_excel = Path(filedialog.askopenfilename())
print(local_excel)

# Passo 2: ler o arquivo em Excel
""""Passo já testado""""

arquivo = pd.read_excel(local_excel)
lista_colunas = arquivo.columns.values

display(arquivo)  # Teste
print(lista_colunas)  # Teste"""

# Passo 3: Criando um box para o usuário organizar as informações do arquivo Excel
glob_ordem_colunas = []

root = Tk()


class Aplicacao(Frame):

    # Método para selecionar as colunas e finalizar o box
    def selecionar_colunas(self):
        oportunidade = self.oportunidade.get()
        pipeline = self.pipeline.get()
        estagio_pipeline = self.estagio_pipeline.get()
        usuario = self.usuario.get()
        contato = self.contato.get()
        empresa = self.empresa.get()
        produto = self.produto.get()
        valor = self.valor.get()

        global glob_ordem_colunas
        glob_ordem_colunas = [oportunidade, pipeline, estagio_pipeline, usuario, contato, empresa, produto, valor]

        root.destroy()

    def __init__(self, **kw):
        Frame.__init__(self)
        # Definindo uma fonte padrão
        super().__init__(**kw)
        self.fonte_padrao = ("Arial", 10)

        # Inserindo o título do box
        self.titulo = Label(self.master, text="Selecione as colunas que correspondem às "
                                              "opções apresentadas", font=self.fonte_padrao)
        self.titulo.grid(row=0, sticky=N, columnspan=2)

        # Oportunidade
        self.oportunidadeLabel = Label(self.master, text="Oportunidade", font=self.fonte_padrao)
        self.oportunidadeLabel.grid(row=1, column=0, sticky=W)

        self.oportunidade = Entry(self.master, width=38, font=self.fonte_padrao)
        self.oportunidade.grid(row=1, column=1)

        # Pipeline
        self.pipelineLabel = Label(self.master, text="Pipeline", font=self.fonte_padrao)
        self.pipelineLabel.grid(row=2, column=0, sticky=W)

        self.pipeline = Entry(self.master, width=38, font=self.fonte_padrao)
        self.pipeline.grid(row=2, column=1)

        # Estágio do pipeline
        self.estagio_pipelineLabel = Label(self.master, text="Estágio Pipeline", font=self.fonte_padrao)
        self.estagio_pipelineLabel.grid(row=3, column=0, sticky=W)

        self.estagio_pipeline = Entry(self.master, width=38, font=self.fonte_padrao)
        self.estagio_pipeline.grid(row=3, column=1)

        # Usuário
        self.usuarioLabel = Label(self.master, text="Usuário", font=self.fonte_padrao)
        self.usuarioLabel.grid(row=4, column=0, sticky=W)

        self.usuario = Entry(self.master, width=38, font=self.fonte_padrao)
        self.usuario.grid(row=4, column=1)

        # Contatos Relacionados
        self.contatoLabel = Label(self.master, text="Contato", font=self.fonte_padrao)
        self.contatoLabel.grid(row=5, column=0, sticky=W)

        self.contato = Entry(self.master, width=38, font=self.fonte_padrao)
        self.contato.grid(row=5, column=1)

        # Empresas relacionadas
        self.empresaLabel = Label(self.master, text="Empresa", font=self.fonte_padrao)
        self.empresaLabel.grid(row=6, column=0, sticky=W)

        self.empresa = Entry(self.master, width=38, font=self.fonte_padrao)
        self.empresa.grid(row=6, column=1)

        # Produto relacionado
        self.produtoLabel = Label(self.master, text="Produto", font=self.fonte_padrao)
        self.produtoLabel.grid(row=7, column=0, sticky=W)

        self.produto = Entry(self.master, width=38, font=self.fonte_padrao)
        self.produto.grid(row=7, column=1)

        # Valor da oportunidade
        self.valorLabel = Label(self.master, text="Valor", font=self.fonte_padrao)
        self.valorLabel.grid(row=8, column=0, sticky=W)

        self.valor = Entry(self.master, width=38, font=self.fonte_padrao)
        self.valor.grid(row=8, column=1)

        # Botão de confirmação
        self.confirmar = Button(self.master, text="Confirmar", font=self.fonte_padrao, width=12,
                                   command=self.selecionar_colunas)
        self.confirmar.grid(row=9, column=1)


Aplicacao()
root.mainloop()

for nome in glob_ordem_colunas:
    print(nome)
