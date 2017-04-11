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
#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
#população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
#número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
#taxas de crescimento.

pais_a = 80000
pais_b = 200000
ano = 0


while pais_a < pais_b:
    pais_a += pais_a * 0.03
    pais_b += pais_b * 0.015
    ano = ano + 1

    print("O país A ultrapassa o país B em %d anos" %ano)