import tkinter as tk

"""class Aplicacao(tk.Frame):
    # Método para selecionar as colunas
    def selecionarcolunas(self):
        oportunidade = self.oportunidade.get()
        pipeline = self.pipeline.get()
        estagio_pipe = self.estagio_pipe.get()
        usuario = self.usuario.get()
        contato = self.contato.get()
        empresa = self.empresa.get()
        produto = self.produto.get()
        valor = self.valor.get()

        ordem_colunas = [oportunidade, pipeline, estagio_pipe, usuario, contato, empresa, produto, valor]
        print(ordem_colunas)

    def __init__(self):
        fonte_padrao =("Arial", "10")
        # Inicializando o frame
        tk.Frame.__init__(self)
        self.master.title("")

        tk.Label(self.master, text="Oportunidade", font=fonte_padrao).grid(row=0, sticky=tk.W)
        tk.Label(self.master, text="Pipeline", font=fonte_padrao).grid(row=1, sticky=tk.W)
        tk.Label(self.master, text="Estágio Pipeline", font=fonte_padrao).grid(row=2, sticky=tk.W)
        tk.Label(self.master, text="Responsável", font=fonte_padrao).grid(row=3, sticky=tk.W)
        tk.Label(self.master, text="Contato", font=fonte_padrao).grid(row=4, sticky=tk.W)
        tk.Label(self.master, text="Empresa", font=fonte_padrao).grid(row=5, sticky=tk.W)
        tk.Label(self.master, text="Produto", font=fonte_padrao).grid(row=6, sticky=tk.W)
        tk.Label(self.master, text="Valor", font=fonte_padrao).grid(row=7, sticky=tk.W)


        oportunidade = tk.Entry(self.master)
        pipeline = tk.Entry(self.master)
        estagio_pipe = tk.Entry(self.master)
        usuario = tk.Entry(self.master)
        contato = tk.Entry(self.master)
        empresa = tk.Entry(self.master)
        produto = tk.Entry(self.master)
        valor = tk.Entry(self.master)


        oportunidade.grid(row=0, column=1)
        pipeline.grid(row=1, column=1)
        estagio_pipe.grid(row=2, column=1)
        usuario.grid(row=3, column=1)
        contato.grid(row=4, column=1)
        empresa.grid(row=5, column=1)
        produto.grid(row=6, column=1)
        valor.grid(row=7, column=1)

        self.confirmar = tk.Button(width=12, command=self.selecionarcolunas, text="Corfirmar")
        self.confirmar.grid(row=8, column=1)


        tk.mainloop()

Aplicacao()"""
ordem_colunas = []

root = tk.Tk()


class Aplicacao(tk.Frame):
    # Método para selecionar as colunas

    def selecionar_colunas(self):
        oportunidade = self.oportunidade.get()
        pipeline = self.pipeline.get()
        estagio_pipeline = self.estagio_pipeline.get()
        usuario = self.usuario.get()
        contato = self.contato.get()
        empresa = self.empresa.get()
        produto = self.produto.get()
        valor = self.valor.get()

        global ordem_colunas
        ordem_colunas = [oportunidade, pipeline, estagio_pipeline, usuario, contato, empresa, produto, valor]

    def __init__(self):
        tk.Frame.__init__(self)
        # Definindo uma fonte padrão
        self.fonte_padrao = ("Arial", 10)

        # Inserindo o título
        self.titulo = tk.Label(self.master, text="Selecione as colunas que correspondem às "
                                                             "opções apresentadas", font=self.fonte_padrao)
        self.titulo.grid(row=0, sticky=tk.N, columnspan=2)

        # Oportunidade
        self.oportunidadeLabel = tk.Label(self.master, text="Oportunidade", font=self.fonte_padrao)
        self.oportunidadeLabel.grid(row=1, column=0, sticky=tk.W)

        self.oportunidade = tk.Entry(self.master, width=38, font=self.fonte_padrao)
        self.oportunidade.grid(row=1, column=1)

        # Pipeline
        self.pipelineLabel = tk.Label(self.master, text="Pipeline", font=self.fonte_padrao)
        self.pipelineLabel.grid(row=2, column=0, sticky=tk.W)

        self.pipeline = tk.Entry(self.master, width=38, font=self.fonte_padrao)
        self.pipeline.grid(row=2, column=1)

        # Estágio do pipeline
        self.estagio_pipelineLabel = tk.Label(self.master, text="Estágio Pipeline", font=self.fonte_padrao)
        self.estagio_pipelineLabel.grid(row=3, column=0, sticky=tk.W)

        self.estagio_pipeline = tk.Entry(self.master, width=38, font=self.fonte_padrao)
        self.estagio_pipeline.grid(row=3, column=1)

        # Usuário
        self.usuarioLabel = tk.Label(self.master, text="Usuário", font=self.fonte_padrao)
        self.usuarioLabel.grid(row=4, column=0, sticky=tk.W)

        self.usuario = tk.Entry(self.master, width=38, font=self.fonte_padrao)
        self.usuario.grid(row=4, column=1)

        # Contatos Relacionados
        self.contatoLabel = tk.Label(self.master, text="Contato", font=self.fonte_padrao)
        self.contatoLabel.grid(row=5, column=0, sticky=tk.W)

        self.contato = tk.Entry(self.master, width=38, font=self.fonte_padrao)
        self.contato.grid(row=5, column=1)

        # Empresas relacionadas
        self.empresaLabel = tk.Label(self.master, text="Empresa", font=self.fonte_padrao)
        self.empresaLabel.grid(row=6, column=0, sticky=tk.W)

        self.empresa = tk.Entry(self.master, width=38, font=self.fonte_padrao)
        self.empresa.grid(row=6, column=1)

        # Produto relacionado
        self.produtoLabel = tk.Label(self.master, text="Produto", font=self.fonte_padrao)
        self.produtoLabel.grid(row=7, column=0, sticky=tk.W)

        self.produto = tk.Entry(self.master, width=38, font=self.fonte_padrao)
        self.produto.grid(row=7, column=1)

        # Valor da oportunidade
        self.valorLabel = tk.Label(self.master, text="Valor", font=self.fonte_padrao)
        self.valorLabel.grid(row=8, column=0, sticky=tk.W)

        self.valor = tk.Entry(self.master, width=38, font=self.fonte_padrao)
        self.valor.grid(row=8, column=1)

        # Mensagem para confirmação
        self.mensagem_confirmacao = tk.Label(self.master, text="Verifique as opção, clique em Confirmar"
                                                               "e em seguida clique em Concluir", font=self.fonte_padrao)
        self.mensagem_confirmacao.grid(row=9, sticky=tk.N, columnspan=2)

        # Botão de confirmação
        self.confirmar = tk.Button(self.master, text="Confirmar", font=self.fonte_padrao, width=12,
                                   command=self.selecionar_colunas)
        self.confirmar.grid(row=10, column=0)

       # Botão concluir
        self.concluir = tk.Button(self.master, text="Concluir", font=self.fonte_padrao, width=12,
                                   command=root.quit)
        self.concluir.grid(row=10, column=1)


Aplicacao()
root.mainloop()

print(ordem_colunas)