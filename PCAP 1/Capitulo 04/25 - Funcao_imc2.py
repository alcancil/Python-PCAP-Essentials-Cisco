# Algumas funções simples: avaliação do IMC (em inglês, BMI) e conversão de unidades imperiais em unidades métricas
#
# Veja o código no editor. Há duas coisas a que temos de prestar atenção.
#

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(352.5, 1.65))
print(bmi(0, 100))
print(bmi(490.76, 201))
print(bmi(2, 100))

# Primeiro, a invocação de teste assegura que a proteção funciona corretamente - o output é:
# None
#
# output
#
# Em segundo lugar, dê uma vista de olhos na forma como o símbolo da barra invertida (\) é usado. Se o utilizar em código Python e terminar uma linha com ele, dirá ao Python para continuar a linha de código # na próxima linha de código.
#
# Pode ser particularmente útil quando se tem de lidar com longas linhas de código e se gostaria de melhorar a legibilidade do código.
#
# Está bem, mas há algo que omitimos com demasiada facilidade - as medidas imperiais. Esta função não é muito útil para pessoas acostumadas a libras, pés e polegadas.
#
# O que pode ser feito por elas?
#
# Podemos escrever duas funções simples para converter unidades imperiais em unidades métricas. Vamos começar com as libras.
# 
# É um facto bem conhecido que 1 lb = 0.45359237 kg. Utilizaremos isto na nossa nova função.
# 
# Esta é a nossa função auxiliar, chamada lb_to_kg:
def lb_to_kg(lb):
    return lb * 0.45359237


print(lb_to_kg(1))


# O resultado da invocação do teste parece bom:
# 0.45359237
# 
# output
#
# E agora é altura para os pés e polegadas: 1 ft = 0.3048 m, e 1 in = 2.54 cm = 0.0254 m.
#
# A função que escrevemos é chamada ft_and_inch_to_m:
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(1, 1))


# O resultado de um teste rápido é:
# 0.3302
#
# output
#
# Parece como o esperado.
# 
# Nota: queríamos nomear o segundo parâmetro apenas in, não inch, mas não podíamos. Sabe porquê?
#
# in é uma keyword Python - não pode ser usada como um nome.
#
# Vamos converter seis pés em metros:
print(ft_and_inch_to_m(6, 0))


# E esta é o output:
#1.8288000000000002

# output
#
# É bem possível que por vezes se queira usar apenas os pés sem polegadas. O Python vai ajudá-lo? Claro que vai.
#
# Modificámos um pouco o código:
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6))


# Agora o parâmetro inch tem o seu valor padrão igual a 0.0.
#
# O código produz o seguinte output - isto é o que é esperado:
# 1.8288000000000002
#
# output
#
# Finalmente, o código é capaz de responder à pergunta: qual é o IMC de uma pessoa com 1,75 m de altura e pesando 176 lbs?
#
# Este é o código que construímos:
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

#
# E a resposta é:
# 27.565214082533313
#
# output
#
# Execute o código e teste-o.
