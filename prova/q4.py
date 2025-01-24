from lista_sequencial import lista_sequencial
from lista_encadeada import lista_encadeada

class processo:
    def __init__(self, pid, tempo_execucao, prioridade):
        self.pid = pid
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade
    
    def __lt__(self, outro):
        return self.prioridade > outro.prioridade
    
    def __str__(self):
            return f'{self.pid}'
    
class gerenciadorprocessos:
    def __init__(self):
        # self.__jobs = lista_sequencial(15)
        self.__jobs = lista_encadeada()
    
    def add(self, processo:processo):
        self.__jobs.insere_final(processo)
    
    def __executar_proximo_processo(self):
        processo = self.__get_processo()
        if processo != None:
            # print("Tempo ", processo.tempo_execucao)
            if processo.tempo_execucao != 0:
                processo.tempo_execucao -= 1
            else:
                print(f'processo: {processo} foi finalizado')
                indice = self.__jobs.busca_posicao(processo)
                # print(f'indice: {indice}')
                # print("Processo executado: ",  processo)
                self.__jobs.remove(indice)
        else:
            raise Exception('não há elementos a serem executados')

    def __get_processo(self)->processo:
        if self.__jobs.vazia():
            return None
        processo_m = processo(0,0,10)

        for i in range(len(self.__jobs) ):
            if self.__jobs.busca_elemento(i) > processo_m:
                processo_m = self.__jobs.busca_elemento(i)
        
        # print("Processo encontrado: ", processo_m)
        return processo_m

    def simular_tempo(self):
        self.__executar_proximo_processo()

    def __str__(self):
        print("Fila de processos:")
        for i in range(len(self.__jobs) , 0, -1):
            processo = self.__jobs[i]
            print(f"Processo {processo.pid} - Prioridade {processo.prioridade} - Tempo de execução {processo.tempo_execucao}")
        return ""

if __name__ == '__main__':
    gp = gerenciadorprocessos()

    p1 = processo(1, 10, 6)
    p2 = processo(2, 8, 4)
    p3 = processo(3, 6, 2)

    gp.add(p1)
    gp.add(p2)
    gp.add(p3)

    try:
        for _ in range(999):
            gp.simular_tempo()
            # print(gerenciadorprocessos)
    except:
        print('operação finalizada')

