# Key takeaways: tuples e dicionários
#
# Exercício 1
# 
# O que acontece quando se tenta executar o seguinte snippet?
my_tup = (1, 2, 3)
print(my_tup[2])


# O programa irá imprimir 3 para o ecrã.
#
# Exercício 2
#
# Qual é o output do seguinte snippet?
tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

#
# O programa irá imprimir 6 para o ecrã. Os elementos do tuple tup foram “descompactados” nas a, b, e c variáveis.
#
# Exercício 3
#
# Complete o código para utilizar corretamente o método count() para encontrar o número de duplicados de 2 no seguinte tuple.
# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = # Write your code here.
#
# print(duplicates)    # outputs: 4


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4


# Exercício 4
#
# Escreva um programa que irá "colar" os dois dicionários (d1 e d2) e criar um novo (d3).
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}
#
# for item in (d1, d2):
     # Write your code here.
#
# print(d3)


# Solução de amostra:
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)


# Exercício 5
#
# Escreva um programa que irá converter a lista my_list num tuple.
# my_list = ["car", "Ford", "flower", "Tulip"]
#
# t =  # Write your code here.
# print(t)
#
#
# Solução de amostra:
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)


# Exercício 6
#
# Escreva um programa que irá converter o tuple colors num dicionário.
# colors = (("green", "#008000"), ("blue", "#0000FF"))
#
# Write your code here.
#
# print(colors_dictionary)
#
#
# Solução de amostra:
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)


# Exercício 7
#
# O que acontecerá quando executar o seguinte código?
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)


# O programa irá imprimir {'A': 1, 'B': 2} para o ecrã.
#
# Exercício 8
#
# Qual é o output do seguinte programa?
colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)


# white : (255, 255, 255)
# grey : (128, 128, 128)
# red : (255, 0, 0)
# green : (0, 128, 0)
