# Exceções: continuação
#
# Se quiser tratar duas ou mais exceções da mesma forma, pode usar a seguinte sintaxe:
# try:
#    :
# except (exc1, exc2):
#     :
#
#
# É simplesmente necessário colocar todos os nomes de exceção envolvidos numa lista separada por vírgulas, e não esquecer os parêntesis.
#
# Se uma exceção for levantada dentro de uma função, pode ser tratada:
#
#    dentro da função;
#    fora da função;
#
# Vamos começar com a primeira variante - veja o código no editor.


def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

# A exceção ZeroDivisionError (sendo um caso concreto da classe de exceção ArithmeticError ) é levantada dentro da função bad_fun() , e não deixa a função - a própria função cuida dela.
#
# O programa faz o output:
# Arithmetic problem!
# THE END.
#
# output
#
# Também é possível deixar que a exceção se propague fora da função. Vamos testá-la agora.
#
# Veja o código em baixo:
def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")


# O problema tem de ser resolvido pelo invocador (ou pelo invocador do invocador, e assim por diante).
#
# O programa faz o output:
# What happened? An exception was raised!
# THE END.
#
# output
#
# Nota: a exceção levantada pode ultrapassar os limites da função e do módulo, e viajar através da cadeia de invocação procurando uma cláusula except correspondente capaz de a tratar.
#
# Se não existir tal cláusula, a exceção permanece sem ser acionada, e o Python resolve o problema à sua maneira padrão - terminando o seu código e emitindo uma mensagem de diagnóstico.
#
# Agora vamos suspender esta discussão, pois queremos apresentar-lhe uma nova instrução Python.