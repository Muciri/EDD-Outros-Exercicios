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
    def insere(self, num: int, carga:any):
        if num < 0 or num >= self.__tamanho:
            raise ListaError("valor fora do intervalo")
        novo = no(carga)
        cursor = self.__head
        for i in range(num):
            anterior = cursor
            cursor = cursor.prox
        anterior.prox = novo
        novo.prox = cursor
        self.__tamanho += 1

    def insere_ordenado(self, carga:any):
        novo = no(carga)
        if self.vazia() or novo.carga < self.__head.carga:
            novo.prox = self.__head
            self.__head = novo
            return
        cursor = self.__head
        while cursor.prox != None and cursor.prox.carga < novo.carga:
            cursor = cursor.prox
        novo.prox = cursor.prox
        cursor.prox = novo

    def insere_final(self, carga:any):
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
        if len(self) == 1 or num == 0:
            self.__head = self.__head.prox
        else:
            cursor = self.__head
            for i in range(num):
                anterior = cursor
                cursor = cursor.prox
            # elemento = cursor.carga
            anterior.prox = cursor.prox
        self.__tamanho -= 1
        # return elemento

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

    def uniao(self, lista1, lista2):
        lista_n = lista_encadeada()
        
        for i in range(len(lista1)):
            lista_n.insere_final(lista1.busca_elemento(i))
        
        for i in range(len(lista2)):
            lista_n.insere_final(lista2.busca_elemento(i))
        
        return lista_n

    def intersecao(self, lista1, lista2):
        lista_n = lista_encadeada()
        for i in range(len(lista1)):
            try:
                lista_n.insere_final( lista2.busca( lista1.busca_elemento(i) ) )
            except ListaError:
                pass
        return lista_n

    def diferenca(self, lista1, lista2):
        lista_n = lista_encadeada()
        for i in range(len(lista1)):
            try:  
                lista2.busca( lista1.busca_elemento(i) )
            except ListaError:
                lista_n.insere_final(lista1.busca_elemento(i))
        
        return lista_n
    
    def separa(self, n):
        if self.vazia():
            raise ListaError("a lista está vazia")
        if n < 0 or n >= self.__tamanho:
            raise ListaError("valor fora do intervalo")

        lista_n = lista_encadeada()
        cursor = self.__head
        cont = 0
        anterior = None

        # Percorre a lista até o índice n
        while cursor != None and cont < n:
            anterior = cursor
            cursor = cursor.prox
            cont += 1

        # Se `cursor` está no índice `n`, ele será o novo início da lista separada
        if cursor != None:
            lista_n.__head = cursor  # Nova lista começa em cursor
            lista_n.__tamanho = self.__tamanho - n
            anterior.prox = None  # Quebra a referência da lista original
            self.__tamanho = n

        return lista_n

#teste
if __name__ == '__main__':
    #teste lista sequencial
    teste = lista_encadeada()
    teste.insere_final(10)
    teste.insere_final(20)
    teste.insere_final(30)
    teste.insere_final(40)
    teste.insere_final(50)
    print(teste)
    print('-------')
    # teste.insere_ordenado(1)
    # teste.insere_ordenado(35)
    # teste.insere_ordenado(60)
    # print(teste)
    print('-------')

    print(teste.separa(1))
    print(teste)
    print('-------')

    l1 = [1, 2, 3, 4, 5, 10, 20]
    l2 = [1, 9, 3, 8, 5]

    lista1 = lista_encadeada()
    lista2 = lista_encadeada()
    for i in l1:
        lista1.insere_final(i)

    for i in l2:
        lista2.insere_final(i)

    print('listas:')
    print(lista1)
    print(lista2)

    print('união das listas:')
    print(teste.uniao(lista1, lista2))

    print('interseção das listas:')
    print(teste.intersecao(lista1, lista2))

    print('diferença das listas:')
    print(f'diferença da lista1 para a lista2: {teste.diferenca(lista1, lista2)}')
    print(f'diferença da lista2 para a lista1: {teste.diferenca(lista2, lista1)}')
    
    # teste.insere(1, '0.5')
    # teste.insere(3, '3.5')
    # print(teste)
    # print('-------')
    
    # teste.modifica(3, '35')
    # teste.modifica(4, '30')
    # print(teste)
    # print('-------')

    # teste.remove(0)
    # print(teste)
    # teste.remove(1)
    # print(teste)
    # teste.remove(2)
    # print(teste)
    # teste.remove(3)
    # print(teste)
    # print('-------')
    
    # print(teste.busca_elemento(1))
    # print(teste.busca_elemento(2))
    # print('-------')
    
    # print(teste.busca('35'))
    # print(teste.busca('4')) 
    # print('-------')
    
    # print(teste.busca_posicao('3'))
    # print(teste.busca_posicao('4'))