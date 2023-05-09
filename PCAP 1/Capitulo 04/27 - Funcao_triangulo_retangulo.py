# Algumas funções simples: triângulos e o teorema de Pitágoras
#
# Veja o código no editor. Ele pede ao utilizador três valores. Em seguida, faz uso da função is_a_triangle . O código está pronto a ser executado.
#

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')



# No segundo passo, tentaremos assegurar que um certo triângulo é um triângulo de ângulo reto.
# 
# Precisamos de utilizar o teorema de Pitágoras:
# 
# c2 = a2 + b2
#
# Como reconhecer qual dos três lados é a hipotenusa?
#
# A hipotenusa é o lado mais longo.
#
# Aqui está o código:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))


# Veja como testamos a relação entre a hipotenusa e os restantes lados - escolhemos o lado mais longo, e aplicamos o teorema de Pitágoras para verificar se tudo está certo. Isto requer três verificações no # total.