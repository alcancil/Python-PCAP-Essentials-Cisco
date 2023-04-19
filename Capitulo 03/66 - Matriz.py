# Listas em listas: arrays bidimensionais
# Vamos também assumir que um símbolo pré-definido chamado EMPTY designa um campo vazio no tabuleiro de xadrez.
# 
# Assim, se quisermos criar uma lista de listas representando todo o tabuleiro de xadrez, isso pode ser feito da seguinte forma:
# 
# board = []
#
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
#
#
# Nota:
#
# a parte interior do loop cria uma linha composta por oito elementos (cada um deles igual a EMPTY) e anexa-o à lista board ;
# a parte externa repete-o oito vezes;
# no total, a lista board consiste em 64 elementos (todos iguais a EMPTY)
# Este modelo imita perfeitamente o verdadeiro tabuleiro de xadrez, que é de facto uma lista de oito elementos, sendo todos eles filas únicas. Vamos resumir as nossas observações:
#
# os elementos das filas são campos, oito deles por fila;
# os elementos do tabuleiro de xadrez são linhas, oito delas por tabuleiro de xadrez.
# A variável board é agora um array bidimensional. Também é chamada, por analogia aos termos algébricos, uma matriz.
#
#
# Como as compreensões de lista podem ser nested, podemos encurtar a criação do tabuleiro da seguinte forma:
#
# board = [[EMPTY for i in range(8)] for j in range(8)]
#
#
# A parte interior cria uma fila, e a parte exterior constrói uma lista de filas.


EMPTY = "-"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

print(board)

board = [[EMPTY for i in range(8)] for j in range(8)]
print(board)