
def cadastro(dicionario):
    
    id = input('Digite o ID do candidato: ')
    name = input('Digite o nome do candidato: ')
    
    if id.isdigit() and len(id) == 2:
        db_cadastrados[id] = name
    else: 
        print('\nDados incorretos!')

def votacao():
    voto = input('\nInsira o numero do candidato que deseja votar: ')
    
    if voto in db_cadastrados.keys():
        print(f'Voce esta votando em: {db_cadastrados[voto]}\nDeseja confimar o voto [y]es/[n]o: ')
        
        qty_voto_atual = db_votacao[voto]
        db_votacao[voto] = qty_voto_atual + 1
        
    elif voto == '':
        print('Voto nulo')
        qty_voto_atual = db_votacao['nulo']
        db_votacao['nulo'] = qty_voto_atual + 1
        
    elif voto not in db_cadastrados.keys():
        print('Voce em branco ')
        qty_voto_atual = db_votacao['branco']
        db_votacao['branco'] = qty_voto_atual + 1
    
def criar_db_votacao():    
    # Criar base de votacao iniciando os votos em 0
    db_votacao = {chave: 0 for chave in db_cadastrados}
    db_votacao['branco'] = 0
    db_votacao['nulo'] = 0

db_cadastrados = {}
db_votacao = {}

while True:
    s = input('[v]otar ou [c]adastrar?').lower()
    
    if s == 'c':
        maximo = int(input('\nDigite quantos usuarios ira cadastrar: '))
        contador = 0 
        # Loop para cadastrar sem necessidade de perguntar ao final de cada cadastros se quer cadastrar outra pessoa
        for usuarios in range(0,maximo,1):
            cadastro(db_cadastrados)
            
    elif s == 'v':
        criar_db_votacao()
        
        while True:
            votacao()
            print(db_votacao)
            x = input('\nVotar novamente?').lower()
            if x == 'n':
                break
    else:
        continue
    