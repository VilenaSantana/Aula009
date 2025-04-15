
n1 = int(input("Digite nota 1: "))
while n1 < 0 or n1 > 10:
    n1 = int(input("Digite nota 1 valida: "))

n2 = int(input("Digite nota 2: "))
while n2 < 0 or n2 > 10:
    n2 = int(input("Digite nota 2 valida: "))

m = (n1+n2)/2
print(m)
