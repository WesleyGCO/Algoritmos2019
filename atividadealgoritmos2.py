#10) Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
# x = int(input("Digite o primeiro número: "))
# y = int(input("Digite o segundo número: "))
# z = int(input("Digite o terceiro número: "))
# if (x > y) and (x > y):
#         print("O número", x, "é o maior!")
# elif (y > x) and (y > z):
#     print("O número", y, "é o maior!")
# else:
#     print("O número", z, "é o maior!")

#11) Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.
# A = int(input("Digite o valor de A: "))
# B = int(input("Digite o valor de B: "))
# C = int(input("Digite o valor de C: "))
#
# if (A > B and A > C and B > C):
#     print("A ordem crescente é", C, B, A,)
# elif (B > A and B > C and A > C):
#     print("A ordem crescente é", C, A, B,)
# elif (C > A and C > B and B > A):
#     print("A ordem crescente é", A, B, C,)
# elif (A > B and A > C and B < C):
#     print(" A ordem crescente é", B, C, A )
# elif (B > A and B > C and A < C):
#     print("A ordem crescente é", A, C, B)
# else:
#     print("A ordem crescente é", B, A, C)

#19) Construa um programa que mostre menu exatamente como o exemplo abaixo e implemente as funções necessárias:

# print(""" \t\t\t MENU DE OPÇÕES
#
# 1) Somar 2 números
# 2) Potência Y de um número X
# 3) Raiz quadrada de X
# """)
# opção = int(input("Digite a opção desejada: "))
#
# if ( opção == 1 ):
#
#     x = float(input("Digite o valor de x: "))
#     y = float(input("Digite o valor de y: "))
#     print("A soma dos números digitados é", x + y,)
#
# elif (opção == 2):
#     x = float(input("Digite um número: "))
#     y = float(input("Digite a potência: "))
#     print("O resultado é", x ** y)
#
# elif ( opção == 3):
#     x = int(input("Digite um número: "))
#     print("A raiz quadrada desse número é", x ** (1/2))
# else:
#     print("Opção inválida!")

#20) Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corporal), que é definida como sendo a relação entre o peso e o quadrado da altura (informada em metros, ex: 1.80) do indivíduo. Ou seja: IMC = peso/altura² e a situação do peso é determinada pela tabela abaixo

print("\t\t\t CÁLCULO DE IMC")

altura = float(input("Digite sua altura em centímetros: "))
peso = float(input("Digite seu peso: "))
print("  ")

print("Seu IMC é", peso / (altura ** 2))
