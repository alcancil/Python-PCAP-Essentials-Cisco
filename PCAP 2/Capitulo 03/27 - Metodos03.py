# Métodos em detalhe: continuação
#
# Se nomear um método como este: __init__, não será um método regular - será um construtor.
#
# Se uma classe tem um construtor, é invocada automática e implicitamente quando o objeto da classe é instanciado.
#  
# O construtor:
#
#    é obrigado a ter o parâmetro self (é definido automaticamente, como de costume);
#    pode (mas não é necessário) ter mais parâmetros do que apenas self; se isto acontecer, a forma como o nome da classe é utilizado para criar o objeto deve refletir a definição __init__ ;
#    pode ser utilizada para configurar o objeto, ou seja, inicializar devidamente o seu estado interno, criar variáveis de instância, instanciar quaisquer outros objetos se a sua existência for necessária, 
# etc.
#
# Veja o código no editor. O exemplo mostra um construtor muito simples a trabalhar.
#
# Execute-o. Output do código:
# object
#
# output
#
# Observe que o construtor:
#
#    não pode devolver um valor, uma vez que foi concebido para devolver um objeto recém-criado e nada mais;
#    não pode ser invocado diretamente do objeto ou de dentro da classe (pode invocar um construtor de qualquer uma das subclasses do objeto, mas discutiremos esta questão mais tarde).


class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)