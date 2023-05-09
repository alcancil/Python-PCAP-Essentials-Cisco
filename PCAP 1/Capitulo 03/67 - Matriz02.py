# Listas em listas: arrays bidimensionais - continuação
# O acesso ao campo selecionado do tabuleiro requer dois índices - o primeiro seleciona a linha; o segundo - o número do campo dentro da linha, que é de facto um número de coluna.
#
# Dê uma vista de olhos no tabuleiro de xadrez. Cada campo contém um par de índices que devem ser dados para aceder ao conteúdo do campo:
#
#
#
#
# Olhando para a figura mostrada acima, vamos colocar algumas peças de xadrez no tabuleiro. Primeiro, vamos adicionar todas as torres (em inglês, rooks):
#
# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
#
#
# Se quiser acrescentar um cavaleiro (knight) ao C4, faça-o da seguinte forma:
#
# board[4][2] = KNIGHT
#
#
# E agora um peão (pawn) para E5:
# 
# board[3][4] = PAWN
#
#
# E agora - experimente o código no editor.

EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)