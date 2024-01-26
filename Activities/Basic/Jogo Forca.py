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
letras_certas = []
letras_erradas = []

tamanho_palavra = len(set(palavra_sorteada))
palavra_escondida = ''

for letra in palavra_sorteada:
    palavra_escondida += '_'
    
tentativas = 0
print(palavra_sorteada + '\n')
print(palavra_escondida + '\n')

while tentativas <= 5 and (tamanho_palavra != len(letras_certas)):
    
    chute = input('Digite uma letra: ')
    
    if chute in palavra_sorteada:        
        letras_certas.append(chute)
        print(f'\nLetras certas {letras_certas}\n\n')
    else:
        letras_erradas.append(chute)
        print(f'\nLetras erradas {letras_erradas}\n')
        tentativas += 1
        print(f'Erros: {tentativas}')
        
if len(set(palavra_sorteada)) == len(letras_certas):
    print(f'Voce ganhou! A palavra era {palavra_sorteada}')
else:
    print(f'Voce perdeu! A palavra correta era {palavra_sorteada}')
    