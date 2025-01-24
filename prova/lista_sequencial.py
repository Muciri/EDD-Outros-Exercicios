import numpy as np

class ListaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

class lista_sequencial:
    #CONSTRUTOR
    def __init__(self, tamanho: int):
        self.__dados = np.full(tamanho, None)
        self.__fim = -1
        self.__tamanho = 0
    
    #MÉTODOS ESPECIAIS
    def __str__(self):
        if self.vazia():
            return '[]'
    
        lista = '['
        for i in range(self.__tamanho):
            if self.__dados[i] != None:
                lista += f'{self.__dados[i]}, '
        lista = lista.rstrip(', ') + ']' 
        return lista
    
    def __len__(self):
        return self.__tamanho
    
    #MÉTODOS DE CONTROLE
    def cheia(self):
        return self.__tamanho == len(self.__dados)
    
    def vazia(self):
        return self.__tamanho == 0
    
    #MÉTODOS GERAIS
    def insere(self, num:int, carga:any):
        if self.cheia():    
            raise ListaError("a lista está cheia")  
        for i in range(num, self.__tamanho):
            self.__dados[i] = self.__dados[i + 1]
            print( self.__dados[i] )
        self.__dados[num] = carga

    def insere_final(self, carga:any):
        if self.cheia():    
            raise ListaError("a lista está cheia")    
        self.__fim += 1 
        self.__dados[self.__fim] = carga
        self.__tamanho += 1

    def remove(self, num):
        if self.vazia():
            raise ListaError("a lista está vazia")
        if num < 0 or num >= self.__tamanho:
            raise ListaError("valor fora do intervalo")
        for i in range(num, self.__tamanho - 1):
            self.__dados[i] = self.__dados[i + 1]
        self.__dados[self.__tamanho - 1] = None
        self.__tamanho -= 1
        self.__fim -= 1
    
    def modifica(self, num, carga):
        if num < 0 or num >= self.__tamanho:
            raise ListaError("valor fora do intervalo")
        self.__dados[num] = carga

    def busca(self, elemento):
        for i in range(len(self)):
            if self.__dados[i] == elemento:
                return self.__dados[i]  
        raise ValueError(f"Elemento {elemento} não encontrado na lista") 

    def busca_elemento(self, num):
        if num < 0 or num >= self.__tamanho:
            raise ListaError("valor fora do intervalo")
        return self.__dados[num]
    
    def busca_posicao(self, elemento):
        for i in range(self.__tamanho):
            if self.__dados[i] == elemento:
                return i
        return -1

#teste
if __name__ == '__main__':
    #teste lista sequencial
    teste = lista_sequencial(10)
    teste.insere_final('1')
    teste.insere_final('2')
    teste.insere_final('3')
    teste.insere_final('4')
    teste.insere_final('5')
    print(teste)
    # teste.modifica(3, '10')
    # teste.modifica(4, '20')
    teste.insere(1, '1.5')
    teste.insere(3, '3.5')
    print(teste)
    teste.remove(1)
    teste.remove(2)
    print(teste)

    print(teste.busca_elemento(0))
    print(teste.busca_elemento(1))
    print(teste.busca_elemento(2))

    # print(teste.busca('1'))
    # print(teste.busca('3'))


    print(teste.busca_posicao('3'))
    print(teste.busca_posicao('4'))