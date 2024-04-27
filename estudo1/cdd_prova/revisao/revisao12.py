"""12. Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores."""
numeroEleitores = int(input("Digite o numero de eleitores:"))
numeroBrancos = int(input("Digite os votos em branco:"))
numeroNulos = int(input("Digite os votos nulos:"))
numeroValidos = int(input("Digite os numeros validos:"))
percentualBrancos = (numeroBrancos/ numeroEleitores) * 100
percentualNulos = (numeroNulos/ numeroEleitores) * 100
percentualValidos = (numeroValidos / numeroEleitores) * 100

# Exibe os percentuais de cada tipo de voto
print("Percentual de votos brancos:", percentualBrancos, "%")
print("Percentual de votos nulos:", percentualNulos, "%")
print("Percentual de votos válidos:", percentualValidos, "%")