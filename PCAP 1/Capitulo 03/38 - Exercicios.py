# Key takeaways
#
# 1. O Python suporta os seguintes operadores lógicos:
#
# and → se ambos os operandos forem verdadeiros, a condição é verdadeira, por exemplo, (True and True) é True,
# or → se algum dos operandos for verdadeiro, a condição é verdadeira, por exemplo, (True or False) é True,
# not → retorna falso se o resultado for verdadeiro, e retorna verdadeiro se o resultado for falso, por exemplo, not True é False.
# 2. Pode utilizar operadores bitwise para manipular bits únicos de dados. Os seguintes dados de amostra:
# 
# x = 15, que é 0000 1111 em binário,
# y = 16, que é 0001 0000 em binário.
# serão utilizados para ilustrar o significado de operadores bitwise em Python. Analise os exemplos em baixo:
# 
# & faz um bitwise and, por exemplo, x & y = 0, que é 0000 0000 em binário,
# | faz um bitwise ou, por exemplo, x | y = 31, que é 0001 1111 em binário,
# ˜  faz um bitwise não, por exemplo, ˜ x = 240*, que é 1111 0000 em binário,
# ^ faz um bitwise xor, por exemplo, x ^ y = 31, que é 0001 1111 em binário,
# >> faz um bitwise right shift, por exemplo, y >> 1 = 8, que é 0000 1000 em binário,
# << faz um bitwise left shift, por exemplo, y << 3 = , que é 1000 0000 em binário,
#
# * -16 (decimal do complemento assinado de 2) — leia mais sobre a Two's complement operation (operação de complemento de dois).
#
#
#
# Exercício 1
#
# Qual é o output do seguinte snippet?

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

#
#
# Verifique
# False
#
# Exercício 2
#
# Qual é o output do seguinte snippet?
#
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)


# Verifique
# 0 5 -5 1 1 16
