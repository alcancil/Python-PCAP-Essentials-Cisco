# For
#
# Pode ser que existam situações em que se precise parar um Loop for.
# Se utilizarmos esse recurso, depois poderemos retomar o loop de onde parou.
#
# Para isso existem as funcoes break e continue
#
# Veja o exemplo
#
#
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")