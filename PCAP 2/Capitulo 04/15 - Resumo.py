
# Key takeaways
#
# 1. Um iterador é um objeto de uma classe que fornece pelo menos dois métodos (sem contar com o construtor!):
# 
#     __iter__() é invocado uma vez quando o iterador é criado e devolve o próprio objeto do iterador;
#     __next__() é invocado para fornecer o valor da próxima iteração e levanta uma exceção StopIteration quando a iteração chega ao fim.
#
#
# 2. O método yield só pode ser utilizada dentro de funções. A declaração yield suspende a execução da função e faz com que a função devolva o argumento do yield como resultado. Tal função não pode ser 
# invocada de forma regular - a sua única finalidade é ser usada como um gerador (ou seja, num contexto que requer uma série de valores, como um loop for .)
#
# 3. Uma expressão condicional é uma expressão construída usando o operador if-else . Por exemplo:
print(True if 0 >=0 else False)
#
#
# tem como output True.
#
# 4. Uma compreensão de lista torna-se um gerador quando usada dentro de parêntesis curvos (usada dentro de parêntesis retos, produz uma lista regular). Por exemplo:
for x in (el * 2 for el in range(5)):
    print(x)

# tem como output 02468.
#
# 4. Uma função lambda é uma ferramenta para a criação de funções anónimas. Por exemplo:
def foo(x,f):
    return f(x)

print(foo(9, lambda x: x ** 0.5))
#
#
# tem como output 3.0.
#
# 5. O módulo map(fun, list) cria uma cópia de um argumento list , e aplica a função fun a todos os seus elementos, devolvendo um gerador que fornece o novo conteúdo da lista elemento por elemento. Por 
# exemplo:

short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)


# tem como output ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor'].
#
# 6. A função filter(fun, list) cria uma cópia desses elementos list , que causam que a função fun devolva True. O resultado da função é um gerador que fornece o novo conteúdo da lista elemento por 
# elemento. Por exemplo:

short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)


# tem como output ['Python', 'Monty'].
#
# 7. O closure é uma técnica que permite o armazenamento de valores apesar do facto de o contexto em que foram criados já não existir. Por exemplo:

def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner


b_tag = tag('<b>')
print(b_tag('Monty Python'))


# tem como output <b>Monty Python</b>
#
#
# Exercício 1
#
# Qual é o output esperado do seguinte código?

class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  # Yes, we know that y is not always considered a vowel.
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]


vowels = Vowels()
for v in vowels:
    print(v, end=' ')


# a e i o u y
#
#
# Exercício 2
#
# Escreva uma função lambda, definindo a parte menos significativa do seu argumento inteiro, e aplique-a à função map() para produzir a string 1 3 3 5 na consola.
# any_list = [1, 2, 3, 4]
# even_list = # Complete the line here.
# print(even_list)
#
#
# list(map(lambda n: n | 1, any_list))
#
#
#
# Exercício 3
#
# Qual é o output esperado do seguinte código?

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))


# And*Now*for*Something*Completely*Different
#
# Nota
#
# PEP 8, o Guia de Estilo do Código Python, recomenda que os lambdas não sejam atribuídos a variáveis, mas sim que sejam definidos como funções.
#
# Isto significa que é melhor usar uma declaração def , e evitar utilizar uma declaração de atribuição que ligue uma expressão lambda a um identificador. Por exemplo:
#
# Recommended:
# def f(x): return 3*x
#
#
# Not recommended:
# f = lambda x: 3*x
#
# A vinculação de lambdas a identificadores geralmente duplica a funcionalidade da declaração def . Utilizar declarações def , por outro lado, gera mais linhas de código.
#
# É importante compreender que a realidade gosta frequentemente de desenhar os seus próprios cenários, que não seguem necessariamente as convenções ou recomendações formais. A decisão de os seguir ou não 
# dependerá de muitas coisas: as suas preferências, outras convenções adotadas, diretrizes internas da empresa, compatibilidade com o código existente, etc. Esteja atento a isto.