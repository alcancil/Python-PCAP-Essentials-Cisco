# Então, o que é que têm em comum, geradores e compreensões de lista? Existe alguma conexão entre eles? Sim. Uma conexão bastante ligeira, mas inequívoca.
#
# Apenas uma mudança pode transformar qualquer compreensão de lista num gerador.

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)

# Compreensões de lista vs. geradores
#
# Agora olhe para o código abaixo e veja se consegue encontrar o detalhe que transforma uma compreensão de lista num gerador:

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()


# São os parêntesis. Os parêntesis retos fazem uma compreensão, os parêntesis curvos fazem um gerador.
# 
# O código, no entanto, quando executado, produz duas linhas idênticas:
# 1 0 1 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1 0 1 0
#
# output
#
# Como pode saber que a segunda tarefa cria um gerador, não uma lista?
# 
# Há algumas provas que lhe podemos mostrar. Aplicar a função len() para ambas as entidades.
# 
# len(the_list) avaliará a 10. Claro e previsível. len(the_generator) irá levantar uma exceção, e verá a seguinte mensagem:
# TypeError: object of type 'generator' has no len()
#
# output
#
# Claro que não é necessário guardar a lista ou o gerador - pode criá-los exatamente no local onde precisa deles - tal como aqui:

for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()


# Nota: a mesma aparência do output não significa que ambos os loops funcionam da mesma forma. No primeiro loop, a lista é criada (e iterada através) como um todo - ela existe de facto quando o loop está a # ser executado.
#
# No segundo loop, não existe qualquer lista - existem apenas valores subsequentes produzidos pelo gerador, um por um.
#
# Realize as suas próprias experiências.