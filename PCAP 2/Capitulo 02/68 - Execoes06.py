# Exceções: continuação
#
# A instrução raise também pode ser utilizada da seguinte maneira (observe a ausência do nome da exceção):
# raise
#
#
# Existe uma restrição grave: este tipo de instrução raise pode ser utilizada dentro do ramo except apenas; usá-la em qualquer outro contexto causa um erro.
#
# A instrução voltará imediatamente a levantar a mesma exceção que é atualmente tratada.
#
# Graças a isto, pode distribuir o tratamento de exceções entre diferentes partes do código.
#
# Veja o código no editor. Execute-o - vamos vê-lo em ação.
#
# A exceção ZeroDivisionError é levantado duas vezes:
#
#    primeiro, dentro da parte do código try (isto é causado pela divisão real zero)
#    segundo, dentro da parte except pela instrução raise .
#
# Com efeito, o código faz o output:
# I did it again!
# I see!
# THE END.

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")