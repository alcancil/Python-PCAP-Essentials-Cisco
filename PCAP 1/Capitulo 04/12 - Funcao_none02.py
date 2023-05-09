# Algumas palavras sobre None: continuação
# Veja o código no editor.
#
# É óbvio que a função strangeFunction devolve True quando o seu argumento é par.
#
# O que devolve de outra forma?
#
# Podemos utilizar o seguinte código para o verificar:
#
# print(strange_function(2))
# print(strange_function(1))
#
#
# Isto é o que vemos na consola:
#
# True
# None
# output
#
#
# Não fique surpreendido da próxima vez que vir None como resultado de uma função - pode ser o sintoma de um erro subtil dentro da função.


def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))
