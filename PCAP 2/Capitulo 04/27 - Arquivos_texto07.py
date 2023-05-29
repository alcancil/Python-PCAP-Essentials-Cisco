# Lidar com ficheiros de texto: write()
#
# Escrever ficheiros de texto parece ser mais simples, pois de facto existe um método que pode ser utilizado para realizar tal tarefa.
#
# O método é chamado write() e espera apenas um argumento - uma string que será transferida para um ficheiro aberto (não esquecer - o modo aberto deve refletir a forma como os dados são transferidos - 
# escrever um ficheiro aberto em modo de leitura não será bem sucedido).
#
# Nenhum caratere newline é adicionado ao argumento write(), pelo que terá de ser você próprio a adicioná-lo se quiser que o ficheiro seja preenchido com um certo número de linhas.
#
# O exemplo no editor mostra um código muito simples que cria um ficheiro com o nome newtext.txt (nota: o modo aberto w assegura que o ficheiro será criado do zero, mesmo que este exista e contenha dados) e 
# depois coloca dez linhas no mesmo.
#
# A string a ser gravada consiste na linha da palavra, seguida do número da linha. Decidimos escrever o conteúdo da string caratere a caratere (isto é feito pelo loop for interno) mas não é obrigado a fazê-lo # desta forma.
#
# Só queríamos mostrar-lhe que write() é capaz de operar em carateres individuais.
#
# O código cria um ficheiro preenchido com o seguinte texto:
# line #1
# line #2
# line #3
# line #4
# line #5
# line #6
# line #7
# line #8
# line #9
# line #10
#
# output
#
# Pode imprimir o conteúdo do ficheiro para a consola?
#
# Encorajamo-lo a testar o comportamento do método write() localmente na sua máquina.

from os import strerror

try:
	fo = open('28-newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))