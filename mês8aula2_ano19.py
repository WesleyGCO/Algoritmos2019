"""
Procedimentos com parâmetros
Os parâmetros são valores/dados (adicionais) que são fornecidos
para um procedimento
"""
# import math
# # Neste caso, o parâmetro é o valor 9
# r = math.sqrt(9)

# Neste procedimento, x é um parâmetro
# def msg(x):
#     print(x)
# msg("oi")

# def msg(a, b, c):
#     print(a)
#     print(b)
#     print(c)
# msg(1, 2, 3)


# def somar(a, b, c):
#     soma = a + b + c
#     print(soma)
#
# # somar(2, 3, 5)
# # somar(34, 21, 43)
# somar(12, 22, 4)

#------------------------------------------------------------

# def multiplicar(a, b):
#     mult = a * b
#     print(mult)
#
# multiplicar(3, 5)


# def calcularRaiz (a):
#     raiz = a ** (1/2)
#     print(raiz)
#
# calcularRaiz(2)


# def calcularPotencia(a, b):
#     potencia = a ** b
#     print(calcularPotencia)
#
# calcularPotencia(4, 3)


# def calcularTabuada(a):
#     mult = 1
#     while(mult <= 10):
#         x = a * mult
#         print(x)
#         mult = mult + 1
#
# calcularTabuada(3)


# def imprimirVetor(v1):
#     print(v1)
#
# imprimirVetor([1, 2, 3, 4, 5, 23, 21, 32, 67, 99])


# def encontrarMaior(a):
#     maior = a[0]
#     for cont in range(0, len(a)):
#         if (maior < a[cont]):
#             maior = a[cont]
#     print("Maior: ", maior)
# encontrarMaior([23, 32, 12, 3, 2, 1, 4, -15, 65, 9, 100, 100.5])


# def encontrarMenor(a):
#     menor = a[0]
#     for cont in range(0, len(a)):
#         if (menor > a[cont]):
#             menor = a[cont]
#     print("Menor: ", menor)
#
# encontrarMenor([12, 343, 432, 654, 56, 904.5, 34212, 3])


#-------------------------------------------------

# v1 = [12, 34, 32, 14, 65, 7, 8, 3, 98, 100]
#
# def encontrarMaior(a):
#     maior = a[0]
#     for cont in range(0, len(a)):
#         if (maior < a[cont]):
#             maior = a[cont]
#     print("Maior: ", maior)
#
# encontrarMaior(v1)
#
# def encontrarMenor(a):
#     menor = a[0]
#     for cont in range(0, len(a)):
#         if(menor > a[cont]):
#             menor = a[cont]
#     print("Menor: ", menor)
#
# encontrarMenor(v1)


#-------------------------------------------------

# def numero(a):
#     if (a %2 == 0):
#         print("Número é par!")
#     else:
#         print("Número é ímpar!")
#
# for cont in range(1, 5):
#     x = int(input("Insira um número: "))
#
# numero(x)
