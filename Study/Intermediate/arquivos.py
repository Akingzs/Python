# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

path_file = r'C:\Users\arthur.oliveira\OneDrive\Study\Python - Course\Python\Study\Intermediate\wk_w_files'
file_name = r'\arquivo.txt'
full_path = path_file+file_name

file = open(full_path,'w')
file.close()

# Context manager - with (abre e fecha) automaticamente
with open(full_path,'w') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
# arquivo = open(caminho_arquivo, 'w')
# #
# # arquivo.close()
# with open(full_path, 'w') as arquivo:
#     print('Olá mundo')
#     print('Arquivo vai ser fechado')

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load