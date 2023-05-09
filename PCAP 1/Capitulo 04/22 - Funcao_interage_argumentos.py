# Como a função interage com os seus argumentos
#
# Vamos agora descobrir como a função interage com os seus argumentos.
#
# O código no editor deve ensinar-lhe algo. Como se pode ver, a função altera o valor do seu parâmetro. A alteração afeta o argumento?
#
# Execute o programa e verifique.
 
def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)

print("-" * 100)
print("Exemplo 01")
print("-" * 100)

var = 1
my_function(var)
print(var)


# O output do código é:
# I got 1
# I have 2
# 1
#
# output
# 
# A conclusão é óbvia - a alteração do valor do parâmetro não se propaga fora da função (em qualquer caso, não quando a variável é uma escalar, como no exemplo).
# 
# Isto também significa que uma função recebe o valor do argumento, não o argumento em si. Isto é verdade para escalares.
# 
# Vale a pena verificar como funciona com listas (lembra-se das peculiaridades de atribuir slices de listas versus atribuir listas como um todo?).
# 
# O exemplo a seguir irá lançar alguma luz sobre a questão:
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

print("-" * 100)
print("Exemplo 02")
print("-" * 100)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


# O output do código é:
# Print #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [0, 1]
# Print #4: [2, 3]
# Print #5: [2, 3]
#
# output
#
# Parece que a regra anterior ainda funciona.
# 
# Finalmente, pode ver a diferença no exemplo abaixo:

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


print("-" * 100)
print("Exemplo 03")
print("-" * 100)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


# Não alteramos o valor do parâmetro my_list_1 (we already know it will not affect the argument), but instead modify the list identified by it.
# 
# O output pode ser surpreendente. Execute o código e verifique:
# Print #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [3]
# Print #4: [3]
# Print #5: [3]
#
# output
#
# Consegue explicá-lo?
#
# Vamos tentar:
#
#    se o argumento for uma lista, então alterar o valor do parâmetro correspondente não afeta a lista (lembre-se: as variáveis que contêm listas são armazenadas de uma forma diferente dos escalares),
#    mas se alterar uma lista identificada pelo parâmetro (nota: a lista, não o parâmetro!), a lista irá refletir a alteração.
#
# É tempo de escrever algumas funções de exemplo. Fá-lo-á na próxima secção.
