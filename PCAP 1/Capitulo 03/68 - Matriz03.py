# Natureza multidimensional das listas: aplicações avançadas
# Vamos aprofundar a natureza multidimensional das listas. Para encontrar qualquer elemento de uma lista bidimensional, é preciso utilizar duas coordenadas:
#
# uma vertical (número da fila)
# e uma horizontal (número da coluna).
# Imagine que desenvolve uma peça de software para uma estação meteorológica automática. O dispositivo regista a temperatura do ar numa base horária e fá-lo ao longo de todo o mês. Isto dá-lhe um total de 
# 24 & vezes; 31 = 744 valores. Vamos tentar criar uma lista capaz de armazenar todos estes resultados.
#
# Primeiro, tem de decidir que tipo de dados serão adequados para esta aplicação. Neste caso, um float seria melhor, uma vez que este termómetro é capaz de medir a temperatura com uma precisão de 0,1 ℃.
#
# De seguida, toma uma decisão arbitrária de que as filas registarão as leituras de hora em hora (por isso a fila terá 24 elementos) e que cada uma das filas será atribuída a um dia do mês (vamos supor que # cada mês tem 31 dias, por isso precisa de 31 filas). Aqui está o par apropriado de compreensões (h é para hora, d para dia):
#
# temps = [[0.0 for h in range(24)] for d in range(31)]
#
#
# Toda a matriz está agora preenchida com zeros. Pode assumir que é atualizada automaticamente utilizando agentes especiais de hardware. O que tem de fazer é esperar que a matriz seja preenchida com 
# medições.
#
# Agora é altura de determinar a temperatura média mensal ao meio-dia. Some todas as 31 leituras registadas ao meio-dia e divida a soma por 31. Pode assumir que a temperatura à meia-noite é armazenada em 
# primeiro lugar. Aqui está o código relevante:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)


# Nota: a variável day usada pelo loop for não é um escalar - cada passagem através da matriz temps atribui-a com as linhas subsequentes da matriz; portanto, é uma lista. Tem que ser indexado com 11 para 
# aceder ao valor da temperatura medida ao meio-dia.
#
# Agora encontre a temperatura mais alta durante todo o mês - veja o código:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)


# Nota:
#
# a keyword day itera através de todas as linhas na matriz temps ;
# a variável temp itera através de todas as medições efetuadas num dia.
# Agora conte os dias em que a temperatura ao meio-dia era de pelo menos 20 ℃:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

