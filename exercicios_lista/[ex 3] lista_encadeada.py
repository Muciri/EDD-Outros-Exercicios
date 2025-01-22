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
    
    #MÉTODOS DO EXERCÍCIO 
    #------QUESTÃO 2------ 
    def maiores(self, n):
        cont = 0
        cursor = self.__head
        try:
            while(cursor != None):
                if cursor.carga > n:
                    cont += 1
                cursor = cursor.prox
        except TypeError:
            raise ListaError('elemento oferecido difere em tipo do elemento da lista')
        return cont
    
    #------QUESTÃO 3------ 
    def insere_inicio(self, carga:any):
        novo = no(carga)
        if not self.vazia():
            novo.prox = self.__head
        self.__head = novo
        self.__tamanho += 1

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

#teste
if __name__ == '__main__':
    #teste lista sequencial
    teste = lista_encadeada()
    teste.insere_inicio(1)
    teste.insere_final(2)
    teste.insere_final(3)
    teste.insere_final(4)
    teste.insere_final(5)
    print(teste)
    print('-------------')
    teste.insere_inicio(6)
    print(teste)
    print('-------------')
    teste.modifica(3, 10)
    teste.modifica(4, 20)
    print( teste.maiores(10) )