class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __str__(self):
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória.')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'



livro1 = Livro('Python Rocks', 'Bruno', 400)
livro2 = Livro('IA com Python', 'João', 350)

print(livro1)

print(livro2)

print(len(livro1))

print(livro1 + livro2)

print(livro1 * 3)

