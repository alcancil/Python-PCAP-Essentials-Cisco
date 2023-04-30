
# Key takeaways: dicionários
#
# 1. Os dicionários são coleções de dados desordenados*, alteráveis (mutáveis), e indexados. (*Em Python 3.6x, os dicionários tornaram-se ordenados por defeito.
#
# Cada dicionário é um conjunto de chaves: pares de valores. Pode criá-lo usando a seguinte sintaxe:
my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
    }


# 2. Se quiser aceder a um item de dicionário, pode fazê-lo fazendo referência à sua chave dentro de um par de parêntesis retos (ex. 1) ou usando o método get() (ex. 2):
pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # outputs: soil

item_2 = pol_eng_dictionary.get("woda")
print(item_2)    # outputs: water


# 3. Se quiser alterar o valor associado a uma chave específica, pode fazê-lo referindo-se ao nome da chave do item da seguinte forma:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]    
print(item)  # outputs: lock


# 4. Para adicionar ou remover uma chave (e o valor associado), utilize a seguinte sintaxe:
phonebook = {}    # an empty dictionary

phonebook["Adam"] = 3456783958    # create/add a key-value pair
print(phonebook)    # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook)    # outputs: {}


# Também pode inserir um item num dicionário utilizando o método update() , e remover o último elemento usando o método popitem() , por exemplo:
pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower'}


# 5. Pode utilizar o loop for para percorrer um dicionário, por exemplo:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for item in pol_eng_dictionary:
    print(item) 

# outputs: zamek
#          woda
#          gleba



# 6. Se quiser percorrer as chaves e valores de um dicionário, pode usar o método items() , por exemplo:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)


# 7. Para verificar se uma determinada chave existe num dicionário, pode utilizar a in keyword:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

if "zamek" in pol_eng_dictionary:
    print("Yes")
else:
    print("No")


# 8. Pode utilizar a keyword del para remover um item específico, ou apagar um dicionário. Para remover todos os itens do dicionário, é necessário utilizar o clear() método:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(len(pol_eng_dictionary))    # outputs: 3
del pol_eng_dictionary["zamek"]    # remove an item
print(len(pol_eng_dictionary))    # outputs: 2

pol_eng_dictionary.clear()   # removes all the items
print(len(pol_eng_dictionary))    # outputs: 0

del pol_eng_dictionary    # removes the dictionary


# 9. Para copiar um dicionário, use o copy() método:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()

