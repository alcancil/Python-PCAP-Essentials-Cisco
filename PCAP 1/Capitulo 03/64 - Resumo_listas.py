# Key takeaways
#
# 1. Se tiver uma lista l1, então a seguinte tarefa: l2 = l1 não faz uma cópia da lista l1 , mas faz com que as variáveis l1 e l2 apontem para uma e a mesma lista na memória. Por exemplo:
#
print("Exemplo 01")
vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']

#
# 2. Se quiser copiar uma lista ou parte da lista, pode fazê-lo executando slicing:

print("Exemplo 02")
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list


# 3. Também se podem utilizar índices negativos para executar slices. Por exemplo:

print("Exemplo 03")
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']


# 4. O objeto da exceção start e end parâmetros são opcionais ao executar uma slice: list[start:end], por exemplo.:

print("Exemplo 04")
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]


# 5. Pode eliminar slices usando a instrução del :

print("Exemplo 05")
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []


# 6. Pode testar se alguns itens existem numa lista ou não usando as keywords in e not in, por exemplo.:

print("Exemplo 06")
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False


# Exercício 1
#
# Qual é o output do seguinte snippet?

print("Exercicio 01")
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)


# Verifique
# ['C']

# Exercício 2

#Qual é o output do seguinte snippet?

print("Exercicio 02")
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)


# Verifique
# ['B', 'C']
#
# Exercício 3
#
# Qual é o output do seguinte snippet?

print("Exercicio 03")
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)


# Verifique
# []
#
# Exercício 4
#
# Qual é o output do seguinte snippet?

print("Exercicio 04")
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

# Verifique
# ['A', 'B', 'C']
#
# Exercício 5
#
# Insira in ou not in em vez de ??? para que o código faça output do resultado esperado.
#
# my_list = [1, 2, "in", True, "ABC"]
#
# print(1 ??? my_list)  # outputs True
# print("A" ??? my_list)  # outputs True
# print(3 ??? my_list)  # outputs True
# print(False ??? my_list)  # outputs False
#
# Verifique
# my_list = [1, 2, "in", True, "ABC"]
#
# print(1 in my_list)  # outputs True
# print("A" not in my_list)  # outputs True
# print(3 not in my_list)  # outputs True
# print(False in my_list)  # outputs False