#escreva um programa em python que pergunte tres informações ao usuario
#é um estudante (uma string "sim"ou "nao"")
#dia da semana(uma string "terca"ou öutro")
#tipo de salaüma string "vip"ou "comum")
#o programa deve exibir "desconto aplicado" ou "valor integral""
#
#regra "o cliente ganha o desconto se for estudante ou for terca e a sala for comum"

estudante=input("é estudante?")
dia_semana=input("dia da semana?")
tipo_sala=input("tipo de sala?")



if estudante=="sim" or dia_semana=="terca" and tipo_sala=="comum":
    print("ganhou desconto paizão")
else:
    print("valor integral")