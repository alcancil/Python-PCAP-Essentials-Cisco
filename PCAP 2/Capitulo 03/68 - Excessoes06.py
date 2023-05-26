# Como criar a sua própria exceção
#
# A hierarquia de exceções não está fechada nem terminada, e pode sempre alargá-la se quiser ou precisar de criar o seu próprio mundo povoado com as suas próprias exceções.
#
# Pode ser útil quando se cria um módulo complexo que deteta erros e levanta exceções, e se pretende que as exceções sejam facilmente distinguíveis de quaisquer outras trazidas pelo Python.
#
# Isto é feito definindo as suas próprias, novas exceções como subclasses derivadas de subclasses predefinidas.
#
# Nota: se quiser criar uma exceção que será utilizada como um caso especializado de qualquer exceção incorporada, derive-a apenas desta. Se quer construir a sua própria hierarquia, e não quer que ela esteja # intimamente ligada à árvore de exceção de Python, derive-a de qualquer uma das classes de exceção de topo, como Exception.
#
# Imagine que criou uma aritmética completamente nova, regida pelas suas próprias leis e teoremas. É evidente que a divisão também foi redefinida, e tem de se comportar de uma forma diferente da divisão de 
# rotina. É também claro que esta nova divisão deve levantar a sua própria exceção, diferente da ZeroDivisionError, mas é razoável assumir que em algumas circunstâncias, você (ou o utilizador da sua 
# aritmética) pode querer tratar todas as divisões zero da mesma maneira.
#
# Exigências como estas podem ser satisfeitas da forma apresentada no editor. Veja o código, e vamos analisá-lo:
#
#    Definimos a nossa própria exceção, denominada MyZeroDivisionError, derivado a partir da incorporada ZeroDivisionError. Como pode ver, decidimos não acrescentar novos componentes à classe.
#
#    Com efeito, uma exceção a esta classe pode ser - dependendo do ponto de vista desejado - tratada como uma simples ZeroDivisionError, ou considerada separadamente.
#
#    A função do_the_division() levanta ou uma exceção MyZeroDivisionError ou ZeroDivisionError , dependendo do valor do argumento.
#
#    A função é invocada quatro vezes no total, enquanto as duas primeiras invocações são tratadas utilizando apenas um ramo except (o mais geral) e os dois últimos com dois ramos diferentes, capazes de 
# distinguir as exceções (não se esqueça: a ordem dos ramos faz uma diferença fundamental!)



class MyZeroDivisionError(ZeroDivisionError):	
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:		
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')
