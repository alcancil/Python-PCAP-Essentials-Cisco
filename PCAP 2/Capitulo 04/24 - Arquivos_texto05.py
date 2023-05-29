# Processamento de ficheiros de texto: readlines()
#
# Outro método, que trata o ficheiro de texto como um conjunto de linhas e não de carateres, é readlines().
#
# A classe readlines() , quando invocado sem argumentos, tenta ler todo o conteúdo do ficheiro, e devolve uma lista de strings, um elemento por linha de ficheiro.
#
# Se não tiver a certeza se o tamanho do ficheiro é suficientemente pequeno e não quiser testar o SO, pode convencer o método readlines() a ler não mais do que um número especificado de bytes ao mesmo tempo 
# (o valor de retorno permanece o mesmo - é uma lista de uma string).
#
# Sinta-se à vontade para experimentar o seguinte código de exemplo para compreender como o método readlines() funciona:

s = open("25-text.txt")
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
s.close()

# O tamanho máximo aceite do buffer de input é passado para o método como seu argumento.
#
# Pode esperar que readlines() pode processar o conteúdo de um ficheiro de forma mais eficaz do que readline(), uma vez que pode precisar de ser invocado menos vezes.
#
# Nota: quando não há nada a ler do ficheiro, o método devolve uma lista vazia. Utilize-o para detetar o fim do ficheiro.
#
# Na medida do tamanho do buffer, é de esperar que o seu aumento possa melhorar o desempenho de input, mas não há nenhuma regra de ouro para isso - tente você mesmo encontrar os valores ótimos.
#
# Veja o código no editor. Modificámo-lo para lhe mostrar como usar readlines().

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('25-text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))



# Decidimos usar um buffer de 15 bytes. Não pense que se trata de uma recomendação.
#
# Utilizámos esse valor para evitar a situação em que a primeira invocação readlines() consome o ficheiro inteiro.
#
# Queremos que o método seja forçado a trabalhar mais, e a demonstrar as suas capacidades.
#
# Existem dois nested loops no código: o externo utiliza o resultado de readlines()para iterar através dele, enquanto que o interior imprime as linhas caratere a caratere.