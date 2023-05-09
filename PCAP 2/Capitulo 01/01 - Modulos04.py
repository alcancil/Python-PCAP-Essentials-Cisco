# Modulos
#
# Conforme os codigos vao crescendo, o numero de modulos tambem vai aumentando. Entao e possivel de se armazenar os modulos dentro de uma pasta para melhor organizar a estrtura dos codigos.
# Porem agora a forma da importacao dos modulos muda ligeiramente. Observe:

import modulos.utilidades, modulos.utilidades02


print(modulos.utilidades.soma(2, 3))
print(modulos.utilidades02.mult(2, 3))

