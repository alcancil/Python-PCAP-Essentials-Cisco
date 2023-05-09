# Key takeaways
# 
# 1. A lista é um tipo de dados em Python usada para armazenar vários objetos. É uma coleção ordenada e mutável de ítens separados por vírgulas, entre parêntesis retos, por exemplo:
# 
# my_list = [1, None, True, "I am a string", 256, 0]
#
#
# 2. As listas podem ser indexadas e atualizadas, por exemplo:
#
# my_list = [1, None, True, 'I am a string', 256, 0]
# print(my_list[3])  # outputs: I am a string
# print(my_list[-1])  # outputs: 0
#
# my_list[1] = '?'
# print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]
#
# my_list.insert(0, "first")
# my_list.append("last")
# print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']
#
#
# 3. As listas podem ser nested, por exemplo:
#
# my_list = [1, 'a', ["list", 64, [0, 1], False]]
#
#
# Aprenderá mais sobre o nesting no módulo 3.1.7 - por enquanto, só queremos que esteja ciente de que algo como isto também é possível.
# 
# 4. Os elementos da lista e as listas podem ser excluídos, por exemplo:
#
# my_list = [1, 2, 3, 4]
# del my_list[2]
# print(my_list)  # outputs: [1, 2, 4]
# 
# del my_list  # deletes the whole list
#
#
# Novamente, aprenderá mais sobre isto no módulo 3.1.6 - não se preocupe. Por enquanto, basta tentar experimentar o código acima e verificar como a sua alteração afeta o output.
#
# 5. As listas podem ser iteradas através da utilização do loop for , por exemplo:
#
# my_list = ["white", "purple", "blue", "yellow", "green"]
#
# for color in my_list:
#    print(color)
#
#
# 6. A função len() pode ser usada para verificar o comprimento da lista, por exemplo:
#
# my_list = ["white", "purple", "blue", "yellow", "green"]
# print(len(my_list))  # outputs 5
#
# del my_list[2]
# print(len(my_list))  # outputs 4
#
#
# 7. Uma invocação de função típica parece-se com a seguinte: result = function(arg), enquanto uma invocação de método típica parece-se com isto:result = data.method(arg).
#
#
#
#
# Exercício 1
#
# Qual é o output do seguinte snippet?
#
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)

#
# Verifique
# [6, 2, 3, 4, 5, 1]
# Exercício 2
#
# Qual é o output do seguinte snippet?

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

#
# Verifique
# [1, 3, 6, 10, 15]
# Exercício 3
#
# O que acontece quando executa o seguinte snippet?
#
# lst = []
# del lst
# print(lst)


# Verifique
# NameError: name 'lst' is not defined
# Exercício 4
#
# Qual é o output do seguinte snippet?

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))


# Verifique
# [2, 3]
# 3