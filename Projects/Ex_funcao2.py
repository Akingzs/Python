
def criar_multi(multiplicador):
    def multiplicadora(numero):
        return multiplicador * numero
    return multiplicadora

multiplicador5 = criar_multi(5)
multiplicador7 = criar_multi(7)

print(multiplicador5(5))
print(multiplicador7(7))