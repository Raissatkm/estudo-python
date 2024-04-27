# Solicita ao usuário que insira os dois valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Verifica se os valores são iguais
if valor1 == valor2:
    print("Os valores são iguais. Por favor, insira valores diferentes.")
elif valor1 > valor2:
    # Se o primeiro valor for maior que o segundo, troca os valores
    valor1, valor2 = valor2, valor1

# Exibe os valores em ordem crescente
print("Os valores em ordem crescente são:", valor1, "e", valor2)
