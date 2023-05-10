# Funções selecionadas a partir do módulo math : continuação
#
# Outro grupo das funções de mathé formado por funções que estão ligadas à exponenciação:
#
#    e → uma constante com um valor que é uma aproximação do número de Euler (e)
#    exp(x) → encontrar o valor de ex;
#    log(x) → o logaritmo natural de x
#    log(x, b) → o logaritmo de x para base b
#    log10(x) → o logaritmo decimal de x (mais preciso do que log(x, 10))
#    log2(x) → o logaritmo binário de x (mais preciso do que log(x, 2))
#
# Nota: a função pow() .
#
#    pow(x, y) → encontrar o valor de xy (atenção aos domínios)
#
# Esta é uma função integrada, e não tem de ser importada.
#
# Veja o código no editor. Consegue prever o seu output?
#
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
