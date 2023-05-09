# Remover elementos de uma lista
# Qualquer elemento da lista pode ser removido a qualquer momento - isto é feito com uma instrução chamada del (delete). Nota: é uma instrução, não uma 
# função.
#
# É preciso apontar o elemento a ser removido - desaparecerá da lista, e o comprimento da lista será reduzido em um.
#
# Olhe para o snippet abaixo. Consegue adivinhar que output irá produzir? Execute o programa no editor e verifique.
# 
# del numbers[1]
# print(len(numbers))
# print(numbers)
#
#
# Não se pode aceder a um elemento que não existe - não se pode obter o seu valor nem atribuir-lhe um valor. Ambas estas instruções irão agora causar erros de # runtime:
# 
# print(numbers[4])
# numbers[4] = 1
# 
# 
# Adicione o snippet acima após a última linha de código no editor, execute o programa e verifique o que acontece.
# 
# Nota: retirámos um dos elementos da lista - agora só há quatro elementos na lista. Isto significa que o elemento número quatro não existe.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###
