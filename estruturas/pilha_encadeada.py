class PilhaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

class no:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None

class pilha_encadeada:
    #CONSTRUTOR
    def __init__(self):
        self.__head = None
        self.__topo = -1
    
    #MÉTODOS ESPECIAIS
    def __str__(self):
        if self.vazia():
            return '||'
        pilha = '|>'
        cursor = self.__head
        while(cursor != None):
            pilha += f'{cursor.carga}, '
            cursor = cursor.prox

        pilha = pilha.rstrip(', ') + '|' 
        return pilha
    
    def __len__(self):
        return self.__topo + 1
    
    #MÉTODOS DE CONTROLE
    def vazia(self):
        return self.__topo == -1
    
    def topo(self):
        if self.vazia():
            raise PilhaError("a pilha está vazia")
        return self.__head.carga         
    
    #MÉTODOS GERAIS
    def empilha(self, carga:any):
        self.__topo += 1
        novo = no(carga)
        novo.prox = self.__head
        self.__head = novo

    def desempilha(self):
        if self.vazia():
            raise PilhaError("a pilha está vazia")
        self.__topo -= 1
        elemento = self.__head.carga
        self.__head = self.__head.prox
        return elemento  
        
    def busca(self, elemento):
        cursor = self.__head
        while (cursor != None):
            if cursor.carga == elemento:
                return cursor.carga
            cursor = cursor.prox
        raise PilhaError(f'{elemento} não encontrado na pilha')
    
    def busca_elemento(self, num:int):
        if num < 0 or num > self.__topo:
            raise PilhaError("valor fora do intervalo")
        cont = 0
        cursor = self.__head
        while cont != num:
            cursor = cursor.prox
            cont += 1
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
    teste = pilha_encadeada()

    teste.empilha('1')
    teste.empilha('2')
    teste.empilha('3')
    teste.empilha('4')
    teste.empilha('5')
    print(teste)
    teste.desempilha()
    teste.desempilha()
    print(teste)

    print(teste.busca_elemento(0))
    print(teste.busca_elemento(2))
    print(teste.busca('3'))

    print(teste.busca_posicao('3'))
    print(teste.busca_posicao('4'))

    print(f'topo: {teste.topo()}')
