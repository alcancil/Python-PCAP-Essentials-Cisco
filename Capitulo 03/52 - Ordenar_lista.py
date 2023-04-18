# Classificar uma lista
# Quantas passagens precisamos para ordenar a lista completa?
#
# Resolvemos esta questão da seguinte forma: introduzimos outra variável; a sua 
# tarefa é observar se foi feita alguma troca durante a passagem ou não; se não 
# houver troca, então a lista já está ordenada, e nada mais tem de ser feito. Criamos # uma variável chamada swapped, e atribuímos-lhe um valor de False , para indicar que # não há trocas. Caso contrário, será atribuído True.
# 
print("Exemplo 01")
my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.


# Deverá ser capaz de ler e compreender este programa sem quaisquer problemas:

print()
print("Exemplo 02")
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)


# Execute o programa e teste-o.