# Listas - alguns programas simples
# Agora queremos mostrar-lhe alguns programas simples que utilizam listas.
#
# O primeiro deles tenta encontrar o maior valor na lista. Veja o código no editor.
#
# O conceito é bastante simples - assumimos temporariamente que o primeiro elemento é o maior, e verificamos a hipótese contra todos os restantes elementos da lista.
#
# O código fará o output 17 (como esperado).
#
# O código pode ser reescrito para fazer uso da forma recentemente introduzida do for :
#
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

#
# O programa acima realiza uma comparação desnecessária, quando o primeiro elemento é comparado consigo mesmo, mas isto não é de todo um problema.
#
# O código fará o output 17, também (nada invulgar).
#
# Se precisar de poupar energia do computador, pode utilizar um slice:

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


# A questão é: qual destas duas ações consome mais recursos informáticos - apenas uma comparação, ou slicing de quase todos os elementos de uma lista?