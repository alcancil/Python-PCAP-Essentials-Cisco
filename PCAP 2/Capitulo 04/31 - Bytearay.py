
# O que é um bytearray?
#
# Antes de começarmos a falar de ficheiros binários, temos de lhe falar de uma das classes especializadas que o Python utiliza para armazenar dados amorfos.
#
# Dados amorfos são dados que não têm formato ou forma específica - são apenas uma série de bytes.
#
# Isto não significa que estes bytes não possam ter o seu próprio significado, ou não possam representar qualquer objeto útil, por exemplo, gráficos bitmap.
#
# O aspeto mais importante disto é que no local onde temos contacto com os dados, não somos capazes, ou simplesmente não queremos, saber nada sobre isso.
#
# Os dados amorfos não podem ser armazenados utilizando qualquer um dos meios anteriormente apresentados - eles não são strings nem listas.
#
# Deve haver um recipiente especial capaz de tratar de tais dados.
#
#
#
# O Python tem mais do que um desses recipientes - um deles é um bytearray de nome de classe especializado - como o nome sugere, é um array contendo bytes (amorfos).
#
# Se quiser ter um tal recipiente, por exemplo, para ler uma imagem bitmap e processá-la de qualquer forma, precisa de o criar explicitamente, utilizando um dos construtores disponíveis.
#
# Dê uma vista de olhos:

data = bytearray(10)


# Tal invocação cria um objeto bytearray capaz de armazenar dez bytes.
#
# Nota: tal construtor preenche todo o array com zeros.
