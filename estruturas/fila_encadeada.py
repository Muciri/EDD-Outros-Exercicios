class FilaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

class no:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None

class controle:
    def __init__(self):
        self.frente = None
        self.fim = None
        self.tamanho = 0

class fila_encadeada:
    #CONSTRUTOR
    def __init__(self):
        self.__head = controle()
    
    #MÉTODOS ESPECIAIS
    def __str__(self):
        if self.vazia():
            return '||'
        fila = '|>'
        cursor = self.__head.frente
        while(cursor != None):
            fila += f'{cursor.carga}, '
            cursor = cursor.prox

        fila = fila.rstrip(', ') + '<|' 
        return fila
    
    def __len__(self):
        return self.__head.tamanho
    
    #MÉTODOS DE CONTROLE
    def vazia(self):
        return self.__head.tamanho == 0
    
    def frente(self):
        if self.vazia():
            raise FilaError("a fila está vazia")
        return self.__head.frente.carga        
    
    #MÉTODOS GERAIS
    def enfileira(self, carga:any):
        novo = no(carga)
        if self.vazia():
            self.__head.frente = self.__head.fim = novo
        else:
            self.__head.fim.prox = novo
            self.__head.fim = novo
        self.__head.tamanho += 1

    def desenfileira(self):
        if self.vazia():
            raise FilaError("a fila está vazia")
        elemento = self.__head.frente.carga
        if len(self) == 1:
            self.__head.frente = self.__head.fim = None
        else:
            self.__head.frente = self.__head.frente.prox
        self.__head.tamanho -= 1
        return elemento  
        
    def busca(self, elemento):
        cursor = self.__head.frente
        while (cursor != None):
            if cursor.carga == elemento:
                return cursor.carga
            cursor = cursor.prox
        raise FilaError(f'{elemento} não encontrado na fila')
    
    def busca_elemento(self, num:int):
        if num < 0 or num >= self.__head.tamanho:
            raise FilaError("valor fora do intervalo")
        cont = 0
        cursor = self.__head.frente
        while cont != num:
            cursor = cursor.prox
            cont += 1
        return cursor.carga
    
    def busca_posicao(self, elemento):
        cont = 0
        cursor = self.__head.frente
        while (cursor != None):
            if cursor.carga == elemento:
                return cont
            cursor = cursor.prox
            cont += 1
        return -1
    
#teste
if __name__ == '__main__':
    teste = fila_encadeada()
    teste.enfileira('1')
    teste.enfileira('2')
    teste.enfileira('3')
    teste.enfileira('4')
    teste.enfileira('5')
    print(teste)
    teste.desenfileira()
    teste.desenfileira()
    print(teste)

    print(teste.busca_elemento(0))
    print(teste.busca_elemento(1))
    print(teste.busca_elemento(2))

    print(teste.busca('3'))
    print(teste.busca('4'))

    print(teste.busca_posicao('3'))
    print(teste.busca_posicao('4'))