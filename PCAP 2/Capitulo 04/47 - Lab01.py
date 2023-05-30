# Cenário
#
# Escusado será dizer que os sistemas operativos permitem-lhe procurar ficheiros e diretorias. Ao estudar esta parte do curso aprendeu sobre as funções do módulo os, que têm tudo o que precisa para escrever 
# um programa que procurará diretorias num determinado local.
#
# Para facilitar a sua tarefa, preparámos-lhe uma estrutura de diretoria de teste:
#
# Estrutura de diretoria
#
#
# O seu programa deve cumprir os seguintes requisitos:
#
#    Escreve uma função ou método chamado find que toma dois argumentos chamados path e dir. O argumento path deve aceitar um caminho relativo ou absoluto para uma diretoria onde a pesquisa deve começar, 
# enquanto o argumento dir deve ser o nome de uma diretoria que deseje encontrar no caminho dado. O seu programa deve exibir os caminhos absolutos se encontrar uma diretoria com o nome fornecido.
#    A pesquisa de diretoria deve ser feita recursivamente. Isto significa que a pesquisa também deve incluir todas as subdiretorias no caminho dado.
#
# Exemplo de input:
# path="./tree", dir="python"

import os

def find(path, dir):
    for root, dirs, files in os.walk(path):
        if dir in dirs:
            dir_path = os.path.join(root, dir)
            return os.path.abspath(dir_path)
    return None

# Solicitar o diretório ao usuário
path = input("Digite o caminho do diretorio onde deseja iniciar a pesquisa: ")
dir = input("Digite o nome do diretorio que deseja encontrar: ")

result = find(path, dir)
if result:
    print("Caminho absoluto encontrado:", result)
else:
    print("Diretorio nao encontrado.")