#
# Key takeaways
#
# 1. Uma variável que existe fora de uma função tem um scope dentro do corpo da função (Exemplo 1), a menos que a função defina uma variável com o mesmo nome (Exemplo 2, e Exemplo 3), por exemplo:
#
# Exemplo 1:

var = 2


def mult_by_var(x):
    return x * var

print("=" * 100)
print("Exercicio 01")
print("=" * 100)

print(mult_by_var(7))    # outputs: 14


# Exemplo 2:

def mult(x):
    var = 5
    return x * var


print("=" * 100)
print("Exercicio 02")
print("=" * 100)
print(mult(7))    # outputs: 35


# Exemplo 3:

def mult(x):
    var = 7
    return x * var

print("=" * 100)
print("Exercicio 03")
print("=" * 100)

var = 3
print(mult(7))    # outputs: 49

#
# 2. Uma variável que existe dentro de uma função tem um scope dentro do corpo da função (Exemplo 4), por exemplo:
#
# Exemplo 4:

def adding(x):
    var = 7
    return x + var

print("=" * 100)
print("Exercicio 04")
print("=" * 100)

print(adding(4))    # outputs: 11
# print(var)    # NameError
#
#
# 3. Pode utilizar a keyword global seguida por um nome de variável para tornar o scope da variável global, por exemplo

print("=" * 100)
print("Exercicio 05")
print("=" * 100)

var = 2
print(var)    # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())    # outputs: 5
print(var)    # outputs: 5




# Exercício 1
#
# O que acontecerá quando tentar executar o seguinte código?
# 
# def message():
#    alt = 1
#    print("Hello, World!")
#
# print(alt)
#
#
# A função NameError será lançada (NameError: name 'alt' is not defined)
#
# Exercício 2
# 
# Qual é o output do seguinte snippet?
# a = 1
#
#
# def fun():
#    a = 2
#    print(a)
#
#
# fun()
# print(a)
#
#
# 2
# 1
#
# Exercício 3
#
# Qual é o output do seguinte snippet?
# a = 1
#
#
# def fun():
#     global a
#     a = 2
#     print(a)
#
#
# fun()
# a = 3
# print(a)
#
#
# 2
# 3
#
# Exercício 4
#
# Qual é o output do seguinte snippet?
# a = 1
#
#
# def fun():
#     global a
#     a = 2
#     print(a)
#
#
# a = 3
# fun()
# print(a)
#
#
# 2
# 2
