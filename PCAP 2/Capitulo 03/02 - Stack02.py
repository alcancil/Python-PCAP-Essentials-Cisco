# A stack - a abordagem ao objeto
#
# Evidentemente, a ideia principal continua a ser a mesma. Usaremos uma lista como armazenamento da stack. Só temos que saber como colocar a lista na classe.
#
# Comecemos do início absoluto - é assim que começa a stack objetiva:
# class Stack:
#
#
# Agora, esperamos duas coisas dela:
#
#    queremos que a classe tenha uma propriedade como armazenamento da stack - temos de "instalar" uma lista dentro de cada objeto da classe (nota: cada objeto tem de ter a sua própria lista - a lista não 
# deve ser partilhada entre diferentes stacks)
#    em seguida, queremos que a lista seja escondida da vista dos utilizadores da classe.
#
# Como é isto feito?
#
# Ao contrário de outras linguagens de programação, o Python não tem meios de lhe permitir declarar tal propriedade sem mais nem menos.
#
# Em vez disso, é necessário acrescentar uma declaração ou instrução específica. As propriedades têm que ser adicionadas à classe manualmente.
#
# Como garante que tal atividade ocorre cada vez que a nova stack é criada?
#
# Há uma forma simples de o fazer - é necessário equipar a classe com uma função específica - a sua especificidade é dupla:
#
#    tem de ser nomeada de forma estrita;
#    é invocada implicitamente, quando o novo objeto é criado.
#
# Tal função é chamada de construtor, pois o seu objetivo geral é a construção de um novo objeto. O construtor deve saber tudo sobre a estrutura do objeto, e deve realizar todas as inicializações 
# necessárias.
#
# Vamos adicionar um construtor muito simples à nova classe. Veja o snippet:
# class Stack:
#     def __init__(self):
#         print("Hi!")
#
#
# stack_object = Stack()
#
#
# E agora:
#
#    o nome do construtor é sempre __init__;
#     tem de ter pelo menos um parâmetro (discutiremos isto mais tarde); o parâmetro é usado para representar o objeto recentemente criado - pode usar o parâmetro para manipular o objeto, e para o 
# enriquecer com as propriedades necessárias; fará uso disto em breve;
#    nota: o parâmetro obrigatório é geralmente chamado self - é apenas uma convenção, mas deve segui-la - simplifica o processo de leitura e compreensão do seu código.
#
# O código está no editor. Execute-o agora.
#
# Aqui está o seu output:
# Hi!
#
# output
#
# Nota - não há vestígios de invocação do construtor dentro do código. Foi invocado implícita e automaticamente. Vamos fazer uso disso agora.


class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")


stack_object = Stack()  # Instantiating the object.