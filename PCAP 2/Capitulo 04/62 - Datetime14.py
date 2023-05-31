# Formatação de data e hora (parte 1)
#
# Todas as classes de módulo datetime apresentadas até agora têm um método chamado strftime. Este é um método muito importante, porque nos permite devolver a data e a hora no formato que especificamos.
#
# O método strftime só aceita um argumento sob a forma de uma string especificando o formato que pode consistir em diretivas.
#
# Uma diretiva é uma string que consiste no caratere % (percentagem) e uma letra minúscula ou maiúscula, por exemplo, a diretiva %Y significa o ano com o século como um número decimal. Vejamo-lo num exemplo. # Execute o código no editor.

from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))


# Resultado:
# 2020/01/04
#
# output
#
# No exemplo, passámos um formato constituído por três diretivas separadas por / (barra) para o método strftime . É claro que o caratere separador pode ser substituído por outro caratere, ou mesmo por uma 
# string.
#
# Pode colocar quaisquer carateres no formato, mas apenas as diretivas reconhecíveis serão substituídas pelos valores apropriados. No nosso formato, utilizámos as seguintes diretivas:
#
#    %Y — devolve o ano com o século como um número decimal. No nosso exemplo, é 2020.
#    %m — devolve o mês como um número decimal de zero. No nosso exemplo, é 01.
#    %d — devolve o dia como um número decimal de zero. No nosso exemplo, é 04.
#
# Nota: Pode encontrar todas as diretivas disponíveis aqui.
#
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes