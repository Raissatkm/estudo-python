numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

"""Neste exemplo, usamos elif (abreviação de "else if") para verificar se o número é menor que zero. Se nenhum dos casos anteriores for verdadeiro, a instrução else é executada, o que significa que o número é zero."""