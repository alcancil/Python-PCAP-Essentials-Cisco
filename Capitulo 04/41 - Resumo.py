
# Key takeaways: tuples
#
# 1. Os tuples são coleções de dados ordenados e imutáveis. Podem ser imaginados como listas imutáveis. São escritos entre parêntesis curvos:

my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)


# Cada elemento tuple pode ser de um tipo diferente (ou seja, inteiros, strings, booleanos, etc.). Além disso, os tuples podem conter outros tuples ou listas (e o inverso).
#
# 2. Pode-se criar um tuple vazio como este:

empty_tuple = ()
print(type(empty_tuple))    # outputs: <class 'tuple'>


# 3. Um tuple de um elemento pode ser criado da seguinte forma:
one_elem_tuple_1 = ("one", )    # Brackets and a comma.
one_elem_tuple_2 = "one",       # No brackets, just a comma.


# Se remover a vírgula, dirá ao Python para criar uma variável e não um tuple:

my_tuple_1 = 1, 
print(type(my_tuple_1))    # outputs: <class 'tuple'>

my_tuple_2 = 1             # This is not a tuple.
print(type(my_tuple_2))    # outputs: <class 'int'>


# 4. Pode aceder aos elementos do tuple através da indexação:
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])    # outputs: [3, 4]


# 5. Os tuples são imutáveis, o que significa que não se pode alterar os seus elementos (não se pode anexar tuples, ou modificar, ou remover elementos tuple). O snippet a seguir causará uma exceção:
# my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
# my_tuple[2] = "guitar"    # The TypeError exception will be raised.
#
#
# No entanto, é possível apagar um tuple como um todo:
# 
# my_tuple = 1, 2, 3, 
# del my_tuple
# print(my_tuple)    # NameError: name 'my_tuple' is not defined
#
# 6. Pode fazer um loop através dos elementos de um tuple (Exemplo 1), verificar se um elemento específico está (ou não) presente num tuple (Exemplo 2), utilizar a função len() para verificar quantos # 
# elementos existem num tuple (Exemplo 3), ou mesmo juntar/multiplicar tuples (Exemplo 4):
# Example 1

tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# Example 2

tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# Example 3
tuple_3 = (1, 2, 3, 5)
print(len(tuple_3))

# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)


# EXTRA
#
# Também pode criar um tuple usando uma função Python incorporada chamada tuple(). Isto é particularmente útil quando se pretende converter um certo iterável (por exemplo, uma lista, range, string, etc.) num tuple:
my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>


# Da mesma forma, quando se pretende converter um iterável numa lista, pode-se usar uma função Python integrada chamada list():
tup = 1, 2, 3, 
my_list = list(tup)
print(type(my_list))    # outputs: <class 'list'>



