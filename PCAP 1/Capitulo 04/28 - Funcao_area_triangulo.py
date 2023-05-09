# Algumas funções simples: avaliar a área de um triângulo
# 
# Também podemos avaliar a área de um triângulo. A fórmula de Heron será útil aqui:
# s = (a + b + c) / 2
# 
# A = raiz quadrada de s(s - a)(s - b)(s - c)
#
# Vamos usar o operador de exponenciação para encontrar a raiz quadrada - pode parecer estranho, mas funciona:
# A raiz quadrada de x = x à potência de 1/2
#
# Este é o código resultante:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))


# Tentamo-lo com um triângulo retângulo como metade de um quadrado com um lado igual a 1. Isto significa que a sua área deve ser igual a 0,5.
#
# É estranho - o código produz o seguinte output:
# 0.49999999999999983
#
# output
#
# É muito perto de 0,5, mas não é exatamente 0,5. O que significa isto? É um erro?
#
# Não, não é. Estas são as especificidades dos cálculos de floating-point. Em breve, contar-lhe-emos mais sobre o assunto.