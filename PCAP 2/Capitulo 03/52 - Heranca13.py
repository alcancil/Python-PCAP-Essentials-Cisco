# Como o Python encontra propriedades e métodos: continuação
#
# Vejamos o exemplo no editor.
#
# A classe Sub herda bens de duas superclasses, Left e Right (estes nomes destinam-se a ser significativos).
#
# Não há dúvida de que a variável de classe var_right vem da classe Right , e var_left vem de Left respetivamente.
#
# Isto é evidente. Mas de onde var vem? É possível adivinhá-lo? O mesmo problema é encontrado com o método fun() - será invocado a partir de Left ou a partir de Right? Vamos executar o programa - o seu output # é:
# L LL RR Left
# 
# output
#
# Isto prova que ambos os casos pouco claros têm uma solução dentro da Left classe. Será esta uma premissa suficiente para formular uma regra geral? Sim, é.
#
# Podemos dizer que o Python procura componentes de objeto na seguinte ordem:
#
#    dentro do próprio objeto;
#    nas suas superclasses, de baixo para cima;
#    se houver mais do que uma classe num determinado caminho de herança, o Python analisa-os da esquerda para a direita.
#
# Precisa de mais alguma coisa? Basta fazer uma pequena emenda no código - substituir: class Sub(Left, Right): por: class Sub(Right, Left):, em seguida, execute o programa novamente e veja o que acontece.
#
# O que vê agora? Nós vemos:
# R LL RR Right
#
# output
#
# Vê o mesmo, ou algo diferente?


class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
