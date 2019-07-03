# Criação de vetores

# v1 = [1, 2, 3, 8, 4, 9, 0]
# v2 = [0]*6
#
# #Verificando o tamanho de cada um
#
# print("Tamanho do v1: ", len(v1))
# print("Tamanho do v2: ", len(v2))

print('''1)
a) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
b) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
c) Mostre na tela o dobro de todos os números.
d) Apresente na tela a soma de todos os números.
e) Apresente na tela a média geral dos valores contidos na lista.
f) Mostre na tela a quantidade de números pares.
''')
#a
# v1 = [1]*100
# for cont in range (0, 100):
#     v1 [cont] = cont + 1
# print(v1)


#b
# v1 = [1]*100
# y = 1
# for cont in range (len(v1) - 1, -1, -1 ):
#     v1 [cont] = y
#     y = y + 1
# print(v1)


#c
# # y = 100
# # v1 = [1]*100
# for cont in range (0, 100):
#     # v1 [cont] = cont * 2
#     # y = y + 1
#     print(v1[cont]*2)
# print(v1)


#d
# soma = 0
# v1 = [1]*100
# for cont in range (0, 100):
#     v1 [cont] = cont + 1
#     soma = soma + v1 [cont]
# print(soma)


#e
# v1 = [1]*100
# soma = 0
# media = soma / 100
# for cont in range (len(v1) - 1, -1, -1 ):
#     v1 [cont] = cont + 1
#     soma = soma + v1 [cont]
# print(media)

#f
# par = 0
# v1 = [1]*100
#
# for cont in range (0, 100):
#     v1 [cont] = cont + 1
#     if ((v1 [cont] %2) == 0):
#         par = par + 1
# print("Par: ", par)


#3
# nomes = [""]*5
# cont = 0
# # while (cont < len(nomes)):
# #      nomes[cont] = input("Informe um nome: ")
# #      cont = cont + 1
# #     print("Os nomes digitados foram: ", nomes[cont],)
# for cont in range(0, len(nomes)):
#     nomes[cont] = input("Informe um nome: ")
#     print(cont, ":", nomes[cont])


#4
# cont = 0
# x = int(input("Digite o valor do vetor: "))
#
# v1 = [0]*x
# for cont in range (0, len(v1)):
#     v1 [cont] = int(input("Digite valores dentro do vetor: "))
# cont = cont + 1
# print(v1)


#5
# Apresente os números do vetor em ordem inversa.

# for cont in range (len(v1), 0):
#     cont = cont - 1
# print(v1)

# Apresente a soma de todos os elementos.

# cont = 0
# x = int(input("Digite o valor do vetor: "))
# soma = 0
# v1 = [0]*x
# for cont in range (0, len(v1)):
#     v1 [cont] = int(input("Digite valores dentro do vetor: "))
#     soma = soma + v1 [cont]
# cont = cont + 1
# print(v1)
# print("Soma: ", soma)

# Calcule a média aritmética dos valores.

# cont = 0
# x = int(input("Digite o valor do vetor: "))
# soma = 0
#
# v1 = [0]*x
# for cont in range (0, len(v1)):
#     v1 [cont] = int(input("Digite valores dentro do vetor: "))
#     soma = soma + v1 [cont]
# cont = cont + 1
# print(v1)
# print("Média dos números: ", soma / len(v1))

# Liste na tela somente os números do vetor que estão em posições (índices) pares.

# cont = 0
# x = int(input("Digite o valor do vetor: "))
#
# v1 = [0]*x
# for cont in range (0, len(v1)):
#     v1 [cont] = int(input("Digite valores dentro do vetor: "))
# cont = cont + 1
# # print(v1)
#
# for cont in range (0, len(v1), 2):
#     print(v1 [cont])

#  Por exemplo: na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 o usuário teria que informar 4 e 8 (posição inicial e final, respectivamente) para mostrar na tela somente os valores destacados.


# cont = 0
# x = int(input("Digite o valor do vetor: "))
#
# v1 = [0]*x
# for cont in range (0, len(v1)):
#     v1 [cont] = int(input("Digite valores dentro do vetor: "))
# cont = cont + 1
# print(v1)

# cont = 0
# v1 = int(input("Digite o valor de seu vetor: "))
#
# while (cont < len(v1)):
#     print(vetor [cont])
#     cont = cont + 1
# print(vetor)

"#################################################"

cont = 0
x = int(input("Digite o valor do vetor: "))

v1 = [0]*x
for cont in range (0, len(v1)):
    v1 [cont] = int(input("Digite valores dentro do vetor: "))
cont = cont + 1
# print(v1)

# soma = 0
#
# y = int(input("Digite o valor inicial: "))
# z = int(input("Digite o valor final: "))
#
# for cont in range (y, z + 1):
#     soma = soma + v1 [cont]
# print("Soma: ", soma)


# y = int(input("Digite o valor inicial: "))
# # z = int(input("Digite o valor final: "))
# maior = 0
# menor = 0


# maior = v1[0]
# menor = v1[0]
# pos = 0
# posinc = pos
# posifinal = pos
# for cont in range (0, len(v1)):
#     #if (cont == 0):
#        # maior = v1[cont]
#        # menor = v1[cont]
#     if(maior < v1[cont]):
#         maior = v1[cont]
#         posinc = pos
#
#     elif(menor > v1[cont]):
#         menor = v1[cont]
#         posifinal = pos
#     pos = pos + 1
#
# print("Maior: ", maior, "na posição ", posinc)
# print("Menor: ", menor, "na posição ", posifinal)

# cont = 0
# par = 0
# impar = 0
# for cont in range (0, len(v1)):
#     if (v1 [cont] %2 == 0):
#         cont += 1
#         par = par + 1
#     else:
#         cont += 1
#         impar = impar + 1
# print("Números pares: ", par)
# print("Números ímpares: ", impar)

# x = int(input("Digite o valor do vetor: "))
# v1 = [0]*x
# cont = 0
# for cont in range (0, len (v1)):
#     v1 [cont] = int(input("Digite um número: "))
#     print(v1 [cont] * 2)
#     cont = cont + 1



cont = 0
v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for cont in range (0, len(v1)):
#     print(v1 [cont]* 2)

for cont in range (0, len (v1)):
    for x in range (0, len (v1)):
        print("") 
