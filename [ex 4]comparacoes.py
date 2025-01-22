from estruturas.lista_encadeada import lista_encadeada, ListaError, no

def uniao(lista1, lista2):
    lista_n = lista_encadeada()
    
    for i in range(len(lista1)):
        lista_n.insere_final(lista1.busca_elemento(i))
    
    for i in range(len(lista2)):
        lista_n.insere_final(lista2.busca_elemento(i))
    
    return lista_n

def intersecao(lista1, lista2):
    lista_n = lista_encadeada()
    for i in range(len(lista1)):
        try:
            lista_n.insere_final( lista2.busca( lista1.busca_elemento(i) ) )
        except ListaError:
            pass
    return lista_n

def diferenca(lista1, lista2):
    lista_n = lista_encadeada()
    for i in range(len(lista1)):
        try:  
            lista2.busca( lista1.busca_elemento(i) )
        except ListaError:
            lista_n.insere_final(lista1.busca_elemento(i))
    
    return lista_n

if __name__ == '__main__':
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
    print(uniao(lista1, lista2))

    print('interseção das listas:')
    print(intersecao(lista1, lista2))

    print('diferença das listas:')
    print(f'diferença da lista1 para a lista2: {diferenca(lista1, lista2)}')
    print(f'diferença da lista2 para a lista1: {diferenca(lista2, lista1)}')