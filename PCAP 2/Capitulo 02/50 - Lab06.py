# LAB
#
# Tempo estimado
#
# 60-90 minutos
# Nível de dificuldade
#
# Difícil
# Objetivos
#
#    melhorar as competências do aluno em operar com strings e listas;
#    converter strings em listas.
#
# Cenário
#
# Como provavelmente sabe, o Sudoku é um puzzle de colocação de números jogado num tabuleiro 9x9. O jogador tem de preencher o tabuleiro de uma forma muito específica:
#
#    cada linha do tabuleiro deve conter todos os dígitos de 1 a 9 (a ordem não importa)
#    cada coluna do tabuleiro deve conter todos os dígitos de 1 a 9 (novamente, a ordem não importa)
#    cada uma das nove "regiôes" 3x3 (vamos nomeá-las “sub-quadrados”) da tabela deve conter todos os dígitos de 1 a 9.
#
# Se precisar de mais detalhes, pode encontrá-los aqui.
#
# A sua tarefa é escrever um programa que:
#
#     leia 9 linhas do Sudoku, cada uma contendo 9 dígitos (verifique cuidadosamente se os dados introduzidos são válidos)
#     faz o output Yes se o Sudoku for válido, e No caso contrário.
#
# Teste o seu código utilizando os dados por nós fornecidos.
# Dados de teste
#
# Input de amostra:
#
# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672
#
# Exemplo de output:
# Yes
#
#
# Input de amostra:
#
# 195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671
#
# Exemplo de output:
# No

def is_valid_sudoku(sudoku):
    # Verificar as linhas
    for row in sudoku:
        if set(row) != set('123456789'):
            return False

    # Verificar as colunas
    for col in range(9):
        if set([sudoku[row][col] for row in range(9)]) != set('123456789'):
            return False

    # Verificar os sub-quadrados
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if set([sudoku[row][col] for row in range(i, i+3) for col in range(j, j+3)]) != set('123456789'):
                return False

    return True

# Ler as linhas do Sudoku
sudoku = []
for _ in range(9):
    row = input()
    if len(row) != 9 or not row.isdigit():
        print("Invalid input")
        exit()
    sudoku.append(row)

# Verificar se o Sudoku é válido
if is_valid_sudoku(sudoku):
    print("Yes")
else:
    print("No")