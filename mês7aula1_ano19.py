# Ordenação Bolha

# vetor = [10, 20, 8, 30, 7, 4, 0, 25, 20]
#
# print("Valor original: ", vetor)
#
#
# #Contar as interações/passos
#
# for x in range(0, len(vetor) - 1):
#     # Fazer as verificações um a um no vetor inteiro
#     for y in range(0, len(vetor) - 1):
#
#         if (vetor[y] > vetor[y + 1]):
#             aux = vetor[y]
#             vetor[y] = vetor[y + 1]
#             vetor[y + 1] = aux
#         #     print("Trocou")
#         #
#         # else:
#         #     print("Não trocou")
#
# print("Vetor ordenado: ", vetor)



# Ordenação Inserção

# vetor = [10, 8, 1, 7, 12]
#
#
# print("Vetor original:", vetor)
# print("Tamanho do vetor:", len(vetor))
# print(" ")
#
# # Contar as interações/passos
# for x in range(0, len(vetor)):
#     # Fazer as verificações a partir da posição x+1 porque o x já vai estar no for anterior
#     for y in range(x+1, len(vetor)):
#
#         print("Comparando {}(Pos: {}) com {}(Pos: {}).".format(vetor[x], x, vetor[y], y))
#
#         if(vetor[x] > vetor[y]):
#             aux = vetor[x]
#             vetor[x] = vetor[y]
#             vetor[y] = aux
#             print("Trocou")
#         else:
#             print("Não trocou")
#
#         print("Vetor:", vetor)
#         # Se não quiser que o algoritmo fique parando, comente a linha abaixo
        # input("Aperte ENTER para continuar...\n")
#
# print("Vetor ordenado:", vetor)


# Ordenação Seleção

vetor = [10, 1, 5, 4, 2, 9]


print("Vetor original:", vetor)
print("Tamanho do vetor:", len(vetor))
print(" ")

# Contar as iterações/passos
for x in range(0, len(vetor)-1):
    menor = x
    # Fazer as verificações no vetor
    for y in range(x+1, len(vetor)):

        print("Comparando {}(Pos: {}) com {}(Pos: {}).".format(vetor[x], x, vetor[y], y))

        if(vetor[menor] > vetor[y]):
            menor = y
            print("Achou menor")
        else:
            print("Não é menor")

    # Depois de comparar todos da posição "y", faz a troca se o valor da variável "menor" foi alterado
    if (menor != x):
        aux = vetor[x]
        vetor[x] = vetor[menor]
        vetor[menor] = aux
        print("\nFez a troca...")

    print("\nVetor:", vetor)
    # Se não quiser que o algoritmo fique parando, comente a linha abaixo
    input("Aperte ENTER para continuar...\n")

print("Vetor ordenado:", vetor)
