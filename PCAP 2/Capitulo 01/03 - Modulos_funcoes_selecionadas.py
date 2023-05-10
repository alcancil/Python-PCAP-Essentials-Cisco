# Funções selecionadas a partir do módulo math .
#
# Vamos começar com uma rápida pré-visualização de algumas das funções fornecidas pelo módulo math .
#
# Escolhemo-los arbitrariamente, mas isso não significa que as funções que não mencionamos aqui sejam menos significativas. Mergulhe você mesmo nas profundezas dos módulos - não temos aqui espaço nem tempo 
# para falar de tudo em pormenor.
#
# O primeiro grupo das funções de mathestão relacionadas com trigonometria:
#
#     sin(x) → o seno de x;
#     cos(x) → o cosseno de x;
#     tan(x) → a tangente de x.
#
# Todas estas funções tomam um argumento (uma medição angular expressa em radianos) e devolvem o resultado apropriado (tenha cuidado com tan() - nem todos os argumentos são aceites).
#
# Naturalmente, existem também as suas versões invertidas:
#
#    asin(x) → o arco-seno de x;
#    acos(x) → o arco-cosseno de x;
#    atan(x) → o arco-tangente de x.
#
# Estas funções tomam um argumento (atenção aos domínios) e devolvem uma medida de um ângulo em radianos.
#
# Para operar eficazmente em medições de ângulos, o módulo math fornece-lhe as seguintes entidades:
#
#    pi → uma constante com um valor que é uma aproximação de π;
#    radians(x) → uma função que converte x de graus para radianos;
#    degrees(x) → atuando na outra direção (dos radianos aos graus)
#
# Agora veja o código no editor. O programa de exemplo não é muito sofisticado, mas consegue prever os seus resultados?
#
# Além das funções circulares (listadas acima) o módulo math também contém um conjunto dos seus análogos hiperbólicos:
#
#    sinh(x) → o seno hiperbólico;
#    cosh(x) → o cosseno hiperbólico;
#    tanh(x) → a tangente hiperbólica;
#    asinh(x) → o arco-seno hiperbólico;
#    acosh(x) → o arco-cosseno hiperbólico;
#    atanh(x) → o arco-tangente hiperbólico.

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
