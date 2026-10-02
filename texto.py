aluno=input("digite o nome do aluno: ")
ano_nascimento=int(input("digite o ano de nascimento: "))
nota1=float(input("digite a nota do aluno: "))
nota2=float(input("digite a nota do aluno: "))
nota3=float(input("digite a nota do aluno: "))
nota4=float(input("digite a nota do aluno: "))
nota5=float(input("digite a nota do aluno: "))

media=(nota1+nota2+nota3+nota4+nota5) /5

if media >=7:
    situacao = "aprovado"
elif media>= 5:
    situacao = "recuperação"
else:
    situacao= "reprovado"    

ano_atual=2026
idade=(ano_atual-ano_nascimento)

print (f"aluno: {aluno}")
print(f"idade: {idade}")
print(f"media: {media}")
print(f"situação:{situacao}")




# crie um algoritimo que leia tres valores (lados de um triangulo)
# determine se formam um triangulo, e se formar verifique 
# se é um equilatero, isoceles ou escaleno

lado1=float(input("digite o lado 1 do triangulo"))
lado2=float(input("digite o lado 2 do triangulo"))
lado3=float(input("digite o lado 3 do triangulo"))


if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 +lado1 > lado2:
    if lado1==lado2 and lado2==lado3:
        print("equilatero")
    elif lado1==lado2 or lado2==lado3 or lado1==lado3:
        print("isoceles")
    else:
        print("escaleno")

else:
    print("não é um triangulo")