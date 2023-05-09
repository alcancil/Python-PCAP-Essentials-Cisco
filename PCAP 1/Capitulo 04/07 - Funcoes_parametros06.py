# Mistura de argumentos posicionais e de keywords
# Pode misturar ambos os tipos se quiser - há apenas uma regra inquebrável: tem de colocar argumentos posicionais antes de argumentos de keyword.
#
# Se pensar por um momento, certamente adivinhará porquê.
#
# Para lhe mostrar como funciona, utilizaremos a seguinte função simples de três parâmetros:
#
# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
#
#
# O seu objetivo é avaliar e apresentar a soma de todos os seus argumentos.
#
# A função, quando invocada da seguinte maneira:
#
# adding(1, 2, 3)
#
#
# terá como output:
#
# 1 + 2 + 3 = 6
# output
#
#
# Foi - como se pode suspeitar - um puro exemplo de passagem de argumento posicional.
#
# É claro que se pode substituir tal invocação por uma variante de keyword pura, como esta:
#
# adding(c = 1, a = 2, b = 3)
#
#
# O nosso programa fará output de uma linha como esta:
#
# 2 + 3 + 1 = 6
# output
#
#
# Observe a ordem dos valores.
#
# Vamos tentar misturar ambos os estilos agora.
#
# Veja a invocação da função abaixo:
#
# adding(3, c = 1, b = 2)
#
#
# Vamos analisá-la:
#
# o argumento (3) para o parâmetro a é passado usando a maneira posicional;
# os argumentos para c e b são especificados como keywords.
# Isto é o que verá na consola:
#
# 3 + 2 + 1 = 6
# output
#
# Tenha cuidado, e atenção aos erros. Se tentar passar mais do que um valor para um argumento, tudo o que obterá será um erro de runtime.
#
# Olhe para a invocação em baixo - parece que tentámos fixar a duas vezes:
#
# adding(3, a = 1, b = 2)
#
#
# A resposta do Python:
#
# TypeError: adding() got multiple values for argument 'a'
# output
#
#
# Olhe para o snippet abaixo. Um código como este está totalmente correto, mas não faz muito sentido:
#
# adding(4, 3, c = 2)
#
#
# Tudo está correto, mas deixar apenas uma keyword parece um pouco estranho - o que acha?
#
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Call the adding function here.
adding(1,2,3)