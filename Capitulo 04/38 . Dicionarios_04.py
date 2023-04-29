# Como usar um dicionário: Os métodos items() e values() .
#
# Outra forma é baseada na utilização de um método de dicionário chamado items(). O método devolve tuples (este é o primeiro exemplo onde os tuples são algo mais do que apenas um exemplo de si mesmos) onde 
# cada tuple é um par key-value.
#
# É assim que funciona:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)


# Note-se a forma como o tuple foi utilizado como uma for variável de loop.
#
# O exemplo imprime:
# cat -> chat
# dog -> chien
# horse -> cheval
#
# output
#
# Há também um método chamado values(), que funciona de forma semelhante a keys(), mas devolve valores.
#
# Aqui está um exemplo simples:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)


# Como o dicionário não consegue encontrar automaticamente uma chave para um determinado valor, o papel deste método é bastante limitado.
#
# Este é o output esperado:
# cheval
# chien
# chat