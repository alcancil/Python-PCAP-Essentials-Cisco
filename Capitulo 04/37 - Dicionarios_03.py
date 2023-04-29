# Como usar um dicionário: o keys()
#
# Os dicionários podem ser consultados usando o loop for , como listas ou tuples?
#
# Não e sim.
#
# Não, porque um dicionário não é um tipo de sequência - o loop for é inútil com ele.
#
# Sim, porque existem ferramentas simples e muito eficazes que podem adaptar qualquer dicionário aos for requisitos do loop (por outras palavras, construindo um link intermediário entre o dicionário e uma 
# entidade de sequência temporária).
#
# O primeiro deles é um método chamado keys(), possuído por cada dicionário. O método devolve um objeto iterável que consiste em todas as chaves recolhidas dentro do dicionário. Ter um grupo de chaves 
# permite-lhe aceder a todo o dicionário de uma forma fácil e prática.
#
# Tal como aqui:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])


# O output do código é o seguinte:
# horse -> cheval
# dog -> chien
# cat -> chat
#
# output
#
# O método sorted() .
#
# Quer que seja classificado? Apenas enriqueça o loop for , para obter tal forma:

# for key in sorted(dictionary.keys()):


# A função sorted() fará o seu melhor - o output irá ficar assim:
# cat -> chat
# dog -> chien
# horse -> cheval