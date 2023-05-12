# Strings multiline
#
# Agora é um momento muito bom para lhe mostrar outra forma de especificar strings dentro do source code de Python. Note que a sintaxe que já conhece não o deixará usar uma string que ocupa mais do que uma 
# linha de texto.
#
# Por esta razão, o código aqui está errado:
# multiline = 'Line #1
# Line #2'
#
# print(len(multiline))
#
#
# Felizmente, para este tipo de strings, o Python oferece uma sintaxe separada, conveniente e simples.
# 
# Veja o código no editor. É este o seu aspeto.

multiline = '''Line #1
Line #2'''

print(len(multiline))


# Como pode ver, a string começa com três apóstrofes, não uma. A mesma apóstrofe tripla é utilizada para a terminar.
#
# O número de linhas de texto colocadas dentro de tal string é arbitrário.
#
# O snippet faz o output 15.
#
# Conte os carateres com cuidado. Este resultado está correto ou não? À primeira vista parece estar, mas quando se conta os carateres não está.
#
# Line #1 contém sete carateres. Duas dessas linhas compreendem 14 carateres. Perdemos um caratere? Onde? Como?
#
# Não, não perdemos.
#
# O caratere que falta é simplesmente invisível - é um espaço em branco. Ele está localizado entre as duas linhas de texto.
#
# É denotado como: \n.
#
# Lembra-se? É um caratere especial (de controlo) utilizado para forçar uma line feed (alimentação de linha) (daí o seu nome: LF). Não se consegue vê-lo, mas conta.
#
# As strings multiline também podem ser delimitadas por aspas triplas, tal como aqui:
multiline = """Line #1
Line #2"""

print(len(multiline))


# Escolha o método que lhe seja mais confortável. Ambos funcionam da mesma forma.

