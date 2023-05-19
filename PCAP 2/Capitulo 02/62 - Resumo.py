#
# Key takeaways
#
# 1. Uma exceção é um evento na execução de um programa causado por uma situação anormal. A exceção deve ser tratada para evitar a terminação do programa. A parte do seu código que é suspeita de ser a 
# origem da exceção deve ser colocada dentro do ramo try .
#
# Quando a exceção acontece, a execução do código não é terminada, mas em vez disso salta para o ramo except . Este é o local onde deve ter lugar o tratamento da exceção. O esquema geral de tal construção 
# parece-se com o seguinte:
# :
# # The code that always runs smoothly.
# :
# try:
#     :
#     # Risky code.
#     :
# except:
#     :
#     # Crisis management takes place here.
#     : 
# :
# # Back to normal.
# :
#
#
# 2. Se precisar de tratar de mais do que uma exceção proveniente do mesmo ramo try , pode adicionar mais do que um ramo except , mas é preciso rotulá-los com nomes de exceção diferentes, como este:
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
# :
# # Back to normal.
# :
#
#
# No máximo, um dos ramos except é executado - nenhum dos ramos é executado quando a exceção levantada não coincide com as exceções especificadas.
#
# 3. Não pode acrescentar mais do que um ramo anónimo (não nomeado) except após os nomeados.
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
# # Back to normal.
# :
# 
#
#
# Exercício 1
#
# Qual é o output esperado do seguinte código?
try:
    print("Let's try to do this")
    print("#"[2])
    print("We succeeded!")
except:
    print("We failed")
print("We're done")


# Let's try to do this
# We failed
# We're done
#
#
# Exercício 2
#
# Qual é o output esperado do seguinte código?
try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexingError:
    print("index")
except:
    print("some")


# zero


