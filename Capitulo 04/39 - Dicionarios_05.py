# Como utilizar um dicionário: modificar e adicionar valores
# 
# Atribuir um novo valor a uma chave existente é simples - visto os dicionários serem totalmente mutáveis, não há obstáculos para os modificar.
#
# Vamos substituir o valor "chat" com "minou", o que não é muito preciso, mas funcionará bem com o nosso exemplo.
#
# Veja:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)


# O output é:
# {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}
#
# output
#
# Adicionar uma nova chave
#
# Adicionar um novo par key-value a um dicionário é tão simples como alterar um valor - basta atribuir um valor a uma nova chave, previamente inexistente.
# 
# Nota: este é um comportamento muito diferente em relação às listas, que não permitem atribuir valores a índices inexistentes.
#
# Vamos adicionar um novo par de palavras ao dicionário - um pouco estranho, mas ainda assim válido:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)


# O output do exemplo:
# {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}

