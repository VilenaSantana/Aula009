n1 =int(input("Diga um número: "))
n2 = int(input("Diga outro número: "))
while n2 == 0:
    n2 = int(input("Diga um número valido maior que 0: "))
r = n1/n2
print(r)
