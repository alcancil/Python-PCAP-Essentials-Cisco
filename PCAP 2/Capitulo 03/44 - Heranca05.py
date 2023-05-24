# Herança: o operador is .
#
# Há também um operador Python que vale a pena mencionar, pois refere-se diretamente a objetos - aqui está ele:
# object_one is object_two
#
#
# O operador is verifica se duas variáveis (object_one e object_two aqui) se referem ao mesmo objeto.
#
# Não se esqueça que as variáveis não armazenam os objetos em si, mas apenas os manípulos que apontam para a memória interna do Python.
#
# Atribuir um valor de uma variável de objeto a outra variável não copia o objeto, mas apenas o seu manípulo. É por isso que um operador como is pode ser muito útil em circunstâncias particulares.
#
# Dê uma vista de olhos ao código no editor. Vamos analisá-lo:
#
#    existe uma classe muito simples equipada com um construtor simples, criando apenas uma propriedade. A classe é utilizada para instanciar dois objetos. O primeiro é então atribuído a outra variável, e a 
# sua propriedade val é incrementada por um.
#    depois, o operador is é aplicado três vezes para verificar todos os pares de objetos possíveis, e todos os valores de propriedade val também são impressos.
#    a última parte do código realiza outra experiência. Após três atribuições, ambas as cadeias contêm os mesmos textos, mas estes textos são armazenados em objetos diferentes.
#
# O código imprime:
# False
# False
# True
# 1 2 1
# True False
#
# output
#
# Os resultados demonstram que object_1 e object_3 são na verdade os mesmos objetos, enquanto string_1 e string_2 não são, apesar de seu conteúdo ser o mesmo.


class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
