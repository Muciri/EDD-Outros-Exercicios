from estruturas.fila_encadeada import fila_encadeada

def concatenar_filas(fila1, fila2):
    fila_controle = fila_encadeada()

    for i in range(len(fila1)):
        fila_controle.enfileira(fila1.desenfileira())

    for i in range(len(fila2)):
        fila_controle.enfileira(fila2.busca_elemento(i))

    for i in range(len(fila_controle)):
        fila1.enfileira(fila_controle.desenfileira())


fila1 = fila_encadeada()
fila2 = fila_encadeada()

for i in range(5):
    letras = 'abcde'
    fila1.enfileira(letras[i])

for i in range(5):
    fila2.enfileira(i)

print(f'fila1: {fila1}')
print(f'fila2: {fila2}')
print('concatenando...')
concatenar_filas(fila1, fila2)
print(f'fila1: {fila1}')
print(f'fila2: {fila2}')