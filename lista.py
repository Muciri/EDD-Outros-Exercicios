from estruturas.lista_encadeada import no, ListaError

def insere_elemento(self, carga):
    novo = no(carga)
    if self.vazia():
        self.__head = novo
    else:
        cursor = self.__head
        while cursor.prox != None:
            cursor = cursor.prox
        cursor.prox = novo
    self.__tamanho += 1

def remover_elemento(self, num):
    if self.vazia():
        raise ListaError('a lista está vazia')
    if num < 0 or num > self.__tamanho:
        raise ListaError('valor inválido')
    cursor = self.__head
    for i in range(num-1):
        cursor = cursor.prox
    cursor.prox = cursor.prox.prox

def encontrar_elemento(self, num):
    if self.vazia():
        raise ListaError('a lista está vazia')
    if num < 0 or num > self.__tamanho:
        raise ListaError('valor inválido')
    cont = 0 
    cursor = self.__head
    for i in range(num):
        cursor = cursor.prox
    return cursor.carga

def alterar_elemento(self, num, elemento):
    if num < 0 or num > self.__tamanho:
        raise ListaError('valor inválido')
    cursor = self.__head
    for i in range(num):
        cursor = cursor.prox
    cursor.carga = elemento