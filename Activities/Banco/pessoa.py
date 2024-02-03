from abc import ABC, abstractmethod    
    
class Pessoa(ABC):
    
    def __init__(self, nome: str, idade:int) -> None:
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade