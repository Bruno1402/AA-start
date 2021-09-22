# Classe
class Lampada:

    # Objeto
    # O método __init__ é um método especial chamado de construtor e sua função é
    # construir o objeto da classe.
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada():
        return self.__ligada

    def liga_desliga():
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


lamp1 = Lampada('branca', 110, 60)

lamp1.liga_desliga

print(f'A lâmpada está ligada? {lamp1.checa_lampada}')

cc1 = ContaCorrente(5000, 20000)

user1 = ('Bruno', 'Pereira', 'bruno@gmail.com', '123456')
