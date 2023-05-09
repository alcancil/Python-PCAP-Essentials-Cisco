# Key takeaways: continuação
#
# Exercício 1
#
# Qual é o output do seguinte snippet?

x = 5
y = 10
z = 8

print(x > y)
print(y > z)

#
# Verifique
# False
# True
# output
#
#
# Exercício 2
#
# Qual é o output do seguinte snippet?

x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)


# Verifique
# False
# True
# output


# Exercício 3

# Qual é o output do seguinte snippet?

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)


# Verifique
# True
# False
# output
#

# Exercício 4
#
# Qual é o output do seguinte snippet?

x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")


# Verifique
# True
# True
# else
# output