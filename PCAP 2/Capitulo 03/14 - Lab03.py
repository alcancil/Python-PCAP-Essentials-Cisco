# Tempo estimado
#
# 15-30 minutos
# Nível de dificuldade
#
# Fácil/Médio
# Objetivos
#
#    Melhorar as competências do aluno na definição de subclasses;
#    adicionar uma nova funcionalidade a uma classe existente.
#
# Cenário
#
# A sua tarefa é alargar ligeiramente as capacidades da classe Queue . Queremos que ele tenha um método sem parâmetros que devolva True se a queue estiver vazia e False caso contrário.
#
# Complete o código que fornecemos no editor. Execute-o para verificar se ele produz um resultado semelhante ao nosso.
#
# Abaixo pode copiar o código que utilizámos no laboratório anterior:
#
# class QueueError(IndexError):
#    pass
#
#
# class Queue:
#     def __init__(self):
#        self.queue = []
#     def put(self,elem):
#        self.queue.insert(0,elem)
#     def get(self):
#         if len(self.queue) > 0:
#             elem = self.queue[-1]
#             del self.queue[-1]
#             return elem
#         else:
#            raise QueueError
#
#
#
# Output esperado
#
# 1
# dog
# False
# Queue empty

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def put(self, elem):
        self.items.append(elem)

    def get(self):
        if not self.items:
            raise QueueError("Queue is empty")
        return self.items.pop(0)


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")