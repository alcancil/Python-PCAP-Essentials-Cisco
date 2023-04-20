# Funções parametrizadas - mais detalhes
# Acontece por vezes que os valores de um determinado parâmetro são utilizados com mais frequência do que outros. Tais argumentos podem ter os seus valores padrão (predefinidos) tomados em consideração 
# quando os seus argumentos correspondentes tiverem sido omitidos.
#
# Dizem que o apelido inglês mais popular é Smith. Vamos tentar ter isto em conta.
#
# O valor padrão do parâmetro é definido usando uma sintaxe clara e pictórica:
#
# def introduction(first_name, last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
#
#
# Só tem de estender o nome do parâmetro com o sinal = , seguido pelo valor padrão.
#
# Vamos invocar a função como de costume:
#
# introduction("James", "Doe")
#
#
# Consegue adivinhar o output do programa? Execute-o e verifique se estava certo.
#
# Então? Tudo parece igual, mas quando se invoca a função de uma forma que à primeira vista parece um pouco suspeita, como esta:
#
# introduction("Henry")
#
#
# ou esta:
#
# introduction(first_name="William")
#
#
# não haverá nenhum erro, ambas as invocações serão bem sucedidas, e a consola mostrará o seguinte output:
#
# Hello, my name is Henry Smith
# Hello, my name is William Smith
# output
#
#
# Teste-o.
#
# Pode ir mais além se for útil. Ambos os parâmetros têm agora os seus valores padrão, veja o código em baixo:
#
# def introduction(first_name="John", last_name="Smith"):
#    print("Hello, my name is", first_name, last_name)
#
#
# Isto faz com que a seguinte invocação seja absolutamente válida:
#
# introduction()
#
#
# E este é o output esperado:
#
# Hello, my name is John Smith
# output
#
#
# Se utilizar um argumento de keyword, o restante tomará o valor padrão:
#
# introduction(last_name="Hopkins")
#
#
# O output é:
#
# Hello, my name is John Hopkins
# output
#
#
# Teste-o.
#
#
# Parabéns - acabou de aprender as formas básicas de comunicar com funções.

def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.

introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")

def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
    
introduction()