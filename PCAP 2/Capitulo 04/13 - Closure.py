# Um breve olhar sobre os closures
#
# Comecemos por uma definição: o closure é uma técnica que permite o armazenamento de valores apesar do facto de o contexto em que foram criados já não existir. Intrincado? Um pouco.
#
# Vamos analisar um exemplo simples:
# def outer(par):
#     loc = par
#
#
# var = 1
# outer(var)
#
# print(var)
# print(loc)
#
#
# O exemplo é obviamente errado.
#
# As duas últimas linhas causarão uma exceção NameError - nem par nem loc são acessíveis fora da função. Ambas as variáveis existem quando e só quando a função outer() está a ser executada.
#
# Veja o exemplo no editor. Modificámos o código de forma significativa.
#
# Há um novo elemento no mesmo - uma função (denominada inner) dentro de outra função (nomeada outer).
#
# Como é que funciona? Tal como qualquer outra função, exceto o facto de que inner() só pode ser invocada a partir do interior outer(). Podemos dizer que inner() é a ferramenta privada de outer()- nenhuma 
# outra parte do código lhe pode aceder.
#
# Veja com atenção:
#
#    a função inner() devolve o valor da variável acessível dentro do seu scope, uma vez que inner() pode utilizar qualquer uma das entidades à disposição de outer()
#    a função outer() devolve a função inner() em si; mais precisamente, devolve uma cópia da função inner() , a que estava congelada no momento de invocação outer(); a função congelada contém o seu ambiente # completo, incluindo o estado de todas as variáveis locais, o que também significa que o valor de loc é retido com sucesso, embora outer() tenha deixado de existir há muito tempo.
#
# Na verdade, o código é totalmente válido, e tem como output:
# 1
#
# output
#
# A função devolvida durante a invocação outer() é um closure.


def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())