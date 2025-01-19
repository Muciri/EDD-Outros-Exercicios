from estruturas.pilha_encadeada import PilhaError, no

def inserir_elemento(self, carga):
    self.__topo += 1
    novo = no(carga)
    novo.prox = self.__head
    self.__head = novo

def remove_elemento(self):
    if self.vazia():
        raise PilhaError('a pilha está vazia')
    elemento = self.__head.carga
    self.__head = self.__head.prox
    return elemento

def busca_elemento(self, num):
    cursor = self.__head
    for i in range(num):
        cursor = cursor.prox
        if cursor == None:
            raise PilhaError('elemento não encontrado')
    return cursor.carga

#não da pra testar aqui pq o self.__head é privado, mas eu colei na fila, testei e deu green :)