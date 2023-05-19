# Exceções: continuação
#
# A instrução raise levanta a exceção especificada chamada exc como se fosse levantada de uma forma normal (natural):
# raise exc
#
#
# Nota: raise é uma keyword.
#
# A instrução permite-lhe:
#
#    simular o levantamento de exceções reais (por exemplo, para testar a sua estratégia de tratamento)
#    parcialmente tratar uma exceção e tornar outra parte do código responsável por completar o tratamento (separação de preocupações).
#
# Veja o código no editor. É assim que o pode utilizar na prática.
#
# O output do programa permanece inalterado.
#
# Desta forma, pode testar a sua rotina de tratamento de exceções sem forçar o código a fazer coisas estúpidas.

def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")
