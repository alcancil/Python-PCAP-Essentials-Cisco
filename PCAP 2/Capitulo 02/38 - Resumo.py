
Key takeaways

1. Strings podem ser comparadas com strings utilizando operadores de comparação geral, mas compará-las com números não dá nenhum resultado razoável, visto nenhuma string poder ser igual a qualquer número. Por exemplo:

    string == number é sempre False;
    string != number é sempre True;
    string >= number levanta sempre uma exceção.


2. A ordenação de listas de strings pode ser feita por:

    uma função chamada sorted(), criando uma lista nova e ordenada;
    um método chamado sort(), que classifica a lista in situ


3. Um número pode ser convertido numa string usando a função str() .

4. Uma string pode ser convertida num número (embora não todas as strings) usando ou a função int() ou a função float() . A conversão falha se uma string não contiver uma imagem numérica válida (uma exceção é então levantada).



Exercício 1

Qual das linhas a seguir descreve uma condição verdadeira?
'smith' > 'Smith'
'Smiths' < 'Smith'
'Smith' > '1000'
'11' < '8'


1, 3 e 4


Exercício 2

Qual é o output esperado do seguinte código?
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])


are


Exercício 3

Qual é o resultado esperado do seguinte código?
s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)


O código levanta uma exceção ValueError . 