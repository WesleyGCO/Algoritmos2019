#Exercício 1

# def mostrarNumero():
#     num = int(input("Informe um número: "))

#     return num

# ============================================

#Exercício 2

# import random

# def importarNumero(num):
#     aleatorio = random.uniform(1, num)

#     return aleatorio

# =============================================

# Exercício 3

# def mes(x):
#     if (x == 1):
#         mes = ("Janeiro")
#     elif (x == 2):
#         mes = ("Fevereiro")
#     elif (x == 3):
#         mes = ("Março")
#     elif (x == 4):
#         mes = ("Abril")
#     elif (x == 5):
#         mes = ("Maio")
#     elif (x == 6):
#         mes = ("Junho")
#     elif (x == 7):
#         mes = ("Julho")
#     elif (x == 8):
#         mes = ("Agosto")
#     elif (x == 9):
#         mes = ("Setembro")
#     elif (x == 10):
#         mes = ("Outubro")
#     elif (x == 11):
#         mes = ("Novembro")
#     elif (x == 12):
#         mes = ("Dezembro")
#     else:
#         mes = ("mes inválido!")
#     return mes

# ================================================

#Exercício 4 (a)

# def quadrado():
#     a = int(input("Digite o valor do lado: "))
#     resultado = a * a
#     return resultado

#Exercício 4 (b)

# def retangulo():
#     b = int(input("Digite o valor da base: "))
#     h = int(input("Digite o valor da altura: "))
#     resultado = b * h
#     return resultado

#Exercício 4 (c)

# def triangulo():
#     b = int(input("Digite o valor da base: "))
#     h = int(input("Digite o valor da altura: "))
#     resultado = (b *h)/2
#     return resultado

#Exercício 4 (d)

# def trapezio():
#     B = int(input("Digite o valor da base maior: "))
#     h = int(input("Digite o valor da altura: "))
#     b = int(input("Digite o valor da base menor: "))
#     resultado = ((B * b) * h)/2
#     return resultado

# ================================================

#Exercício 5

# def fatorial(a):
#     fat = 1
#     i = 2
#     while (i <= a):
#         fat = fat * i
#         i = i + 1
#     resultado = fat
#     return fat

# ================================================

#Exercício 6

# def fatorialSeg(a):

# ================================================

#Exercício 7

# def maior(a):
#     maior = v1[0]
#     for cont in range(0, len(a)):
#         if (maior < a[cont]):
#             maior = a[cont]
#     return maior

# ================================================

#Exercício 8
# def menor(a):
#     menor = a[0]
#     for cont in range(0, len(a)):
#         if (menor > a[cont]):
#            menor = a[cont]
#     return menor 

# ================================================

#Exercício 9

# def mediaVetor(a):
#     soma = 0
#     for cont in range(0, len(a)):
#         soma = soma + a[cont]
#     media = soma / len(a)
#     return media

# ================================================

#Exercício 10

# def dobro(a):
#     v2 = [0]*len(a)
#     for cont in range(0, len(a)):
#         dobro = a[cont] * 2
#         v2[cont] = dobro
#     return v2       

# ================================================

#Exercício 11

# def data():
#    dt = input("Digite uma data no formato DD/MM/AAAA: ")
#    resultado = dt[0:2] + " de " + mes(int(dt[4:5])) + " de " + dt[6:]
#    return resultado

# ================================================

#Exercício 12

# def reverso(n):
#     print("convertendo ", n)
#     n = str(n)
#     reverso = ""
#     for cont in range(len(n)-1, -1, -1):
#         reverso = reverso + n[cont]
#     print("convertido ", reverso)
#     reverso = int(reverso)
#     return reverso

# ================================================

#Exercício 13

# def reversoNome(l):
#     print("Convertento ", l)
#     reversoN = ""
#     for cont in range(len(l) -1, -1, -1):
#         reversoN = reversoN + l[cont]
#     print("Convertido ", reversoN)
#     reverso = str(reversoN)
#     return reversoN

# ================================================

#Exercício 14

# def vogal(w):
#     print("Convertendo ", w)
#     vogal = 0
#     w = w.lower()
#     v1 = ["a", "e", "i", "o", "u"]
#     for cont in range(0, len(w)):
#         if (w[cont] in v1):
            # vogal = vogal + 1
#     print("Convertido ", w)
#     return vogal

# ================================================

#Exercício 15

# def embaralhado(c):
#     c = c.lower()
#     # print("Convertendo ", c)
#     import random
#     vet = []

#     for cont in range(0, len(c)):
#         # #gera um número
#         alea = random.randint(0, len(c) - 1)
#         while (alea in vet):
#             alea = random.randint(0, len(c) - 1)
#         vet.append(alea)
#     embaralhado = ""
#     for cont in range(0, len(vet)):
#         embaralhado = embaralhado + c[vet[cont]]
    
#     return embaralhado
