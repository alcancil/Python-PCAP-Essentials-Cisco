# Algumas funções simples: continuação
#
# Vamos agora brincar com triângulos. Vamos começar com uma função para verificar se três lados de determinados comprimentos podem construir um triângulo.
# Um triângulo com lados iguais
#
# Sabemos da escola que a soma de dois lados arbitrários tem de ser mais longa do que o terceiro lado.
#
# Não será um desafio difícil. A função terá três parâmetros - um para cada lado.
#
# Ela vai devolver True se os lados puderem construir um triângulo, e False caso contrário. Neste caso, is_a_triangle é um bom nome para tal função.
#
# Veja o código no editor. Pode encontrar aí a nossa função. Execute o programa.
#
#
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


#
# Parece que funciona bem - estes são os resultados:
# True
# False
#
# output
#
# Podemos torná-lo mais compacto? Parece um pouco palavroso.
#
# Esta é uma versão mais compacta:

def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Podemos compactá-lo ainda mais?
#
# Sim, podemos - veja:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Negámos a condição (invertemos os operadores relacionais e substituímos orpor and, recebendo uma expressão universal para testar triângulos).
#
# Vamos instalar a função num programa maior. Vai pedir ao utilizador três valores e fará uso da função.
