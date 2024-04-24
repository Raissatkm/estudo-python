nota1 = float(input("Digite o primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 7 :
    print("aluno aprovado, a media foi:" , media)
elif media >= 5:
    print('Aluno em recuperação, a media foi:', media)
else: 
    print("Aluno reprovado, a media foi:", media)