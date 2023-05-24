
Herança única vs. herança múltipla

Como já sabe, não existem obstáculos à utilização de herança múltipla em Python. Pode derivar qualquer nova classe a partir de mais de uma classe previamente definida.

Existe apenas um "mas". O facto de o poder fazer não significa que tenha de o fazer.

Não se esqueça disso:

    uma única classe de herança é sempre mais simples, mais segura e mais fácil de compreender e manter;

    a herança múltipla é sempre arriscada, pois tem muito mais oportunidades de cometer um erro na identificação destas partes das superclasses, que irão influenciar efetivamente a nova classe;

    herança múltipla pode tornar o overriding extremamente complicado; além disso, a utilização da função super() torna-se ambígua;




    a herança múltipla viola o princípio da responsabilidade única (mais detalhes aqui: https://en.wikipedia.org/wiki/Single_responsibility_principle) uma vez que faz uma nova classe de duas (ou mais) classes que nada sabem uma sobre a outra;

    sugerimos fortemente a herança múltipla como a última de todas as soluções possíveis - se precisar realmente das muitas funcionalidades diferentes oferecidas pelas diferentes classes, a composição pode ser uma alternativa melhor.



