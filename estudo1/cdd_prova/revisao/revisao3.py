"""3. Crie um código que leia a idade de
uma pessoa e diga em qual ano ela
nasceu"""
idade = int(input("Digite a sua idade:"))
mes = int(input("Digite o mês do seu nascimento:"))
anoAtual = 2024
mesAtual = 4
if mes >= mesAtual:
    anoNascimento = (anoAtual -idade)-1
else:
    anoNascimento = (anoAtual - idade)
print(anoNascimento)