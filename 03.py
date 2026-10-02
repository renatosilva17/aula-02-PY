#escreva um programa em python que receba as seguintes quatro informações do usuario
#renda mensal (um numero float)
#score de crédito ( um numero inteiro de 0 a 1000)
# possui bens como garantia?(uma string "sim"ou "nao")
#tem histórico de inadimplencia?(uma string "sim"ou "nao")
# o emprestimo será aprovado se o cliente cumprir  uma das regras abaixo
#
#regra 1 ter renda mensal maior ou igual a 3000 e score de crédito maior ou igual a 600 e nao ter histórico de inadimplencia.
#regra 2 independentemente da renda ou score, se o cliente nao tiver histórico de inadimplencia  e possuir bens como garantia, ele tambem é aprovado
#se o cliente não se encaixar em nenhuma das duas regras, o emprestimo será reprovado

renda_mensal=float(input("qual sua renda mensal? "))
score=int(input("qual seu score? "))
bens=input("tem bens como garantia? ")
historico=input("tem histórico pae? ")

if renda_mensal >= 3000 and score >= 600 and historico == "nao":
    print("emprestimo aprovado")

elif historico =="nao" and bens =="sim":
 print("emprestimo aprovado")

else:
    print("empretimo reprovado")






