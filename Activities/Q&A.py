# Exercício - sistema de questoes e respostas


questoes = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0

for questao in questoes:
    # Mostra as questoes na tela
    print(f'{questao['Pergunta']}\n')
    
    # Mostra as opcoes na tela
    for indexador, resposta in enumerate(questao['Opções']):
        print(f'{indexador}) {resposta}')
    
    # Recebe resposta usuario
    user_response = int(input('\nEscolha uma opção: '))
    
    # Metodo de verificação
    # Verifica resposta6§95
    if questao['Opções'][user_response] == questao['Resposta']:
        print('Acertou\n')
        acertos += 1
    else:
        print('Errou\n')

# Feedback do jogo
print(f'Voce acertou {acertos} de 3 perguntas')
