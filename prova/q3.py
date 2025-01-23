from pilha_encadeada import pilha_encadeada, PilhaError

class DNS:
    def __init__(self):
        self.__urls = {"ifpb":"192.168", "google": "10.10", "g1": "19.17", "uol":"1.10"}
    
    @classmethod
    def add(cls, url:str, ip:str):
        cls.__urls[url] = ip
    
    @classmethod
    def existsurl(cls, url:str)->bool:
        return url in cls.__urls.keys()
    
class Browser:
    def __init__(self):
        self.__historico = pilha_encadeada()
        self.__home = None
    
    def request(self, url:str)->bool:
        urls = DNS()

    def back(self):
        if not len(self.__historico) == 1 and not self.__historico.vazia():
            self.__historico.desempilha()
        else:
            print('não há página a se retornar')

    def __str__(self):
        paginas = '['
        for i in range(len(self.__historico)):
            paginas += f'{self.__historico.busca_elemento(i)} >'
        paginas = paginas.rstrip('> ') + ']'
        return f'{paginas} \nhome: {self.__home}'

url = DNS()
safari = Browser()
print(safari)
safari.back()
print(safari)