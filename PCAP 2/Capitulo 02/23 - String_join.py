# Os loops join() .
#
# A classe join() é bastante complicado, por isso deixe-nos guiá-lo passo a passo:
#
#    como o seu nome sugere, o método realiza uma junção (em inglês, join) - espera um argumento como uma lista; deve ter a certeza de que todos os elementos da lista são strings - o método irá levantar uma  # exceção TypeError de outra forma;
#     todos os elementos da lista serão unidos numa string, mas...
#     ... a string a partir da qual o método foi invocado é usada como um separador, colocado entre as strings;
#     a string recém-criada é devolvida como um resultado.
#
# Dê uma vista de olhos no exemplo no editor. Vamos analisá-lo:
#
#    o método join() é invocado de dentro de uma string contendo uma vírgula (a string pode ser arbitrariamente longa, ou pode estar vazia)
#    o argumento joiné uma lista contendo três strings;
#    o método devolve uma nova string.
#
# Aqui está:
# omicron,pi,rh

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))