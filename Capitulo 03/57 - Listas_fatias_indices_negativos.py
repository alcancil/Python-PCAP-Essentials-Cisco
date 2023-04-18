# Slices - índices negativos
# Veja o snippet em baixo:
#
# my_list[start:end]
#
#
# Para repetir:
#
# start é o index do primeiro elemento incluído no slice;
# end é o index do primeiro elemento não incluído no slice.
#
# É assim que os índices negativos funcionam com o slice:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)


# O output do snippet é:
#
# [8, 6, 4]
# output
#
#
# Se o start especifica um elemento que se encontra mais longe do que o descrito pelo end (do ponto de vista inicial da lista), o slice estará vazio:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)


# O output do snippet é:
#
# []
