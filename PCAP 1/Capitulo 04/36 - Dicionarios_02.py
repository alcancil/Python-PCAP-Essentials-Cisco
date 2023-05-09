# Como usar um dicionário?
#
# Se quiser obter algum dos valores, tem de entregar um key-value válido:
# print(dictionary['cat'])
# print(phone_numbers['Suzy'])
#
#
# A obtenção do valor de um dicionário assemelha-se a uma indexação, especialmente graças aos parêntesis retos que rodeiam o valor da chave.
#
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Print the values here.

print(dictionary['cat'])
print(phone_numbers['Suzy'])



# Nota:
#
#    se a chave for uma string, é necessário especificá-la como uma string;
#    as chaves são sensíveis a maiúsculas e minúsculas: 'Suzy' é algo diferente de 'suzy'.
#
# O snippet produz duas linhas de texto:
# chat
# 5557654321
#
# output
#
# E agora a notícia mais importante: não se deve usar uma chave inexistente. Tentar algo assim:
# print(phone_numbers['president'])
#
#
# causará um erro de runtime. Tente fazê-lo.
#
# Felizmente, há uma maneira simples de evitar tal situação. O operador in , juntamente com o seu companheiro, not in, podem salvar esta situação.
#
# O seguinte código procura com segurança algumas palavras francesas:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


# O output do código é o seguinte:
# cat -> chat
# lion is not in dictionary
# horse -> cheval
#
# output
#
# NOTA
# 
# Quando se escreve uma expressão grande ou longa, pode ser uma boa ideia mantê-la verticalmente alinhada. É assim que pode tornar o seu código mais legível e mais fácil de programar, por exemplo
# Example 1:

dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

# Example 2:

phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }


# Tais formas de formatação de código são chamadas hanging indents (indentações penduradas).