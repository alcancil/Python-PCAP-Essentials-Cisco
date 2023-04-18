# A vida interna das listas
# Agora queremos mostrar-lhe uma característica importante, e muito surpreendente, das listas, que as distingue fortemente das variáveis comuns.
#
# Queremos que o memorize - pode afetar os seus programas futuros, e causar graves problemas se esquecido ou negligenciado.
#
# Veja o snippet no editor.
#
# O programa:
#
# cria uma lista de um elemento chamada list_1;
# atribui-o a uma nova lista chamada list_2;
# altera o único elemento de list_1;
# imprime list_2.
# A parte surpreendente é o facto de que o programa fará o output: [2], não [1], que parece ser a solução óbvia.
#
#
# As listas (e muitas outras entidades complexas de Python) são armazenadas de formas diferentes das variáveis ordinárias (escalares).
#
# Pode-se dizer que:
#
# o nome de uma variável ordinária é o nome do seu conteúdo;
# o nome de uma lista é o nome de um local de memória onde a lista é armazenada.
# Leia estas duas linhas mais uma vez - a diferença é essencial para compreender aquilo de que vamos falar a seguir.
#
# A atribuição: list_2 = list_1 copia o nome do array, não o seu conteúdo. Com efeito, os dois nomes (list_1 e list_2) identificam o mesmo local na memória do computador. Modificar um deles afeta o outro, e 
# vice-versa.
#
# Como se lida com isso?

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
