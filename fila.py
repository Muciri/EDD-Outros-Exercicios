from estruturas.fila_encadeada import no, FilaError

def imprime_elementos(self):
    if self.vazia():
        return '||'
    else:
        elementos = '|>'
        cursor = self.__head.frente
        while cursor != None:
            elementos += f'{cursor.carga}, '
            cursor = cursor.prox
        elementos = elementos.rstrip(', ') + '<|'
        return elementos
    
def inserir_elemento(self, carga):
    novo = no(carga)
    if self.vazia():
        self.__head.frente = self.__head.fim = novo
    else:
        self.__head.fim.prox = novo
        self.__head.fim = novo
    self.__head.tamanho += 1

def remover_elemento(self):
    if self.vazia():
        raise FilaError('a pilha está vazia')
    self.__head.frente = self.__head.frente.prox

#não da pra testar aqui pq o self.__head é privado, mas eu colei na fila, testei e deu green :)