# Key takeaways
#
# 1. Pode utilizar a keyword sort() para ordenar elementos de uma lista, por exemplo:
#
# lst = [5, 3, 1, 2, 4]
# print(lst)
# 
# lst.sort()
# print(lst)  # outputs: [1, 2, 3, 4, 5]
#
# 
# 2. Há também um método de lista chamado reverse(), que pode utilizar para inverter a lista, por exemplo
#
# lst = [5, 3, 1, 2, 4]
# print(lst)
# 
# lst.reverse()
# print(lst)  # outputs: [4, 2, 1, 3, 5]
#
#
#
# Exercício 1
#
# Qual é o output do seguinte snippet?

print("Exercicio 01")
lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)


# Verifique
# ['A', 'D', 'F', 'Z']
#
# Exercício 2
#
# Qual é o output do seguinte snippet?

print("Exercicio 02")
a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)


# Verifique
# [1, 2, 3]
#
# Exercício 3
#
# Qual é o output do seguinte snippet?

print("Exercicio 03")
a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)


# Verifique
# [' ', 'C', 'B', 'A']
