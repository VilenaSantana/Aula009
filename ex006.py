senhacorreta = "1234"
tentativas = 0
limitetentativas = 3
while tentativas < limitetentativas:
    senha = input("Digite a senha: ")
    if senha == senhacorreta:
        print("Senha correta! Acesso liberado.")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta. Tentativas restantes: {limitetentativas - tentativas}")
else:
    print("Senha bloqueada. Número máximo de tentativas excedido.")


'''pin = 1234
tent = 0
msg = "Senha bloqueada"
while tent < 3:
    senha = int(input("Digite a senha: "))
    if senha == pin
        msg= "Senha correta"
        break
    tent+=1
print(msg)'''
