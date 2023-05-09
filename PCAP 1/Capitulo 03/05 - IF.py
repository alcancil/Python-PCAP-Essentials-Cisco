# A função IF
#
# A função IF server para se testar uma condição.
# Por exemplo: 
# Se o carro tiver gasolina então:
#    ande de carro ()
#
# A função ande de carro() só irá ser executada se a condição if for verdadeira.
# A função if funciona na seguinte estrutura
#
# if condicao true :
#    funcao1() 
#    funcao2()
#    funcao3()
#
# PS: para fazer parte do bloco do IF, toda a função a ser executada deve seguir a mesma identação. Se essa estiver fora da mesma, então ela estará
# fora da função if e sempre será executada
#
#if condicao true :
#    funcao1() 
#    funcao2()
#    funcao3()
#funcao4()
#
# Nesse exemplo as funcoes 1, 2 e 3 somente serão executadas se a condição for verdadeira porém a funcao4 sempre sera executada
#
num = input("Digite um número de 0 a 9: ")
if int(num) <= 9:
   print("O numero escolhido esta entre 0 e 9")