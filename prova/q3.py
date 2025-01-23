from pilha_encadeada import pilha_encadeada, PilhaError

class DNS:
    def __init__(self):
        self.__urls = {"ifpb":"192.168", "google": "10.10", "g1": "19.17", "uol":"1.10"}
    
    # @classmethod
    # def add(cls, url:str, ip:str):
    #     cls.__urls[url] = ip
    
    # @classmethod
    # def existsurl(cls, url:str)->bool:
    #     return url in cls.__urls.keys()
    
    def add(self, url:str, ip:str):
        self.__urls[url] = ip
    
    def existsurl(self, url:str)->bool:
        return url in self.__urls.keys()
    
class Browser:
    def __init__(self):
        self.__historico = pilha_encadeada()
        self.__home = None
    
    def request(self, url:str)->bool:
        dns = DNS()
        if dns.existsurl(url):
            # if not len(self.__historico) == 0:
            if not self.__home == None:
                self.__historico.empilha(self.__home)
            self.__home = url
        else:
            pass

    def back(self):
        if not self.__historico.vazia():
            self.__home = self.__historico.desempilha()
        
        elif self.__historico.vazia() and self.__home != None:
            self.__home = None
        
        else:
            print('não há página a se retornar')

    def __str__(self):
        paginas = '['
        for i in range(len(self.__historico)):
            paginas += f'{self.__historico.busca_elemento(i)} > '
        paginas = paginas.rstrip('> ') + ']'
        return f'{paginas} \nhome: {self.__home}'

if __name__ == '__main__':
    url = DNS()
    safari = Browser()
    print(safari)
    safari.request('ifpb')
    print(safari)
    safari.back()
    print(safari)
    safari.request('google')
    print(safari)
    safari.request('g1')
    print(safari)
    safari.request('naoexiste')
    print(safari)
    safari.request('uol')
    print(safari)
    safari.back()
    print(safari)
    safari.back()
    print(safari)