from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

    @abstractmethod
    def gerar_recibo(self):
        pass

class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} no cartão.")
        return valor

    def gerar_recibo(self):
        print("Gerando recibo para pagamento com cartão.")

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} no boleto.")

    def gerar_recibo(self):
        print("Gerando recibo para pagamento com boleto.")


pag_cartao2 = PagamentoCartao().processar_pagamento(5000)
pag_cartao1 = PagamentoCartao()