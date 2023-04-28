# Algumas funções simples: avaliar o IMC
#
# Vamos começar com uma função para avaliar o Índice de Massa Corporal (IMC).
# IMC (em inglês, Body Mass Index, (BMI)) é igual ao peso (weight) em quilogramas dividido pela altura (height) em metros quadrados
# 
# imc = kilos / altura ao quadrado
# 
# Como pode ver, a fórmula obtém dois valores:
#
#    peso (originalmente em quilogramas)
#    altura (originalmente em metros)
#
# Parece que esta nova função terá dois parâmetros. O seu nome será bmi, mas se preferir qualquer outro nome, use-o.
#
# Vamos codificar a função:

def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))
#
#
# O resultado produzido pela invocação da amostra tem o seguinte aspeto:
# 19.283746556473833
#
# output
#
# A função cumpre as nossas expetativas, mas é um pouco simples - assume que os valores de ambos os parâmetros são sempre significativos. Vale definitivamente a pena verificar se são dignos de confiança.
#
# Vamos verificar os dois e devolver None se algum deles parecer suspeito.