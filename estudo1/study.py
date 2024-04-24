"""numero1 = int(input("Digite um numero do tipo inteiro"))
numero2 = int(input("Digte o segundo numero do tipo inteiro"))
soma = numero1 + numero2
print(soma)"""

login = "admin"
senha = 23 

login_dig = str(input("Digite seu login:"))
senha_dig = int(input("Digite sua senha:"))

if login == login_dig and senha == senha_dig:
    print("Acesso permitido!")
else: 
    print("Acesso negado")
