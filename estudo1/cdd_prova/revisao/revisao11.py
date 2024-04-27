"""11. Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias."""
ano = int(input("Digite o ano de nascimento: "))
dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))

# Calcula a idade em dias
idade_em_dias = (ano * 365) + (mes * 30) + dia

# Exibe a idade da pessoa em dias
print("A idade da pessoa em dias é:", idade_em_dias)