""" Calculadora com while """
while True:
    print('\n****************')
    
    try:  
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digite o segundo numero: '))
        operator = input('Digite o segundo numero: ')
        print(eval(
            f'{num1} {operator} {num2}'
        ))
    except:
        print('\nVoce não digitou um numero valido \n\n')
    
    #########
    sair = input('Quer sair? [s]im / [n]ão: ').lower().startswith('s')
    
    if sair is True:
        break
    
    # Com ifs  
    # if operator == '+':
    #     print(num1 + num2)
    # elif operator == '-':
    #     print(num1 - num2)
    # elif operator == '*':
    #     print(num1 * num2)S
    # elif operator == '/':
    #     print(num1 / num2)