# escreva um programa em python que peça as seguintes informações:
#idade (um numero inteiro)
#altura em centimetros (um numero interio)
#tem autorização dos pais? (uma string: "sim"ou "não")
#
#o programa deve exibir "acesso liberado!" se o visitante puder andar no brinquedo, ou "acesso negado". caso o contrario.
#
#regra 
# o visitante pode entrar se:
#tiver idade maior ou igual a 12 e altura maior ou igual a 140 ou
#se tiver autorização igual a "sim".

idade=int(input("qual a sua idade muleke? "))
altura=int(input("e sua altura pirralho? "))
autorização=(input("tem autorização? "))


if idade>=12 and altura>=140 and autorização=="sim":
 print("acesso liberado")
else:
 print("acesso negado")