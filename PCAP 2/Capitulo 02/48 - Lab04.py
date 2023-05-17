# LAB
#
# Tempo estimado
#
# 15-30 minutos
# Nível de dificuldade
#
# Fácil
# Objetivos
#
#    melhorar as habilidades do aluno a operar com strings;
#    converter inteiros em strings, e vice-versa.
#
# Cenário
#
# Alguns dizem que o Dígito da Vida é um dígito avaliado usando o aniversário de alguém. É simples - basta somar todos os dígitos da data. Se o resultado contiver mais do que um dígito, terá de repetir a 
# # adição até obter exatamente um dígito. Por exemplo:
#
#    1 de janeiro de 2017 = 2017 01 01
#    2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
#    1 + 2 = 3
#
# 3 é o dígito que procurámos e encontrámos.
#
# A sua tarefa é escrever um programa que:
#
#    pergunta ao utilizador o seu aniversário (no formato AAAAMMDD, ou AAAADDMM, ou MMDDAAAA - na verdade, a ordem dos dígitos não importa)
#    faz output do Dígito de Vida para a data.
#
# Teste o seu código utilizando os dados por nós fornecidos.
# Dados de teste
#
# Input de amostra:
# 19991229
#
# Exemplo de output:
# 6
#
#
# Input de amostra:
# 20000101
#
# Exemplo de output:
# 4

def digito_de_vida(data):
    while len(data) > 1:
        soma = sum(int(digito) for digito in data)
        data = str(soma)
    return int(data)

aniversario = input("Digite seu aniversário (AAAAMMDD ou AAAADDMM ou MMDDAAAA): ")
digito = digito_de_vida(aniversario)
print("O dígito de vida para", aniversario, "é", digito)