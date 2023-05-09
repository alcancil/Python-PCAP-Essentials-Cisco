# LAB
#
# Tempo estimado
# 5 minutos
#
# Nível de dificuldade
# Muito fácil
#
# Objetivos
# Familiarizar o aluno a:
# 
# utilizar instruções básicas relacionadas com listas;
# criar e modificar listas.
# Cenário
# Houve uma vez um chapéu. O chapéu não continha nenhum coelho, mas uma lista de cinco números: 1, 2, 3, 4, e 5.
#
# A sua tarefa é:
#
# escrever uma linha de código que peça ao utilizador para substituir o número médio na lista por um número inteiro introduzido pelo utilizador (Passo 1)
# escrever uma linha de código que remova o último elemento da lista (Passo 2)
# escrever uma linha de código que imprima o comprimento da lista existente (Passo 3).
# Pronto para este desafio?

chapeu = [1, 2, 3, 4, 5]

# Pergunta ao usuário que numero inteiro ele quer para que
# Se coloque no lugar do elemento central da lista

num = input ("Digite um numero inteiro para substituir o elemento central da lista : ")

# Imprima o tamanho da lista
print("\nA lista possui ", len(chapeu), "elementos")

chapeu[2] = int(num)
print(chapeu)

# Remova o último elemnto da lista
del chapeu[4]
print(chapeu)

# Imprima o tamanho da lista
print("A lista possui ", len(chapeu), "elementos")
