# Operações em strings
#
# Como outros tipos de dados, as strings têm o seu próprio conjunto de operações permitidas, embora sejam bastante limitadas em comparação com os números.
#
# Em geral, as strings podem ser:
#
#    concatenadas (juntas)
#    replicadas.
#
# A primeira operação é realizada pelo operador + (note: não é uma adição) enquanto a segunda pelo operador * (note novamente: não é uma multiplicação).
#
# A capacidade de utilizar o mesmo operador contra tipos de dados completamente diferentes (como números vs. strings) chama-se overloading (visto tal operador estar sobrecarregado com tarefas diferentes).
#
# Analise o exemplo:
#
#    O operador + utilizado contra duas ou mais strings produz uma nova string contendo todos os carateres dos seus argumentos (nota: a ordem importa - este +overloaded, em contraste com a sua versão 
# numérica, não é comutativa)
#    o operador * precisa de uma string e um número como argumentos; neste caso, a ordem não importa - pode colocar o número antes da string, ou vice-versa, o resultado será o mesmo - uma nova string criada # # pela enésima replicação da string do argumento.
#
# O snippet produz o seguinte output:
# ab
# ba
# aaaaa
# bbbb
#
# output
#
# Nota: as variantes de atalho dos operadores acima referidos são também aplicáveis para strings (+= e *=).
#
#
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)