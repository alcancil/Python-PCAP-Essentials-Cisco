# Slices: continuação
# Se omitir o start no seu slice, assume-se que pretende obter um slice começando pelo elemento com index 0.
#
# Por outras palavras, o slice desta forma:
# 
# my_list[:end]
#
#
# é um equivalente mais compacto de:
#
# my_list[0:end]
#
#
# Veja o snippet em baixo:
#
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
#
#
# É por isso que o seu output é: [10, 8, 6].
#
# Da mesma forma, se omitir o end no seu slice, presume-se que deseja que o slice termine no elemento com o index len(my_list).
#
# Por outras palavras, o slice desta forma:
#
# my_list[start:]
#
#
# é um equivalente mais compacto de:
#
# my_list[start:len(my_list)]
#
#
#Veja o snippet seguinte:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)


# O seu output é, portanto: [4, 2].
