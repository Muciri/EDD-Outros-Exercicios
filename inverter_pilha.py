from estruturas.pilha_encadeada import pilha_encadeada

def inverter_pilha(pilha):
    controle = pilha_encadeada()

    for i in range(len(pilha) -1, -1, -1):
        controle.empilha(pilha.busca_elemento(i))

    for i in range(len(pilha)):
        pilha.desempilha()
    
    for i in range(len(controle)):
        pilha.empilha(controle.busca_elemento(i))

pilha = pilha_encadeada()

for i in range(1, 11):
    pilha.empilha(i)

print(pilha)
inverter_pilha(pilha)
print(pilha)
