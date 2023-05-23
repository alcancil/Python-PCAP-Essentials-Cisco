# Investigar classes
#
# O que se pode descobrir sobre as classes em Python? A resposta é simples - tudo.
#
# Tanto a reflexão como a introspeção permitem a um programador fazer qualquer coisa com cada objeto, independentemente da sua proveniência.
#
# Analise o código no editor.
#
# A função chamada incIntsI() obtém um objeto de qualquer classe, digitaliza o seu conteúdo a fim de encontrar todos os atributos inteiros com nomes que comecem por i, e incrementa-os por um.
#
# Impossível? De modo algum!
#
# É assim que funciona:
#
#    linha 1: definir uma classe muito simples...
#    linhas 3 a 10: ...e preenchê-la com alguns atributos;
#    linha 12: esta é a nossa função!
#    linha 13: digitalizar o atributo __dict__ , procurando todos os nomes de atributos;
#    linha 14: se um nome começar com i...
#    linha 15: ...use a função getattr() para obter o seu valor atual; nota: getattr() toma dois argumentos: um objeto, e o seu nome de propriedade (como uma string), e devolve o valor do atributo atual;
#    linha 16: verificar se o valor é do tipo inteiro, e utilizar a função isinstance() para este fim (discutiremos isto mais tarde);
#    linha 17: se a verificação correr bem, aumente o valor da propriedade fazendo uso da função setattr() ; a função toma três argumentos: um objeto, o nome da propriedade (como uma string) e o novo valor # da propriedade.
#
# Output do código:
# {'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
# {'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}
#
# output
#
# E é tudo!
#

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
