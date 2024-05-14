def imprimir_padrao(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Teste a função
n = int(input("Digite o valor de n: "))
imprimir_padrao(n)