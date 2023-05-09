# For
#
# Podemos criar Loops tambbem com o for.
# Ele funciona parecido com o while mas a sua sintaxe é diferente
# Veja o exemplo
#
print("Exemplo 01")
for i in range(10):
    print("The value of i is currently", i)

# Nota:
#
# o loop foi executado dez vezes (é o argumento da função range() )
# o valor da última variável de controlo é 9 (não 10, visto começar a partir de 0, não a partir de 1)
#
# Mas o for pode aceitar dois argumentos tambén no range
# Veja outro exemplo
#
print("")
print("Exemplo 02")
for i in range(2, 8):
    print("The value of i is currently", i)
#
# Neste caso o contador começa em 2 e termina em 7 . MAs porque 7 ?
# O python começa a contar no número 0