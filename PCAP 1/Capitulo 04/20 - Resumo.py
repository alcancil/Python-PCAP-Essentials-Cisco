#
# Key takeaways
#
# 1. Pode utilizar a keyword return para dizer a uma função para devolver algum 
# valor. A declaração return sai da função, por exemplo:
# def multiply(a, b):
#    return a * b
#
# print(multiply(3, 4))    # outputs: 12
#
#
# def multiply(a, b):
#    return
#
# print(multiply(3, 4))    # outputs: None
#
#
# 2. O resultado de uma função pode ser facilmente atribuído a uma variável, por 
# exemplo:
# def wishes():
#    return "Happy Birthday!"
#
# w = wishes()
#
# print(w)    # outputs: Happy Birthday!
#
# Veja a diferença no output dos dois exemplos a seguir:
# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes


# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

# outputs: My Wishes
#          Happy Birthday


# 3. Pode utilizar uma lista como argumento de uma função, por exemplo:
def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)

hi_everybody(["Adam", "John", "Lucy"])


# 4. Uma lista também pode ser o resultado de uma função, por exemplo:
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))





# Exercício 1

# Qual é o output do seguinte snippet?
def hi():
    return
    print("Hi!")

hi()


# a função devolverá um implícito None valor

# Exercício 2

# Qual é o output do seguinte snippet?
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))


# True
# False
# None
#
# Exercício 3
#
# Qual é o output do seguinte snippet?
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))

#
# [0, 2, 4, 6, 8, 10]
#
# Exercício 4
#
# Qual é o output do seguinte snippet?
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))


[1, 4, 9, 16, 25]
