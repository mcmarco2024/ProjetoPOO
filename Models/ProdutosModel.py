from uuid import uuid4

class Produto():
    def __init__(self):
        self.__id = str(uuid4())
        self.__name = ''
        self.__quantidade = ''
        self.__preco = ''
        
    def set_prod(self, nome, quant, preco):
        self.__name = nome
        self.__quantidade = quant
        self.__preco = preco

    def get_nome(self):
        return self.__name
    
    def get_quantidade(self):
        return self.__quantidade
    
    def get_preco(self):
        return self.__preco
    
    def get_id(self):
        return self.__id