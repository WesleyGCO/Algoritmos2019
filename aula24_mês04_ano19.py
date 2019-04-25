import random


# aleatorio = random.uniform(15, 25) #[0 ~ 10]
# print("Aleatório: ", aleatorio)


#x = 0
# while (x <= 10):
#     aleatorio = random.randint(0, 10)
#     x = x + 1
#     print("Aleatório: ", aleatorio)


# while (x < 11):
#     aleatorio = random.randint(0, 10)
#     if (aleatorio %2 == 0):
#         print(aleatorio)
#
#         x = x + 1


# x = 0
# soma = 0
#
#
# while (x < 11):
#     aleatorio = random.randint(0, 10)
#     soma = soma + aleatorio
#     print(aleatorio)
#     if (x == 10):
#         print("Soma: ", soma)
#     x = x + 1
#----------------------------------------
# a = 0
# soma = 0
# while (a < 10):
#     b = random.randint(0, 10)
#     soma = soma + b
#     a = a + 1
# print(soma)


# a = 1
# mult = 1
# while (a <= 10):
#     b = random.randint(0, 10)
#     mult = mult * b
#     a = a + 1
#     print(b)
# print("Multiplicação: " , mult)


a = 0
par = 0
while (a < 10):
    b = random.randint(0, 10)
    print(b)
    if (b %2 == 0):
        par = par + 1
    a = a + 1
print("Quantidade de números pares: ", par)
