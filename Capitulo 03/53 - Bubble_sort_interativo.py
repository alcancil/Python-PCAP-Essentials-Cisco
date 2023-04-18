# O bubble sort - versão interativa
# No editor pode ver um programa completo, enriquecido por uma conversa com o utilizador, e que permite ao utilizador introduzir e imprimir elementos da lista: O bubble sort - versão interativa final.
#
# O Python, contudo, tem os seus próprios mecanismos de ordenação. Ninguém precisa de escrever a sua própria ordenação, uma vez que existe um número suficiente de ferramentas prontas a usar.
# 
# Explicámos-lhe este sistema de ordenação porque é importante aprender a processar o conteúdo de uma lista, e mostrar-lhe como a ordenação real pode funcionar.
# 
# Se quiser que o Python ordene a sua lista, pode fazê-lo desta forma:
#
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)
# 
#
# É tão simples quanto isso.
# 
# O output do snippet é o seguinte:
#
# [2, 4, 6, 8, 10]
# output
#
#
# Como pode ver, todas as listas têm um método chamado sort(), que as classifica o mais rapidamente possível. Já aprendeu alguns dos métodos de lista antes, e vai aprender mais sobre outros muito em breve.

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)