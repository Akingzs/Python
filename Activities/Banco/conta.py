from abc import ABC, abstractmethod
import random

class Conta(ABC):
    
    def __init__(self, limite_conta: int | float = 0) -> None:
        self._limite_conta = limite_conta
        self._agencia = 0 #random.randint(0,1)
        self._numero_conta = random.randint(1000,9999)
    
    @abstractmethod
    def sacar(self, valor_saque: int | float):
        self._limite_conta -= valor_saque
        return self._limite_conta 
    
    @abstractmethod
    def depositar(self, valor_deposito: int | float):
        self._limite_conta += valor_deposito
        return self._limite_conta 