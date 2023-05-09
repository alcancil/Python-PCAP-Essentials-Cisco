# Tuples e dicionários podem trabalhar em conjunto
# 
# Preparámos um exemplo simples, mostrando como tuples e dicionários podem trabalhar em conjunto.
#
# Vamos imaginar o seguinte problema:
#
#    é necessário um programa para avaliar as notas médias dos alunos;
#    o programa deve pedir o nome do aluno, seguido da sua pontuação única;
#    Os nomes podem ser indicados em qualquer ordem;
#    a introdução de um nome vazio termina a introdução dos dados (nota 1: a introdução de uma pontuação vazia levantará a exceção ValueError, mas não se preocupe com isso agora, verá como lidar com tais 
# casos quando falarmos de exceções na segunda parte da série de cursos Python Essentials)
#    uma lista de todos os nomes, juntamente com a pontuação média avaliada, deve então ser emitida.
#
# Veja o código no editor. Esta é a forma de o fazer.
#
# Agora, vamos analisá-lo linha a linha:
#
#   linha 1: criar um dicionário vazio para os dados introduzidos; o nome do aluno é usado como chave, enquanto todas as notas associadas são armazenadas num tuple (o tuple pode ser um valor de dicionário - # 
# isso não é um problema)
#    linha 3: entrar num loop "infinito" (não se preocupe, vai quebrar-se no momento certo)
#    linha 4: ler o nome do aluno aqui;
#    linha 5-6: se o nome for uma string vazia (), leave the loop;
#    linha 8: pedir uma das pontuações do aluno (um inteiro do intervalo 0-10)
#    linha 9-10: se a pontuação introduzida não estiver dentro do intervalo de 0 a 10, deixar o loop;
#    linha 12-13: se o nome do aluno já estiver no dicionário, alongar o tuple associado com a nova pontuação (note o operador +=)
#    linha 14-15: se este for um novo aluno (desconhecido do dicionário), criar uma nova entrada - o seu valor é um tuple de um elemento contendo a pontuação introduzida;
#    linha 17: iterar através dos nomes dos alunos ordenados;
#    linha 18-19: inicializar os dados necessários para avaliar a média (soma e contador)
#    linha 20-22: iteramos através do tuple, tomando todas as pontuações subsequentes e atualizando a soma, juntamente com o contador;
#    linha 23: avaliar e imprimir o nome e a pontuação média do aluno.
#
# Este é um registo de uma conversa que tivemos com o nosso programa:
# Enter the student's name: Bob
# Enter the student's score (0-10): 7
# Enter the student's name: Andy
# Enter the student's score (0-10): 3
# Enter the student's name: Bob
# Enter the student's score (0-10): 2
# Enter the student's name: Andy
# Enter the student's score (0-10): 10
# Enter the student's name: Andy
# Enter the student's score (0-10): 3
# Enter the student's name: Bob
# Enter the student's score (0-10): 9
# Enter the student's name:
# Andy : 5.333333333333333
# Bob : 6.0


school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)