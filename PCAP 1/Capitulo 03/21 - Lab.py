# LAB
#
# Tempo estimado
# 5-15 minutos
#
# Nível de dificuldade
# Muito fácil
# 
# Objetivos
# Familiarizar o aluno a:
#
# a utilização do loop for ;
# refletir situações da vida real em código informático.
# Cenário
# Sabe o que é o Mississippi? Bem, é o nome de um dos estados e rios dos Estados Unidos. O rio Mississippi tem cerca de 3.765 quilómetros de 
# comprimento, o que o torna o segundo rio mais longo dos Estados Unidos (o mais longo sendo o rio Missouri). É tão longo que uma única gota de água 
# precisa de 90 dias para percorrer toda a sua extensão!
#
# A palavra Mississippi é também usada para um propósito ligeiramente diferente: contar mississippily.
#
# Se não está familiarizado com a frase, estamos aqui para lhe explicar o seu significado: é usado para contar segundos.
#
# A ideia por detrás disto é que adicionar a palavra Mississippi a um número ao contar segundos em voz alta faz com que soem mais perto do tempo do 
# relógio, e por isso "um Mississippi, dois Mississippi, três Mississippi" levará aproximadamente três segundos de tempo real! É frequentemente 
# utilizado por crianças que brincam às escondidas para garantir que o buscador faz uma contagem honesta.
#
#
# A sua tarefa aqui é muito simples: escreva um programa que utilize um loop for para “contar mississippily” até cinco. Tendo contado até cinco, o 
# programa deve imprimir para o ecrã a mensagem final "Ready or not, here I come!"
#
# Use o esqueleto que fornecemos no editor.
#
# INFORMAÇÃO EXTRA
#
# Observe que o código no editor contém dois elementos que podem não estar totalmente claros para si neste momento: a declaração import time , e o 
# método sleep() . Vamos falar sobre eles em breve.
#
# Por enquanto, gostaríamos apenas que soubesse que importámos o módulo time e usámos o método sleep() para suspender a execução de cada função print() # subsequente dentro do loop for por um segundo, para que a mensagem enviada para a consola se assemelhe a uma contagem real. Não se preocupe - em 
# breve aprenderá mais sobre módulos e métodos.
#
# Output esperado
# 1 Mississippi
# 2 Mississippi
# 3 Mississippi
# 4 Mississippi
# 5 Mississippi
#
#
import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

for i in range (1, 6):
    print(i, "Missipi")
    time.sleep(1)
    
print("Pronto ou não, aqui vou eu !!!")