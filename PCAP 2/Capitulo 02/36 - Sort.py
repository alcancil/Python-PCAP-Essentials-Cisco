# Sorting
#
# A comparação está estreitamente relacionada com o sorting (ordenação) (ou melhor, o sorting é de facto um caso muito sofisticado de comparação).
#
# Esta é uma boa oportunidade para lhe mostrar duas formas possíveis de ordenar listas contendo strings. Tal operação é muito comum no mundo real - sempre que se vê uma lista de nomes, bens, títulos, ou 
# cidades, espera-se que sejam ordenados.
#
# Vamos supor que quer ordenar a seguinte lista:
#  greek = ['omega', 'alpha', 'pi', 'gamma']
# 
# 
# Em geral, o Python oferece duas formas diferentes de ordenar listas.
# 
# O primeiro é implementado como uma função chamada sorted().
# 
# A função toma um argumento (uma lista) e devolve uma nova lista, preenchida com os elementos do argumento ordenados. (Nota: esta descrição é um pouco simplificada em comparação com a implementação real - 
# discuti-la-emos mais tarde).
#
# A lista original permanece intacta.
#
# Veja o código no editor, e execute-o. O snippet produz o seguinte output:
# ['omega', 'alpha', 'pi', 'gamma']
# ['alpha', 'gamma', 'omega', 'pi']
#
# output
#
# O segundo método afeta a própria lista - nenhuma nova lista é criada. A ordenação é realizada in situ pelo método chamado sort().
# 
# O output não foi alterado:
# ['omega', 'alpha', 'pi', 'gamma']
# ['alpha', 'gamma', 'omega', 'pi']
#
# output
#
# Se precisar de uma ordem que não seja não-decrescente, tem de convencer a função/método a alterar os seus comportamentos padrão. Vamos discutir isso em breve.

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)