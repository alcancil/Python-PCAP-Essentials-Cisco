# Exceções: continuação
#
# Veja o código no editor. O que vai acontecer aqui?
#
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

#
# O primeiro ramo correspondente é o que contém ZeroDivisionError. Isto significa que a consola irá mostrar:
# Zero division!
# THE END.
#
# output
#
# Irá mudar alguma coisa se trocarmos os dois ramos except ? Tal como aqui em baixo:
try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")


# A mudança é radical - o output do código é agora:
# Arithmetic problem!
# THE END.
#
# output
# 
# Porquê, se a exceção levantada é a mesma que anteriormente?
#
# A exceção é a mesma, mas a exceção mais geral é agora listada em primeiro lugar - também irá apanhar todas as divisões zero. Significa também que não há hipótese de qualquer exceção atingir o ramo 
# ZeroDivisionError . Este ramo é agora completamente inacessível.
#
# Lembre-se:
#
#    a ordem dos ramos é importante!
#    não ponha exceções mais gerais antes de exceções mais concretas;
#    isto tornará este último inalcançável e inútil;
#    Além disso, tornará o seu código confuso e inconsistente;
#    O Python não irá gerar quaisquer mensagens de erro relativamente a esta questão.

