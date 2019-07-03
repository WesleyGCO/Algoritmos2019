# matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


# for lin in range (0, len(matriz)):
#
#     for col in range (0, len(matriz [lin])):
#
#         print(matriz[lin][col])

# --------------------------------

#usuário digita valores da linhda, coluna e o número que será guardado

# lin = int(input("Digite o valor da linha: "))
# col = int(input("Digite o valor da coluna: "))

# matriz [lin] [col] = int(input("Digite o valor a ser guardado: "))

# for lin in range (0, len(matriz)):

#     for col in range (0, len(matriz [lin])):
#
#         print(matriz[lin][col])

# print(matriz)

# --------------------------------

# mostrar um número específico
# print(matriz [2][1])

# --------------------------------

# mostrar uma linha específica
# for col in range (0, len(matriz[2])):
#     print(matriz[2][col])

# --------------------------------

# mostrar uma coluna específica
# for lin in range (0, len(matriz)):
#     print(matriz[lin][2])


# --------------------------------
#Criação de matriz do zero

matriz = []

for linhas in range (0, 3):
    matriz.append([0] * 3)

print(matriz)

for lin in range (0, len(matriz)):
    for col in range (0, len(matriz[lin])):
        matriz [lin][col] = int(input("Insira o valor na linha {} e coluna {}: ".format(lin,col)))
print("", matriz[0], '\n', matriz[1], '\n', matriz[2])
