# Como o Python encontra propriedades e métodos: continuação
#
# Agora é possível formular uma declaração geral descrevendo o comportamento do Python.
#
# Quando se tenta aceder à entidade de qualquer objeto, o Python tentará (por esta ordem):
#
#    encontrá-lo dentro do próprio objeto;
#    encontrá-lo em todas as classes envolvidas na linha de herança do objeto, de baixo para cima;
#
# Se ambos os itens acima falharem, uma exceção (AttributeError) é levantada.
#
# A primeira condição pode precisar de alguma atenção adicional. Como sabe, todos os objetos derivados de uma determinada classe podem ter diferentes conjuntos de atributos, e alguns dos atributos podem ser 
# acrescentados ao objeto muito tempo após a sua criação.
#
# O exemplo no editor resume isto numa linha de herança de três níveis. Analise-o cuidadosamente.
#
# Todos os comentários que fizemos até agora estão relacionados com herança única, quando uma subclasse tem exatamente uma superclasse. Esta é a situação mais comum (e a mais recomendada também).
#
# O Python, no entanto, oferece muito mais aqui. Nas próximas lições, vamos mostrar-lhe alguns exemplos de herança múltipla.

class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
