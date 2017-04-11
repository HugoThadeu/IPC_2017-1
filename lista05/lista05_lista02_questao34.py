#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Joelson Pereira Lima 			1715310060
# Gabriel Nascimento de Oliveira 	1715310052
# Hugo Thadeu Silva Cardoso             1715310013
# Jandinne Duarte de Oliveira 		1015070265
# Gabriel de Queiroz Souza		1715310044
# Guilherme Silva de Oliveira		1715310034
#
#Escreva um algoritmo em PORTUGOL que calcule o quociente da divisão de A por B
#(número inteiros e positivos), ou seja, A div B, através de subtrações sucessivas. Esses
#dois valores são passados pelo usuário através do teclado.

A = int(input("Coloque o valor de A: "))
B = int(input("Coloque o valor de B: "))


while A >= B:
    A = A - B

    print("O resto da divisão de A por B é: ", A)