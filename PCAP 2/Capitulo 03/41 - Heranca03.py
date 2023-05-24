
Herança - porquê e como?

O termo herança (inheritance) é mais antigo do que a programação de computadores, e descreve a prática comum de passar vários bens de uma pessoa para outra após a morte da primeira. O termo, quando relacionado à programação de computadores, tem um significado completamente diferente.

O conceito de herança


Vamos definir o termo para os nossos propósitos:

A herança é uma prática comum (na programação de objetos) de passar atributos e métodos da superclasse (definida e existente) para uma classe recém-criada, chamada subclasse.

Por outras palavras, a herança é uma forma de construir uma nova classe, não a partir do zero, mas usando um repertório de traços já definidos. A nova classe herda (e esta é a chave) todo o equipamento já existente, mas é capaz de adicionar alguns novos se necessário.

Graças a isso, é possível construir classes mais especializadas (mais concretas) usando alguns conjuntos de regras e comportamentos gerais predefinidos.



O fator mais importante do processo é a relação entre a superclasse e todas as suas subclasses (nota: se B é uma subclasse de A e C é uma subclasse de B, isto também significa que C é uma subclasse de A, uma vez que a relação é totalmente transitória).

Um exemplo muito simples de herança de dois níveis é apresentado aqui:
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


Todas as classes apresentadas estão vazias por agora, pois vamos mostrar-lhe como funcionam as relações mútuas entre as super e as subclasses. Em breve iremos preenchê-las com conteúdos.

Podemos dizer que:

    A classe Vehicle é a superclasse para ambas as classes LandVehicle e TrackedVehicle ;
    A classe LandVehicle é uma subclasse de Vehicle e uma superclasse de TrackedVehicle ao mesmo tempo;
    A classe TrackedVehicle é uma subclasse de ambas as classes Vehicle e LandVehicle .

O conhecimento acima vem da leitura do código (por outras palavras, nós conhecemo-lo porque o podemos ver).

O Python sabe o mesmo? É possível perguntar ao Python sobre isso? Sim, é.


