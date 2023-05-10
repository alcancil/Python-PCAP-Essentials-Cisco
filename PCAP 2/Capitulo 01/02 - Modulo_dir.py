
# Trabalhar com módulos padrão
#
# Antes de começarmos a passar por alguns módulos Python padrão, queremos introduzir-lhe a função dir() . Não tem nada a ver com o comando dir que conhece de consolas Windows e Unix, visto dir() não mostrar o # conteúdo de uma diretoria/pasta de disco, mas não há como negar que faz algo realmente semelhante - é capaz de revelar todos os nomes fornecidos através de um determinado módulo.
#
# Há uma condição: o módulo tem de ter sido previamente importado como um todo (isto é, utilizar a import module instrução - from module não é suficiente).
#
# A função devolve uma lista ordenada alfabeticamente contendo todos os nomes de entidades disponíveis no módulo identificados por um nome passado para a função como argumento:
# dir(module)
#
#
# Nota: se o nome do módulo tiver sido aliased, deve usar o alias, não o nome original.
#
# A utilização da função dentro de um script regular não faz muito sentido, mas ainda assim é possível.
#
# Por exemplo, pode executar o seguinte código para imprimir os nomes de todas as entidades dentro do math módulo:
import math

for name in dir(math):
    print(name, end="\t")


# O código de exemplo deve produzir o seguinte output:
# __doc__	__loader__	__name__	__package__	__spec__	acos	acosh	asin	asinh	atan	atan2	atanh	ceil	copysign	cos	cosh	degrees	e	erf	erfc	exp	expm1	fabs	factorial	floor	fmod
#	frexp	fsum	gamma	hypot	isfinite	isinf	isnan	ldexp	lgamma	log	log10	log1p	log2	modf	pi	pow	radians	sin	sinh	sqrt	tan	tanh	trunc	
#
# output
#
#
# Já reparou nestes estranhos nomes que começam com __ no topo da lista? Falaremos mais sobre eles quando falarmos sobre as questões relacionadas com a escrita dos seus próprios módulos.
#
# Alguns dos nomes podem trazer memórias de lições de matemática, e provavelmente não terá quaisquer problemas em adivinhar o seu significado.
#
# Utilizar a função dir() dentro de um código pode não parecer muito útil - normalmente quer saber o conteúdo de um determinado módulo antes de escrever e executar o código.
#
# Felizmente, pode executar a função diretamente na consola Python (IDLE), sem necessidade de escrever e executar um script separado.
#
# É assim que pode ser feito:
import math
dir(math)


