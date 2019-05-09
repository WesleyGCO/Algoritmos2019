# Apresente na tela os números de 1 a 100.

# cont = 1
#
# while (cont <=100):
#     print("Valor de cont ", cont)
#     cont = cont + 1

#Faça a soma dos números de 1 a 100 e apresente somente o resultado.

# cont = 1
# soma = 0
#
# while (cont <= 100 ):
#     soma = soma + cont
#     cont = cont + 1
# print("Soma dos todos os números de 1 ao 100: ", soma,)


# Apresente na tela somente os números pares entre 1 e 100

# cont = 1
#
# while (cont <= 100):
#     if (cont %2 == 0):
#         print("Números pares: ", cont,)
#     cont = cont + 1

#Apresente na tela somente a soma dos números pares entre 1 e 100

# cont =  1
# soma = 0
# while (cont <=100):
#     if (cont %2 == 0):
#         soma = soma + cont
#         print("Soma números pares: ", soma,)
#     cont = cont + 1


#Apresente na tela os números de X a Y (peça para o usuário informar os valores de X e de Y)

# cont=0
# num1=int(input("Informe o valor de X: "))
# num2=int(input("Informe o valor de Y: "))
# while(cont<=0):
#     print(num1)
#     num1=num1+1
#     if(num1==num2+1):
#         break

# Faça a soma dos números de X a Y e apresente somente o resultado (peça para o usuário informar os valores de X e de Y)

# num1=int(input("Informe o valor de X: "))
# num2=int(input("Informe o valor de Y: "))
# soma=0
# num3=num1
# cont= 1
#
# while (cont==0):
#     num1=num1+soma
#     soma=num3+1
#     num3=num3+1
#     num2=num2-1
#     if(num1==num2):
#         break
# print(num1)

#Apresente na tela somente os números ímpares entre X e Y (peça para o usuário informar os valores de X e de Y

# x = int(input("Informe o valor de x: "))
# y = int(input("Informe o valor de y: "))
#
# while (True):
#     x = x + 1
#     impar = x %2
#     if (impar != 0):
#         print("Ímpar: ", x,)
#     if (x == y):
#         break

#do 1 ao 10 para um número informado pelo usuário.

# num1 = int(input("Digite o valor da tabuada a ser calculada (1 ao 10): "))
# tabuada = 0
# while (True):
#     print(num1 * tabuada)
#     tabuada = tabuada + 1
#
#     if (tabuada == 11):
#         break

# do X ao Y para um número informado pelo usuário (o usuário também deve informar os valores de X e Y)

# x = int(input("Digite o valor a ser calculado: "))
# y = int(input("Digite até que valor a tabuada deve calcular: "))
# tabuada = 0
# while (True):
#     print(x * tabuada)
#     tabuada = tabuada + 1
#     if (tabuada == y +1):
#         break

#Faça um programa que peça um número para o usuário e apresente na tela seu fatorial.

# num1 = int(input("Digite o valor a ser faturado: "))
# fat = 1
# num2 = num1
# while (True):
#     num1 = num1 * (num2 - 1)
#     num2 = num2 - 1
#     if (num2 == 1):
#         break
# print(num1)

# print("""
#
# ================ Menu Principal ================
#
# 1. Par ou Ímpar?
# 2. Potência Xy
# 3. Raiz quadrada
# 4. Sair
#
# """)
# opcao = int(input("Digite sua opção: "))
#
# while (True):
#     if (opcao == 1):
#         x = int(input("Digite um número: "))
#         if (x %2 == 0):
#             print("Par")
#         else:
#             print("Ímpar")
#             break
#     elif (opcao == 2):
#         num1 = int(input("Digite um número: "))
#         num2 = int(input("Digite a potência: "))
#         print("Resultado: ", num1 ** num2,)
#         break
#     elif (opcao == 3):
#         num3 = int(input("Digite um número: "))
#         print("Resultado: ", num3 ** (1/2),)
#         break
#     elif(opcao == 4):
#         print("Você escolheu a opção 4 (sair), até a próxima!")
#         break
#     else:
#         print("Opção inválida!")


# print("""
#
# ================ Menu Principal ================
#
# 1. Fazer tabuada do 1 ao 10 para um número X
# 2. Apresentar os múltiplos de X entre 1 e 100
# 3. Apresentar a soma dos números de 1 a 100
# 4. Sair do programa
#
# """)
# opcao = int(input("Digite sua opção: "))
#
# while (True):
#     if (opcao == 1):
#         num1 = int(input("Digite o valor da tabuada a ser calculada (1 ao 10): "))
#         tabuada = 0
#         while (True):
#             print(num1 * tabuada)
#             tabuada = tabuada + 1
#             if (tabuada == 11):
#                 break
#     elif (opcao == 2):
#         x = int(input("Digite um valor: "))
#         num2 = 1
#         while (num2 <=100):
#             if (num2 % x == 0):
#                 print("O ", num2, "é múltiplo de ", x,)
#             num2 = num2 + 1
#     elif (opcao == 3):
#         cont = 0
#         soma = 0
#         num = 0
#         while (cont <= 100):
#             num = num + 1
#             soma = soma + num
#             cont = cont + 1
#             print("Soma dos todos os números de 1 ao 100: ", soma,)
#     elif (opcao == 4):
#         print("Opção sair! Até a próxima!")
#         break


#6

# cont = 1
# soma = 0
#
# while (True):
#     produto = float(input("Produto {}: R$ ". format(cont)))
#     soma = soma + produto
#
#     if (produto == 0):
#         break
#
# print("Total: R$ ", soma,)
# dinheiro = float(input("Dinheiro: R$ "))
# print("Troco: R$ ", dinheiro - soma, )

# i = 0
# soma = 0
# while (True):
#     temperatura = float(input("Temperatura: "))
#     soma = soma + temperatura
#
#     i = i + 1
#
#     if (i == 7):
#         break
# media = soma / i
#
# print("Média das temperaturas: ", media,)

# i = 0
# soma = 0
# 
# while (True):
#     nota = float(input("Nota: "))
#     soma = soma + nota
# 
#     i = i + 1
# 
#     if (nota == -1):
#         break
# 
# media = soma / i
# print("Média: ", media,)

# i = 0
# soma = 0 
# 
# while (True):
#     cd = int(input("Informe o número de CD's: "))
