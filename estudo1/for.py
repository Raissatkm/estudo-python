#for item in sequencia :
# bloco de código a ser executado para cada item

"""item é uma variável que representa o item atual na iteração.
sequencia é a sequência sobre a qual você está iterando."""

numeros = [1, 2, 3, 4, 5, 6]

for numero in  numeros :
    print(numero)
    
"""Neste exemplo:

numeros é a lista sobre a qual estamos iterando.
numero é a variável que representa cada item na lista durante a iteração.
O bloco de código dentro do laço for é simplesmente print(numero), que imprime cada número da lista."""

for i in range(5):
    print(i)

"""Neste caso, range(5) gera uma sequência de números de 0 a 4, e o laço for itera sobre essa sequência, imprimindo cada número. A saída seria: 0
1
2
3
4
"""