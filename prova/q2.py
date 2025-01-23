from pilha_encadeada import pilha_encadeada

def reverse_words(frase:str):
    pilha = pilha_encadeada()
    frase_m = ''
    for i in frase:
        pilha.empilha(i)
    for i in range(len(pilha)):
        frase_m += pilha.busca_elemento(i)

    return(frase_m)


novafrase = reverse_words('Fila e Pilha encadeada ')
print(novafrase)