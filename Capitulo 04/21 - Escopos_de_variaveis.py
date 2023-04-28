# Escopos de variveis em Funcoes
#
#
#
#  Existem dois tipos de Variaveis que pode ser utilizadas: as GLOBAIS e as LOCAIS
#
#  A variavel GLOBAL é aquela que pode ser acessada de qualquer parte do programa. Já as variveis LOCAIS, só podem ser utilizadas pnde foram defindas.
#  Acompanhe o exemplo. Aqui vanmos criar um programa onde temos uma funcao também.

VAR_GLOBAL = "Essa e uma variavel de escopo GLOBAL !!!!"


def mostrar_valor():
    var_local = "Essa e uma variavel de escopo LOCAL"
    print("O conteudo de var_local e : ")
    print(var_local)

print("-" * 100)
print("Exemplo 01")
print("-" * 100)

print("\nExecutando a funcao mostrar_valor(): ")
mostrar_valor()
print("\nMostrar o valor da variavel de escopo GLOBAL : ")
print(VAR_GLOBAL)

# Nesse exemplo, fica claro que se quisermos mostrar o conteudo da variavel var_local, só conseguiremos se chamarmos a funcao var_local pois ela só funciona localmente dentro da funcao
# Vamos analisar o exemplo 2 agora.

VAR_GLOBAL = "Essa e uma variavel de escopo GLOBAL !!!!"


def mostrar_valor():
    var_local = "Essa e uma variavel de escopo LOCAL"
    VAR_GLOBAL = "Apesar do nome, VAR_GLOBAL, essa e uma variavel LOCAL"
    print("O conteudo de var_local e : ")
    print(var_local)
    print(VAR_GLOBAL)

print("-" * 100)
print("Exemplo 02")
print("-" * 100)

print("\nExecutando a funcao mostrar_valor(): ")
mostrar_valor()
print("\nMostrar o valor da variavel de escopo GLOBAL : ")
print(VAR_GLOBAL)

# Repare no exemplo 02 que mesmo a variável VAR_GLOBAL que está fora da funcao tem o mesmo nome da variavel VAR_GLOBAL que está dentro da funcao. Porem, a que está fora tem escopo GLOBAL e pode ser
# utilizada em qualquer parte do programa. Ja a que esta dentro da funcao, so tem funcao local e, portanto, so pode ser utilizada quando se chama funcao. Mas e se quizessemos que a VAR_GLOBAL
# de dentro da funcao tive escopo GLOBAL ? Verifique o exemplo 3

def mostrar_valor():
    global VAR_GLOBAL
    VAR_GLOBAL = "Agora essa variavel tem escopo GLOBAL"
    var_local = "Essa e uma variavel de escopo LOCAL"
    print("O conteudo de var_local e : ")
    print(var_local)
    print(VAR_GLOBAL)

print("-" * 100)
print("Exemplo 03")
print("-" * 100)

print("\nExecutando a funcao mostrar_valor(): ")
mostrar_valor()
print("\nMostrar o valor da variavel de escopo GLOBAL : ")
print(VAR_GLOBAL)
