# Variáveis de classe
#
# Uma variável de classe é uma propriedade que existe apenas numa cópia e é armazenada fora de qualquer objeto.
#
# Nota: não existe uma variável de instância se não houver nenhum objeto na classe; existe uma variável de classe numa cópia, mesmo que não haja objetos na classe.
#
# As variáveis de classe são criadas de forma diferente dos seus irmãos de instância. O exemplo dir-lhe-á mais:
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)




# Veja:
#
#    existe uma atribuição na primeira lista da definição da classe - define a variável chamada counter até 0; inicializar a variável dentro da classe mas fora de qualquer um dos seus métodos torna a variável # uma variável de classe;
#    o acesso a tal variável tem o mesmo aspeto que o acesso a qualquer atributo de instância - pode vê-la no corpo do construtor; como pode ver, o construtor incrementa a variável por um; com efeito, a 
# variável conta todos os objetos criados.
#
# A execução do código causará o seguinte output:
# {'_ExampleClass__first': 1} 3
# {'_ExampleClass__first': 2} 3
# {'_ExampleClass__first': 4} 3
#
# output
#
# Duas conclusões importantes vêm do exemplo:
#
#    variáveis de classe não são mostradas num objeto __dict__ (isto é natural porque as variáveis de classe não são partes de um objeto) mas pode sempre tentar olhar para a variável do mesmo nome, mas ao 
# nível da classe - vamos mostrar-lhe isto muito em breve;
#    uma variável de classe apresenta sempre o mesmo valor em todas as instâncias de classe (objetos)

