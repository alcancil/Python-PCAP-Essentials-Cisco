# Formatação de data e hora (parte 2)
#
# A formatação do tempo funciona da mesma forma que a formatação da data, mas requer a utilização de diretivas apropriadas. Vamos dar uma vista de olhos mais atenta a algumas delas no editor.
#
# Resultado:
# 14:53:00
# 20/November/04 14:53:00
#
# output
#
# O primeiro dos formatos usados diz respeito apenas ao tempo. Como pode adivinhar, %H devolve a hora como um número decimal de zero, %M devolve o minuto como um número decimal de zero, enquanto %S devolve o # segundo como um número decimal de zero. No nosso exemplo, %H é substituído por 14, %M por 53, e %S por 00.
#
# O segundo formato usado combina diretivas de data e hora. Existem duas novas directivas, %Y e %B. A diretiva %Y devolve o ano sem um século como um número decimal de zero (no nosso exemplo, é 20). A 
# diretiva %B devolve o mês como o nome completo do local (no nosso exemplo, é novembro).
#
# Em geral, tem muita liberdade na criação de formatos, mas deve lembrar-se de utilizar corretamente as diretivas. Como um exercício, pode verificar o que acontece se, por exemplo, tentar usar a diretiva %Y 
# no formato passado para o método strftime do objeto de tempo. Tente descobrir você mesmo porque obteve este resultado. Boa sorte!

from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))