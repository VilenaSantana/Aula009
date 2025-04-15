a = int(input("Quantos alunos tem na sala? "))
soma = 0
x = 0
while x<a:
    valor = int(input("Diga a nota do aluno: "))
    soma+=valor
    x+=1
m = soma/a
print(f"A da turma media é {m}")