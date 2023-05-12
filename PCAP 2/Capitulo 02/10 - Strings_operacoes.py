# Operações em strings: continuação
#
# Não pense que a imutabilidade de uma string limita a sua capacidade de operar com strings.
#
# A única consequência é que tem de se lembrar disso, e implementar o seu código de uma forma ligeiramente diferente - veja o exemplo do código no editor.

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)



# Esta forma de código é totalmente aceitável, funcionará sem contornar as regras do Python, e trará o alfabeto latino completo para o seu ecrã:
# abcdefghijklmnopqrstuvwxyz
#
# output
#
# Poderá perguntar-se se a criação de uma nova cópia de uma string, cada vez que modifica o seu conteúdo, piora a eficácia do código.
#
# Sim, piora. Um pouco. No entanto, não é de todo um problema.