
# Key takeaways
#
# 1. Não pode acrescentar mais do que um ramo anónimo (não nomeado) except após os nomeados.
# :
# # The code that always runs smoothly.
# :
# try:
#     :
#     # Risky code.
#     :
# except Except_1:
#     # Crisis management takes place here.
# except Except_2:
#     # We save the world here.
# except:
#     # All other issues fall here.
# :
# Back to normal.
# :
# 
#
# 2. Todas as exceções Python pré-definidas formam uma hierarquia, ou seja, algumas delas são mais gerais (a que se chama BaseException é a mais geral), enquanto outras são mais ou menos concretas (por 
# exemplo, IndexError é mais concreta do que LookupError).
#
# Não deve colocar exceções mais concretas antes das mais gerais dentro da mesma sequência de ramificações except . Por exemplo, pode fazer isto:
# try:
#     # Risky code.
# except IndexError:
#     # Taking care of mistreated lists
# except LookupError:
#     # Dealing with other erroneous lookups
#
#
# mas não o faça (a menos que tenha a certeza absoluta de que deseja que alguma parte do seu código seja inútil)
# try:
#     # Risky code.
# except LookupError:
#     # Dealing with erroneous lookups
# except IndexError:
#    # You'll never get here 
#
#
# 3. A declaração Python raise ExceptionName pode levantar uma exceção sob demanda. A mesma declaração, mas sem ExceptionName, pode ser usada dentro do ramo try apenas, e levanta a mesma exceção que está 
# atualmente a ser tratada.
#
# 4. A declaração Python assert expression avalia a expressão e levanta a exceção AssertError quando a expressão é igual a zero, uma string vazia ou None. Pode utilizá-la para proteger algumas partes 
# críticas do seu código de dados devastadores.
#
#
# Exercício 1
#
# Qual é o output esperado do seguinte código?
try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")


# zero
#
#
# Exercício 2
#
# Qual é o output esperado do seguinte código?
try:
    print(1/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")


# arith
#
#
# Exercício 3
#
# Qual é o output esperado do seguinte código?
def foo(x):
    assert x
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")


# some

