vmes = int(input("Digite um número inteiro: "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Número Inválido")

"""
Primeiro, o programa solicita ao usuário que insira um número inteiro representando um mês.
Em seguida, o programa começa a verificar qual mês corresponde ao número fornecido pelo usuário. Ele faz isso usando uma série de declarações if-elif-else.

Se o número for igual a 1, o programa imprime "Janeiro".
Se for igual a 2, imprime "Fevereiro".
E assim por diante, até chegar a 12 para "Dezembro".

Se o número inserido pelo usuário não corresponder a nenhum desses meses (ou seja, se não estiver no intervalo de 1 a 12), o programa executará o bloco de código dentro do else, que imprime "Número Inválido".

Dessa forma, o programa identifica o mês correspondente ao número inserido pelo usuário e o imprime na tela. Se o número não corresponder a nenhum mês válido, ele imprime "Número Inválido".

"""