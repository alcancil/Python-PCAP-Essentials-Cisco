# Operações em strings: ord()
#
# Se quiser saber o valor do code point ASCII/UNICODE de um caratere específico, pode usar uma função chamada ord() (como em ordinal).
#
# A função precisa de uma string de um único caratere como seu argumento - violar este requisito causa uma exceção TypeError , e devolve um número que representa o code point do argumento.
#
# Veja o código no editor, e execute-o. O snippet faz o output:
# 97
# 32
#
# output
#
# Agora atribua valores diferentes para char_1 e char_2, por exemplo, α (alfa grego), e ę (uma letra no alfabeto polonês); em seguida execute o código e veja o resultado que ele produz. Realize as suas 
# próprias experiências.


# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))