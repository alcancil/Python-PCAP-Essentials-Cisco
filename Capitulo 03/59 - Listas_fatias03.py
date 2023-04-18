# Slices: continuação
# Como já dissemos anteriormente, omitindo ambos start e end faz uma cópia de toda a lista:
#
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
#
#
# O output do snippet é: [10, 8, 6, 4, 2].
#
# A instrução anteriormente descrita del é capaz de apagar mais do que apenas um elemento de uma lista ao mesmo tempo - também pode apagar slices:
#
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
#
#
# Nota: neste caso, o slice não produz nenhuma lista nova!
#
# O output do snippet é: [10, 4, 2].
#
#
# A eliminação de todos os elementos de uma só vez também é possível:
#
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
#
#
# A lista fica vazia e o output é: [].
#
#
# A remoção do slice do código muda dramaticamente o seu significado.
#
# Veja:

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
#
#
# A instrução del eliminará a lista em si, não o seu conteúdo.
#
# A print() invocação da função a partir da última linha do código causará então um erro de runtime.

