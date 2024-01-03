nome = 'Arthur'
maximo = len(nome)
letras = 0
novo_nome = ''

# while letras < maximo:
#     print(nome[letras])
#     letras += 1
# print('Fim') 

while letras < maximo:
    novo_nome += "*" + nome[letras]
    if letras == (maximo - 1):
        novo_nome += "*"
    letras += 1
    
print(novo_nome)