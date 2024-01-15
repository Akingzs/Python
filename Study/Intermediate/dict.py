# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

##### NAO SUPORTA INDEXAÇÃO POR INTEIROS EX ERRADO: DICIONARIO[0] X EX CERTO: DICIONARIO['NOME DA CHAVE']

dicionario = {
    'nome': 'Arthur',
    'sobre': 'Reis'
}

for chave in dicionario.keys():
    print(chave)
# print(dicionario.keys())