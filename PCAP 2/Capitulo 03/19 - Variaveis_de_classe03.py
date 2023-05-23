# Variáveis de classe: continuação
#
# Dissemos-lhe antes que as variáveis de classe existem mesmo quando nenhuma instância de classe (objeto) tenha sido criada.
#
# Agora vamos aproveitar a oportunidade para lhe mostrar a diferença entre estas duas variáveis __dict__ , a da classe e a do objeto.
#
# Veja o código no editor. A prova está lá.
# 
# Vamos analisar mais de perto:
#
#    Definimos uma classe chamada ExampleClass;
#
#    A classe define uma variável de classe chamada varia;
#
#    O construtor de classe define a variável com o valor do parâmetro;
#
#    Nomear a variável é o aspeto mais importante do exemplo porque:
#        Alterar a atribuição para self.varia = val criaria uma variável de instância com o mesmo nome que o da classe;
#        Alterar a atribuição para varia = val operaria na variável local de um método; (encorajamo-lo vivamente a testar os dois casos acima referidos - isto facilitar-lhe-á a lembrar-se da diferença)
#    A primeira linha do código fora da classe imprime o valor do atributo ExampleClass.varia ; nota - usamos o valor antes que o primeiro objeto da classe seja instanciado.
#
# Execute o código no editor e verifique o seu output.
#
# Como pode ver, a classe __dict__ contém muito mais dados do que a contraparte do seu objeto. A maioria deles são inúteis agora - aquele que queremos que verifique cuidadosamente mostra o valor varia 
# corrente.
#
# Observe que o __dict__ do objeto está vazio - o objeto não tem variáveis de instância.

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)
