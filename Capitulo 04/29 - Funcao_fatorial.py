# Algumas funções simples: factorials
#
# Outra função que estamos prestes a escrever é a factorials. Lembra-se de como um fatorial é definido?
#
# 0! = 1 (sim! é verdade)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 ** 3 * 4 * ... * n-1 * n
#
# É marcado com um ponto de exclamação, e é igual ao produto de todos os números naturais de um até ao seu argumento.
# 
# Vamos escrever o nosso código. Vamos criar uma função e chamá-la factorial_function. Aqui está o código:
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # testing
    print(n, factorial_function(n))


# Observe como espelhamos passo a passo a definição matemática, e como usamos o loop for para encontrar o produto.
#
# Adicionamos um código de teste simples, e estes são os resultados que obtemos:
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120