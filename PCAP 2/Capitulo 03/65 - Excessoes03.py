# Exceções são classes
#
# Todos os exemplos anteriores se contentavam em detetar um tipo específico de exceção e responder-lhe de uma forma adequada. Agora vamos aprofundar, e olhar para dentro da própria exceção.
#
# Provavelmente não ficará surpreendido ao saber que exceções são classes. Além disso, quando é levantada uma exceção, um objeto da classe é instanciado, e passa por todos os níveis de execução do programa, 
# procurando o ramo exceto o que está preparado para lidar com ele.
#
# Tal objeto traz alguma informação útil que pode ajudá-lo a identificar com precisão todos os aspetos da situação pendente. Para atingir esse objetivo, o Python oferece uma variante especial da cláusula de 
# exceção - pode encontrá-la no editor.
#
# Como pode ver, a declaração except é prolongada, e contém uma frase adicional que começa com a keyword as , seguida por um identificador. O identificador é concebido para apanhar o objeto de exceção, para  # que se possa analisar a sua natureza e tirar as devidas conclusões.
#
# Nota: o scope do identificador abrange o seu ramo except , e não vai mais longe.
#
# O exemplo apresenta uma forma muito simples de utilizar o objeto recebido - basta imprimi-lo (como pode ver, o output é produzido pelo método do objeto __str__() ) e contém uma breve mensagem descrevendo a # razão.
#
# A mesma mensagem será impressa se não houver nenhum bloco de encaixe except no código, e o Python é forçado a lidar com ela sozinho.

try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())
