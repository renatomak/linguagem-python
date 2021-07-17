class ListaDeEstudantes:
    def __init__(self, lista_inicial):
        self._estudantes = lista_inicial

    def __iter__(self):
        return IteradorDeEstudantes(self._estudantes)


class IteradorDeEstudantes:
    def __init__(self, dados):
        self.dados = dados

    def __next__(self):
        item = next(self.dados)
        return item


if __name__ == '__main__':
    lista_estudantes = ListaDeEstudantes(['item1', 'item2', 'item3'])
    print(type(lista_estudantes))
    for estudante in lista_estudantes:
        print(estudante)
