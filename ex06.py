'''pin = int(1234)
senha = input("Digite um  senha de 4 número: ")
t = 3
x = 0
if senha == pin:
    print("Senha correta")
else:
 while x < t:
     senha = input("Senha incorreta, digite novamente: ")
     x +=1
     if senha == pin:
         print("Senha correta")'''

senha_correta = "1234"
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Senha correta! Acesso liberado.")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta. Tentativas restantes: {limite_tentativas - tentativas}")
else:
    print("Senha bloqueada. Número máximo de tentativas excedido.")
