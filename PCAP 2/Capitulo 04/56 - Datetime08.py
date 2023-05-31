# Os loops time .
#
# Para além dos módulos time , a biblioteca padrão de Python oferece um módulo chamado time, que fornece uma função relacionada com o tempo. Já teve a oportunidade de aprender a função chamada time ao 
# discutir a classe date . Agora vamos olhar para outra função útil disponível neste módulo.
#
# Deve passar muitas horas em frente de um computador enquanto faz este curso. Por vezes pode sentir a necessidade de fazer uma sesta. Porque não? Vamos escrever um programa que simula a curta sesta de um 
# estudante. Dê uma vista de olhos ao código no editor.
#
# Resultado:
# I'm very tired. I have to take a nap. See you later.
# I slept well! I feel great!
#
# output
#
# A parte mais importante do código de exemplo é o uso da função sleep (sim, pode recordá-la de um dos labs anteriores do curso), o que suspende a execução do programa durante um determinado número de 
# segundos.
#
# No nosso exemplo são 5 segundos. Tem razão, é uma sesta muito curta.
#
# Prolongue o sesta do aluno alterando o número de segundos. Note que a função sleep aceita apenas um número inteiro ou um número floating-point.


import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)
