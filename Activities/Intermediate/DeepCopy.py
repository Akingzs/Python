import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#1 copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

def raise_prices(lista_produtos):
    temp_produtos_aumento = copy.deepcopy(lista_produtos)
    for produto in temp_produtos_aumento:
        produto['preco'] *= 1.1
    return temp_produtos_aumento



#2 Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


#3 Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = raise_prices(produtos)

# for produto in novos_produtos:
#     print(produto)

produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda d: d['nome'])
produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda d: d['preco'])

for item in produtos_ordenados_por_preco:
    print(item)
print()
for item in novos_produtos:
    print(item)
