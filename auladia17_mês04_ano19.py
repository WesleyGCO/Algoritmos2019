# Comando de repetição - while (condição):
# while ( True ):
#
#      Tudo que vai ser repetido ENQUANTO (while) a condição for verdadeira
#     x1 = int(input("Informe um número: "))

#variável de controle/contagem de repetição do while

# cont = 1
#
# while ( cont < 6 ):
#     x1 = int(input("Informe um número: "))
#     cont = cont + 1
# import time

# cont = 1
#
# while ( cont <= 100000 ):
#     # time.sleep(1)
#     print("Valor de cont: ", cont)
#     cont = cont + 1

# cont = 5
#
# while (cont > 0):
#     print("Valor de cont: ", cont,)
#     cont = cont - 1
#
# print("Fora do while!")

cont = 1
soma = 0

while (cont <= 4):
    nota = int(input("Digite sua nota: "))
    soma = soma + nota
    cont = cont + 1
print("Média: ", soma / 4,)
