# Comparar strings
#
# As strings de Python podem ser comparadas utilizando o mesmo conjunto de operadores que os utilizados em relação aos números.
#
# Dê uma vista de olhos a estes operadores - todos eles também podem comparar strings:
#
#    ==
#    !=
#    >
#    >=
#    <
#    <=
#
# Existe um "mas" - os resultados de tais comparações podem por vezes ser um pouco surpreendentes. Não se esqueça que Python não está ciente (não pode de forma alguma) de questões linguísticas subtis - apenas # compara valores de code point, caratere por caratere.
#
# Os resultados que se obtêm com tal operação são por vezes surpreendentes. Vamos começar com os casos mais simples.
#
# Duas strings são iguais quando consistem nos mesmos carateres, na mesma ordem. Pela mesma forma, duas strings não são iguais quando não consistem nos mesmos carateres, na mesma ordem.
#
# Ambas as comparações dão True como resultado:
print('alpha' == 'alpha')
print('alpha' != 'Alpha')

#
# A relação final entre strings é determinada pela comparação do primeiro caratere diferente em ambas as strings (ter sempre em mente os code points ASCII/UNICODE).
#
# Quando se comparam duas strings de comprimentos diferentes, e a mais curta é idêntica à mais longa, a string mais longa é considerada maior.
# 
# Tal como aqui:
print('alpha' < 'alphabet')

#
# A relação é True.
#
# A comparação de strings é sempre sensível às maiúsculas e minúsculas (letras maiúsculas são tomadas como menores do que as minúsculas).
#
# A expressão é True:
print('beta' > 'Beta')

