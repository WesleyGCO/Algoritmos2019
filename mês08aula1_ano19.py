# def exibirMenu():
#     print('1. inserir')
#     print("2. Alterar")
#     print("3. Excluir")
#     print("4. Sair")
#
# exibirMenu()
#


# def somar():
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite um número: "))
#     print("A soma dos números é ", num1+num2)
#
# somar()


# def multiplicar():
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite um número: "))
#     print("A multiplicação dos números é ", num1*num2)
#
# multiplicar()


# def raiz():
#     num1 = int(input("Digite um número: "))
#     print("A raiz do número é ", num1 ** 1/2)
#
# raiz()


# def potencia():
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite a potência que será elevada: "))
#     print("A raiz do número é ", num1 ** num2)
#
# potencia()


# def tabuada():
#     num = int(input("Digite um número: "))
#     mult = 1
#     while(mult <= 10):
#         x = num * mult
#         print(x)
#         mult = mult + 1
# tabuada()

def menuOpcoes():
    print(''' Menu de Opções
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Raiz quadrada
    5. Tabuada
    6. Sair
    ''')
    opcao = int(input("Digite sua opção: "))
    if (opcao == 1):
        x = int(input("Digite um número: "))
        y = int(input("Digite um número: "))
        print("A soma dos números é", x + y)
    elif (opcao == 2):
        x = int(input("Digite um número: "))
        y = int(input("Digite um número: "))
        print("A subtração dos números é", x - y)
    elif (opcao == 3):
        x = int(input("Digite um número: "))
        y = int(input("Digite um número: "))
        print("A multiplicação dos números é", x * y)
    elif (opcao == 4):
        x = int(input("Digite um número: "))
        print("A raiz quadrada do número escolhido é", x ** 1/2)
    elif (opcao == 5):
        x = int(input("Digite um número: "))
        mult = 1
        while(mult <= 10):
            y = x * mult
            print(y)
            mult = mult + 1
    elif (opcao == 6):
        print("Você escolheu sair do programa")

menuOpcoes()
