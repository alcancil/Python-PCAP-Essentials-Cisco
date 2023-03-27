# Os operadores e as suas ligações
# A ligação do operador determina a ordem dos cálculos efetuados por alguns operadores com igual prioridade, colocados lado a lado numa só expressão.
#
# A maioria dos operadores de Python têm ligação do lado esquerdo, o que significa que o cálculo da expressão é realizado da esquerda para a direita.
#
# Este exemplo simples mostrar-lhe-á como funciona. Veja:
#
print(9 % 6 % 2)
#
# Há duas formas possíveis de avaliar esta expressão:
#
# da esquerda para a direita: primeiro 9 % 6 dá 3e, em seguida, 3 % 2 dá 1;
# da direita para a esquerda: primeiro 6 % 2 dá 0e, em seguida, 9 % 0 causa um erro fatal.
#
# Execute o exemplo e veja o que obtém.
#
# O resultado deve ser 1. Este operador tem ligação do lado esquerdo. Mas há uma exceção interessante.

print(2 ** 2 ** 3)

# Resultado será 256

