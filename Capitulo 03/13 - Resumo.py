# Key takeaways
#
# 1. Os operadores de comparação (ou os chamados relacionais) são usados para comparar valores. A tabela abaixo ilustra como os operadores de 
# comparação funcionam, assumindo que x = 0, y = 1, e z = 0:
#
# Operador	 Descrição	 Exemplo
# ==	        retorna se os valores dos operandos forem iguais, eFalse caso contrário	
#  x == y  # False
#  x == z  # True
#
# !=	        retorna Truese os valores dos operandos não forem iguais, eFalse caso contrário	
#  x != y  # True
#  x != z  # False
#
# >	         True se o valor do operando esquerdo for maior que o valor do operando direito, eFalse caso contrário	
#  x > y  # False
#  y > z  # True
#
# <	        True se o valor do operando esquerdo for inferior ao valor do operando direito, eFalse caso contrário	
#  x < y  # True
#  y < z  # False
#
# ≥	        True se o valor do operando esquerdo for maior ou igual ao valor do operando direito, eFalse caso contrário	
#  x >= y  # False
#  x >= z  # True
#  y >= z  # True
#
# ≤	        True se o valor do operando esquerdo for inferior ou igual ao valor do operando direito, eFalse caso contrário	
#  x <= y  # True
#  x <= z  # True
#  y <= z  # False
#
# 2. Quando quiser executar algum código apenas se uma determinada condição for cumprida, pode usar uma declaração condicional:
#
# uma única if declaração, por exemplo:
#
x = 10

if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.
#
#
# uma série de if declarações, por exemplo:
#
x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.
    

# Cada ifdeclaração é testada separadamente.




# uma if-elsedeclaração, por exemplo:

x = 10

if x < 10:  # Condition
    print("x is less than 10")  # Executed if the condition is True.

else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.


# uma série de if declarações seguidas por um else, por exemplo:

x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")


# Cada if é testado separadamente. O corpo de else é executado se o último if for False.

# A if-elif-elsedeclaração, por exemplo:

x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")


# Se a condição if for False, o programa verifica as condições dos elif blocos subsequentes - o primeiro elif bloco que True é executado. Se todas as 
# condições forem False, o else bloco será executado.

# Declarações condicionais nested, por exemplo:

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


