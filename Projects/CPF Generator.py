# Coletar 9 primeiros digitos do CPF

cpf = '74682489.0'
# cpf = input('Digite os 9 primeiros digitos do CPF: ')

if cpf.__contains__('.'):
    cpf_corrigido = cpf.replace('.','')
else:
    pass

# 1 digito 
# Loop para somar todos os numeros do CPF 
# multiplicados pela contagem regressiva de 10
soma1 = 0
for index, digito in enumerate(cpf_corrigido):
    soma1 += int(digito) * (10 - index)
    
# Multiplicar por 10 e Resto da div por 11
resto_div = (soma1 * 10) % 11

primeiro_dig = 0 if resto_div > 9 else resto_div

cpf_corrigido = cpf_corrigido + str(primeiro_dig)

# 2 digito 
# Loop para somar todos os numeros do CPF 
# multiplicados pela contagem regressiva de 10
soma2 = 0
for index, digito in enumerate(cpf_corrigido):
    soma2 += int(digito) * (11 - index)
    
# Multiplicar por 10 e Resto da div por 11
resto_div2 = (soma2 * 10) % 11

segundo_dig = 0 if resto_div2 > 9 else resto_div2

cpf_corrigido = cpf_corrigido + str(segundo_dig)

print(cpf_corrigido)