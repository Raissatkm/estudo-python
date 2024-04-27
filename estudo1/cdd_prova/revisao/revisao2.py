"""Crie um código que leia um número
diferente de zero e diga se este número
é positivo ou negativo"""
# Solicita ao usuário para inserir um número
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero e exibe o resultado
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
