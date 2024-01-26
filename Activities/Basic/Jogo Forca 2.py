"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import random

lista_palavras = ['maça','pera','uva','banana']
palavra_sorteada = random.choice(lista_palavras)
letras_certas = ''
letras_erradas = ''

tentativas = 0
 
while True:
    
    chute = input('Digite uma letra: ')
    
    if chute in palavra_sorteada:        
        letras_certas += chute
    else:
        letras_erradas += chute
        tentativas += 1
        print(f'Erros: {tentativas}\n')
        
    palavra_escondida = '' 
    for letra_secreta in palavra_sorteada:
        if letra_secreta in letras_certas:
            palavra_escondida += letra_secreta
        else:
            palavra_escondida += '*'
            
    print(palavra_escondida)         
            
    if palavra_sorteada == palavra_escondida:
        print(f'Voce ganhou! A palavra era {palavra_sorteada}\n')
        break
    elif tentativas == 5:
        print(f'Voce perdeu! A palavra correta era {palavra_sorteada}\n')
        break
