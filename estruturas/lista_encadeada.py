class ListaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

class no:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None

class lista_encadeada:
    #CONSTRUTOR
    def __init__(self):
        self.__head = None
        self.__tamanho = 0
    
    #MÉTODOS ESPECIAIS
    def __str__(self):
        if self.vazia():
            return '[]'
    
        lista = '['
        cursor = self.__head
        while(cursor != None):
            lista += f'{cursor.carga}, '
            cursor = cursor.prox
        lista = lista.rstrip(', ') + ']' 
        return lista
    
    def __len__(self):
        return self.__tamanho
    
    #MÉTODOS DE CONTROLE
    def vazia(self):
        return self.__tamanho == 0    
    
    #MÉTODOS GERAIS
    def insere(self, carga:any):
        novo = no(carga)
        if self.vazia():
            self.__head = novo
        else:
            cursor = self.__head
            while(cursor.prox != None):
                cursor = cursor.prox
            cursor.prox = novo
        self.__tamanho += 1

    def remove(self, num):
        if self.vazia():
            raise ListaError("a lista está vazia")
        if num < 0 or num >= self.__tamanho:
            raise ListaError("valor fora do intervalo")
        if len(self) == 1:
            self.__head = self.__head.prox
        else:
            cont = 0
            cursor = self.__head
            while cont != num-1:
                cursor = cursor.prox
                cont += 1
            cursor.prox = cursor.prox.prox
        self.__tamanho -= 1

    def modifica(self, num, carga):
        if num < 0 or num >= self.__tamanho:
            raise ListaError("valor fora do intervalo")
        else:
            cursor = self.__head
            cont = 0
            while(cont != num):
                cursor = cursor.prox
                cont += 1
            cursor.carga = carga

    def busca(self, elemento):
        cursor = self.__head
        while (cursor != None):
            if cursor.carga == elemento:
                return cursor.carga
            cursor = cursor.prox
        raise ListaError(f'{elemento} não encontrado na fila')
    
    def busca_elemento(self, num:int):
        if num < 0 or num >= self.__tamanho:
            raise ListaError("valor fora do intervalo")
        cont = 0
        cursor = self.__head
        for _ in range(num):
            cursor = cursor.prox
        return cursor.carga
    
    def busca_posicao(self, elemento):
        cont = 0
        cursor = self.__head
        while (cursor != None):
            if cursor.carga == elemento:
                return cont
            cursor = cursor.prox
            cont += 1
        return -1 

#teste
if __name__ == '__main__':
    #teste lista sequencial
    teste = lista_encadeada()
    teste.insere('1')
    teste.insere('2')
    teste.insere('3')
    teste.insere('4')
    teste.insere('5')
    print(teste)
    teste.modifica(3, '10')
    teste.modifica(4, '20')
    print(teste)
    teste.remove(1)
    print(teste)
    teste.remove(2)
    print(teste)
    print('-------')
    print(teste.busca_elemento(1))
    print(teste.busca_elemento(2))

    print('-------')
    print(teste.busca('1'))
    print(teste.busca('3'))

    print('-------')
    print(teste.busca_posicao('3'))
    print(teste.busca_posicao('4'))