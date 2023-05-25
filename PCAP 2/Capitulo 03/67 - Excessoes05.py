# Anatomia detalhada das exceções
#
# Vamos analisar mais de perto o objeto da exceção, uma vez que há aqui alguns elementos realmente interessantes (voltaremos à questão em breve quando considerarmos as técnicas de base de input/output de 
# Python, uma vez que o seu subsistema de exceção estende um pouco estes objetos).
#
# A classe BaseException introduz uma propriedade chamada args. É um tuple concebido para reunir todos os argumentos passados ao construtor da classe. Está vazio se a construção foi invocada sem quaisquer 
# argumentos, ou contém apenas um elemento quando o construtor recebe um argumento (não contamos o argumento self aqui), e assim por diante.
#
# Preparámos uma função simples para imprimir a propriedade args de uma forma elegante. Pode ver a função no editor.
#
# Utilizámos a função para imprimir o conteúdo da propriedade args em três casos diferentes, em que a exceção da classe Exception é levantada de três maneiras diferentes. Para o tornar mais espetacular, 
# imprimimos também o próprio objeto, juntamente com o resultado da invocação __str__() .
#
# O primeiro caso parece rotineiro - há apenas o nome Exception após a keyword raise . Isto significa que o objeto desta classe foi criado de uma forma muito rotineira.
#
# O segundo e terceiro casos podem parecer um pouco estranhos à primeira vista, mas não há nada de estranho aqui - estas são apenas as invocações do construtor. Na segunda declaração raise , o construtor é 
# invocado com um argumento, e no terceiro com dois.
#
# Como pode ver, o output do programa reflete isto, mostrando o conteúdo apropriado da propriedade args :
# :  :
# my exception : my exception : my exception
# ('my', 'exception') : ('my', 'exception') : ('my', 'exception')


def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
