#3)

# matriz = [[10, 20, 15], [9, 8, 7], [1, 3, 5]]

# for lin in range (0, len(matriz)):
#     for col in range (0, len(matriz [lin])):
#         print(matriz [lin][col])

#4)

# matriz = []
#
# for linhas in range (0, 4):
#     matriz.append([0] * 4)
#
# for lin in range (0, len(matriz)):
#     for col in range(0, len(matriz[lin])):
#         matriz [lin][col] = int(input("Insira o valor na linha {} e coluna {}: ".format(lin,col)))
#
# print(matriz)

#5)

# matriz = []
#
# a = int(input("Digite a quant de linhas de sua matriz: "))
# b = int(input("Digite a quant de colunas de sua matriz: "))
#
# for linhas in range (a):
#     matriz.append([0]* b)
#
# for lin in range (0, len(matriz)):
#     for col in range(0, len(matriz[lin])):
#         matriz [lin][col] = int(input("Insira o valor na linha {} e coluna {}: ".format(lin,col)))
#
# for lin in range(0, len(matriz)):
#     for col in range(0, len(matriz[lin])):
#         print(matriz[lin][col], "\t", end="")
#     print()

#6)

# matriz = []
#
# soma = 0
# linhas = 3
# colunas = 4
#
# for linhas in range (linhas):
#     matriz.append([0] * colunas)
#
# for lin in range(0, len(matriz)):
#     for col in range (0, len(matriz[lin])):
#         matriz[lin][col] = int(input("Insira o valor na linha {} e coluna {}: ".format(lin,col)))
#         soma = soma + matriz[lin][col]
# print("Soma de todos os números dentro da matriz é ", soma)


#7)

matriz =[]
linhas = 5
colunas = 3
for linhas in range(linhas):
    matriz.append([0] * colunas)

for lin in range (0, len(matriz)):
    for col in range (0, len(matriz[lin])):
        matriz[lin][col] = int(input("Insira o valor na linha {} e coluna {}: ".format(lin,col)))


soma = 0
somacol = 0
somalin = 0
maiorlin = [matriz[0][0]]*5
menorlin = [matriz[0][0]]*5
maiorcol = [matriz[0][0]]*3
menorcol = [matriz[0][0]]*3
menorma = 0
menorma = 0


for lin in range (0, len(matriz)):
    for col in range (0, len(matriz[lin])):
        soma = soma + matriz[lin][col]
        somacol = somacol + matriz[col]
        somalin = somalin + matriz[lin]

        if (maiorlin < matriz[0][col]):
            maiorlin = matriz[0][col]
        if (menorlin > matriz[0][col]):
            menorlin = matriz[0[col]

        # if (maiorcol < matriz[lin][0]):
        #     maiorcol = matriz[lin][0]
        # if (menorcol > matriz[lin][0]):
        #     menorcol = matriz[lin][0]

        # if (maiorma < matriz[lin][col]):
        #     maiorma = matriz[lin][col]
        # if (menorma > matriz[lin][col]):
        #     menorma = matriz[lin][col]


print("A somatória dos valores para cada coluna é ", somalin)
print("A somatória dos valores para cada coluna é ", somacol)
print("A somatória de todos os valores da matriz é ", soma)
print("O maior valor para cada linha é ", maiorlin)
print("O menor valor para cada linha é ", menorlin)
# print("O maior valor para cada coluna é ", maiorcol)
# print("O menor valor para cada coluna é ", menorcol)
print("O maior valor da matriz é ", maiorma)
print("O menor valor da matriz é ", menorma)
print("A média dos valores da matriz é ", soma / len(matriz))
