# Os loops replace() .
#
# O método de dois parâmetros replace() devolve uma cópia da string original na qual todas as ocorrências do primeiro argumento foram substituídas pelo segundo argumento.
#
# Veja o código de exemplo no editor. Execute-o.
#
# O output do exemplo:
# www.pythoninstitute.org
# Thare are it!
# Apple
#
# output
#
# Se o segundo argumento for uma string vazia, a substituição está na realidade a remover a string do primeiro argumento. Que tipo de magia acontece se o primeiro argumento for uma string vazia?
#
# A variante de três parâmetros replace() utiliza o terceiro argumento (um número) para limitar o número de substituições.
#
# Veja o código de exemplo modificado abaixo:
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
#
#
# Consegue adivinhar o seu output? Execute o código e verifique as suas suposições.
#
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))