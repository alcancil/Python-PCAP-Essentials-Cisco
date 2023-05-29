# Processamento de ficheiros de texto: continuação
#
# O último exemplo que queremos apresentar mostra uma característica muito interessante do objeto devolvido pela função open() no modo de texto.
#
# Achamos que pode surpreendê-lo - o objeto é uma instância da classe iterável.
#
# Estranho? De modo algum. Utilizável? Sim, completamente.
#
# O protocolo de iteração definido para o objeto de ficheiro é muito simples - o seu método __next__ apenas devolve a próxima linha lida a partir do ficheiro.
#
# Além disso, pode esperar que o objeto invoque automaticamente close() quando qualquer uma das leituras do ficheiro chegar ao fim do ficheiro.
#
# Olhe para o editor e veja como o código se tornou agora simples e claro.

from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('25-text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
