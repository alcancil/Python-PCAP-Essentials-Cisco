# Funções selecionadas a partir do módulo math : continuação
#
# O último grupo é constituído por algumas funções de caráter geral, como por exemplo:
#
#    ceil(x) → o teto de x (o menor inteiro maior ou igual a x)
#    floor(x) → o piso de x (o maior número inteiro menor ou igual a x)
#    trunc(x) → o valor de x truncado a um número inteiro (tenha cuidado - não é equivalente a um teto ou piso)
#    factorial(x) → devolve x! (x tem de ser um integral e não um negativo)
#    hypot(x, y) → devolve o comprimento da hipotenusa de um triângulo de ângulo retângulo com o comprimento das pernas igual a x e y (o mesmo que sqrt(pow(x, 2) + pow(y, 2)) mas mais preciso)
#
# Veja o código no editor. Analise o programa com cuidado.
#
# Demonstra as diferenças fundamentais entre ceil(), floor() e trunc().
#
# Execute o programa e verifique o seu output.

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))