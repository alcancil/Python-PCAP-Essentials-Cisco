# Strings - uma breve revisão
#
# Vamos fazer uma breve revisão sobre a natureza das strings do Python.
#
# Em primeiro lugar, as strings do Python (ou simplesmente strings, pois não vamos discutir as strings de qualquer outra linguagem) são sequências imutáveis. 
#
# É muito importante notar isto, porque significa que se deve esperar algum comportamento familiar por parte delas.
#
# Vamos analisar o código no editor para perceber do que estamos a falar:
#
#    Dê uma vista de olhos no Exemplo 1. A função len() utilizada para strings devolve um número de carateres contidos pelos argumentos. O snippet faz o output 2.
#    Qualquer string pode estar vazia. O seu comprimento é de 0 então - assim como no Exemplo 2.
#    Não se esqueça que uma barra invertida (\) utilizada como caratere de escape não está incluída no comprimento total da string. O código no Exemplo 3, portanto, gera o output 3.
#
# Execute os três códigos de exemplo e verifique.


# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))