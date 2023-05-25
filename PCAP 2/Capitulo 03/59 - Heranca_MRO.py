# O que é o Method Resolution Order (MRO) e porque é que nem todas as heranças fazem sentido?
#
# MRO, em geral, é uma forma (pode-se chamar-lhe uma estratégia) em que uma determinada linguagem de programação analisa a parte superior da hierarquia de uma classe, a fim de encontrar o método de que ela # necessita atualmente. Vale a pena salientar que línguas diferentes utilizam ligeiramente (ou mesmo completamente) diferentes MROs. O Python é uma criatura única a este respeito, contudo, e os seus 
# costumes são um pouco específicos.
#
# Vamos mostrar-lhe como funciona o MRO de Python em dois casos peculiares, que são exemplos claros de problemas que podem ocorrer quando se tenta usar a herança múltipla de forma demasiado imprudente. 
# Vamos começar com um snippet que inicialmente pode parecer simples. Veja o que preparámos para si no editor.
#
# Temos a certeza de que, se analisar o snippet você mesmo, não verá quaisquer anomalias no mesmo. Sim, tem toda a razão - parece claro e simples, e não suscita preocupações. Se executar o código, este 
# produzirá o seguinte output previsível:
# bottom
# middle
# top
#
# output
#
# Sem surpresas até agora. Vamos fazer uma pequena alteração neste código. Veja:

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


# Consegue ver a diferença? Está escondida nesta linha:
#
# class Bottom(Middle, Top):
#
# Desta forma exótica, transformamos um código muito simples com um claro caminho de uma única herança num misterioso enigma de múltiplas heranças. “É válido?” pode-se perguntar. Sim, é. "Como é isso 
# possível?" deve perguntar agora, e esperamos que sinta realmente a necessidade de fazer esta pergunta.
#
# Como pode ver, a ordem em que as duas superclasses foram listadas entre parêntesis está em conformidade com a estrutura do código: a classe Middle precede a classe Top , assim como no caminho da herança 
# real.
#
# Apesar da sua estranheza, a amostra está correta e funciona como esperado, mas é preciso afirmar que esta notação não traz nenhuma nova funcionalidade ou significado adicional.
#
# Vamos modificar o código mais uma vez - agora vamos trocar os dois nomes de superclasse na definição de classe Bottom . Este é o aspeto que o snippet tem agora:

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Top, Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# Para antecipar a sua pergunta, diremos que esta emenda estragou o código, e que já não funcionará mais. Que pena. A ordem que tentamos forçar (Top, Middle) é incompatível com o caminho da herança que é 
# derivado da estrutura do código. O Python não vai gostar. Isto é o que veremos:
# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle
# 
# output
# 
# Achamos que a mensagem fala por si. O MRO de Python não pode ser distorcido ou violado, não só porque é assim que o Python funciona, mas também porque é uma regra a que se tem de obedecer.
