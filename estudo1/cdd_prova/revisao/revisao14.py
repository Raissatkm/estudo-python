"""14. Escreva um algoritmo para ler uma
temperatura em graus Fahrenheit, calcular
e escrever o valor correspondente em graus
Celsius (baseado na fórmula abaixo):
C = ((F - 32)/9)*5
Observação: Para testar se a sua resposta
está correta saiba que 100 ⍛C = 212 F"""
# Solicita ao usuário que insira a temperatura em graus Fahrenheit
temperatura_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Calcula a temperatura correspondente em graus Celsius
temperatura_celsius = ((temperatura_fahrenheit - 32) / 9) * 5

# Exibe o valor correspondente em graus Celsius
print("A temperatura em graus Celsius é:", temperatura_celsius, "°C")
