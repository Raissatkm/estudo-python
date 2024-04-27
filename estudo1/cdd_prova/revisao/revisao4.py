"""4. Crie um algoritmo que receba 3
números e informe qual o maior entre
eles."""

numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))
numero3 = int(input("Digite o terceiro numero:"))

if numero1 >= numero2 and numero1 >= numero3:
    maiornumero = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maiornumero = numero2
else:
    maiornumero = numero3
print("O maior numero é", maiornumero)