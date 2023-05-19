# Exceções: continuação
#
# Agora é um bom momento para lhe mostrar outra instrução Python, chamada assert. Esta é uma keyword.
# assert expression
#
#
# Como é que funciona?
#
#    Ela avalia a expressão;
#    se a expressão for avaliada para True, ou um valor numérico não nulo, ou uma string não vazia, ou qualquer outro valor diferente de None, não fará mais nada;
#    caso contrário, levanta automática e imediatamente uma exceção chamada AssertionError (neste caso, dizemos que a assertion falhou)
#
# Como pode ser utilizada?
#
#    pode querer inseri-la no seu código onde quer estar absolutamente a salvo de dados evidentemente errados, e onde não tem a certeza absoluta de que os dados já foram cuidadosamente examinados (por 
# exemplo, dentro de uma função utilizada por outra pessoa)
#    levantar uma exceção AssertionError assegura que o seu código não produz resultados inválidos, e mostra claramente a natureza do fracasso;
#    as assertions não substituem as exceções nem validam os dados - são seus suplementos.
#
# Se as exceções e a validação de dados forem como uma condução cuidadosa, a assertion pode desempenhar o papel de um airbag.
#
# Vamos ver a instrução assert em ação. Veja o código no editor. Execute-o.
#
# O programa corre sem falhas se introduzir um valor numérico válido maior ou igual a zero; caso contrário, ele para e emite a seguinte mensagem:
# Traceback (most recent call last):
#   File ".main.py", line 4, in 
#    assert x >= 0.0
# AssertionError

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
