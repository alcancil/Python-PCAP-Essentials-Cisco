# Exceções: continuação
#
# Veja o código no editor. É um exemplo simples para começar. Execute-o.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")
#
# O output que esperamos ver é semelhante a este:
# Oooppsss...
# THE END.
#
# output
#
# Agora veja o código abaixo:

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")


# Alguma coisa mudou nele - nós substituímos ZeroDivisionError por ArithmeticError.
#
# Já sabe que ArithmeticError é uma classe geral, incluindo (entre outros) a exceção ZeroDivisionError .
#
# Assim, o output do código permanece inalterado. Teste-o.
#
# Isto também significa que a substituição do nome da exceção por Exception ou BaseException não vai mudar o comportamento do programa.
#
# Vamos resumir:
#
#    cada exceção levantada cai no primeiro ramo correspondente;
#     o ramo correspondente não tem de especificar exatamente a mesma exceção - basta que a exceção seja mais geral (mais abstrata) do que a exceção levantada.


