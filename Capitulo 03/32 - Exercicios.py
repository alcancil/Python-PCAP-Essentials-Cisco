# Principais takeaways: continuação
# Exercício 1
#
# Crie um loop for que conta de 0 a 10, e imprime os números ímpares no ecrã. Use o esqueleto abaixo:
#
# for i in range(1, 11):
    # Line of code.
        # Line of code.
#
#
# Verifique
# Solução de amostra:
print("Exercicio 01")
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

#
# Exercício 2
#
# Crie um loop while que conta de 0 a 10, e imprime os números ímpares no ecrã. Use o esqueleto abaixo:
#
# x = 1
# while x < 11:
     # Line of code. 
         # Line of code.
     # Line of code.


# Verifique
# Solução de amostra:

print()
print("Exercicio 02")
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1


# Exercício 3
# 
# Crie um programa com um loop for e uma declaração break . O programa deve iterar sobre os caracteres de um endereço de e-mail, sair do loop quando 
# chegar ao símbolo @ , e imprimir a parte antes de @ numa linha. Use o esqueleto abaixo:
#
# for ch in "john.smith@pythoninstitute.org":
#    if ch == "@":
         # Line of code.
     # Line of code.

print()
print("Exercicio 03")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Verifique
# Exercício 4
#
# Crie um programa com um loop for e uma declaração continue . O programa deve iterar sobre uma string de dígitos, substituir cada 0 com xe imprimir a # string modificada no ecrã. Use o esqueleto abaixo:
#
# for digit in "0165031806510":
#    if digit == "0":
         # Line of code.
         # Line of code.
     # Line of code.
 

# Verifique
# Solução de amostra:

print()
print("Exercicio 04")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")




# Exercício 5
#
# Qual é o output do seguinte código?

print()
print("Exercicio 05")
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

#
# Verifique
# 4
# 3
# 2
# 0
#
# Exercício 6
#
# Qual é o output do seguinte código?

print()
print("Exercicio 06")
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)


# Verifique
# -1
# 0
# 1
# 2
# 3

# Exercício 7
#
# Qual é o output do seguinte código?

print()
print("Exercicio 07")
for i in range(0, 6, 3):
    print(i)

#
# Verifique
# 0
# 3

# Prev Next