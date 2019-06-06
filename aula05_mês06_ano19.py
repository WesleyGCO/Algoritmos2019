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
cont = 0
x = int(input("Digite o valor do vetor: "))

v1 = [0]*x
for cont in range (0, len(v1)):
    v1 [cont] = int(input("Digite valores dentro do vetor: "))
cont = cont + 1
print(v1)
