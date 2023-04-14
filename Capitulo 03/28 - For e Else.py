# Os loops for e o ramo else .
# for os loops comportam-se de forma um pouco diferente - dê uma vista de olhos ao snippet no editor e execute-o.
#
# O output pode ser um pouco surpreendente.
# 
# A variável i retém o seu último valor.
#
#
# Modifique um pouco o código para levar a cabo mais uma experiência.
#
# i = 111
# for i in range(2, 1):
#    print(i)
# else:
#     print("else:", i)
#
#
# Consegue adivinhar o output?
#
# O corpo do loop não será executado aqui. Nota: atribuímos a variável i antes do loop.
#
# Execute o programa e verifique o seu output.
# 
# Quando o corpo do loop não é executado, a variável de controlo retém o valor que tinha antes do loop.
#
# Nota: se a variável de controlo não existir antes do início do loop, não existirá quando a execução atingir o ramo else .
# 
# O que acha desta variante de else?
#
#
# Agora vamos falar-lhe de alguns outros tipos de variáveis. As nossas variáveis atuais só podem armazenar um valor de cada vez, mas há variáveis que 
# podem fazer muito mais - podem armazenar tantos valores quantos você quiser.
#

print("""
----------------------
 O loop acontece aqui 
----------------------
""")
for i in range(5):
    print(i)
else:
    print("else:", i)

print(""" 
---------------------------------------------------------
Aqui a variavel i de controle é definida antes do loop
Entao o loop não acontece
---------------------------------------------------------
""")
i = 111
for i in range(2,1):
    print(i)
else:
    print("else:", i)
