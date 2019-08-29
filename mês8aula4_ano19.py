# def acao(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# acao(4, 5, 26)

#------------------------------------------------------


# idade = 20
#
# def exibirIdade(idade):
#     print(idade)
#
# exibirIdade(25)

#------------------------------------------------------


# def exibirMensagem(a):
#     for i in range(a):
#         print("Olá Pessoal!")
#
# exibirMensagem(4)

#------------------------------------------------------


# def exibirNumero(a):
#     for i in range(a):
#         x = int(input("Digite um número: "))
#         if (x %2 == 0):
#             print(x, "é par!")
#         else:
#             print(x, "é ímpar!")
#
# exibirNumero(5)

#------------------------------------------------------


# def exibirMenu():
#     print("""
#     MENU DE OPÇÕES
#     1. Somar dois números
#     2. Subtrair dois números
#     3. Dividir dois números
#     4. Multiplicar dois números
#     5. Sair
#     """)

# def somar():
#     x = int(input("Digite um número: "))
#     y = int(input("Digite um número: "))
#     print("Soma: ", x + y)
#
# def subtrair():
#     x = int(input("Digite um número: "))
#     y = int(input("Digite um número: "))
#     print("Subtração: ", x - y)
#
# def dividr():
#     x = int(input("Digite um número: "))
#     y = int(input("Digite um número: "))
#     print("Divisão: ", x / y)
#
# def multiplicar():
#     x = int(input("Digite um número: "))
#     y = int(input("Digite um número: "))
#     print("Multiplicação: ", x * y)
#
#
# while (True):
#     exibirMenu()
#     opcao = int(input("Digite a opção desejada: "))
#
#     if (opcao == 1):
#         somar()
#     elif (opcao == 2):
#         subtrair()
#     elif (opcao == 3):
#         dividr()
#     elif (opcao == 4):
#         multiplicar()
#     elif (opcao == 5):
#         print("Você optou por sair do programa. Até mais a próxima")
#     else:
#         print("Opção inválida")
#
# # ------------------------------------------------------

# def fatorial(n):
#     fat = 1
#     i = 1
#     while(i <= n):
#         fat = fat * i
#         i = i + 1
#     print("Fatorial: ", fat)
#
# n = int(input("Número: "))
# fatorial(n)

##----------------------------------------------------------


# import random
#
# def exibirDados(vetorNotas, vetorMedia, nomeDisciplina):
#     print("\n\nNotas da disciplina de", nomeDisciplina)
#     print(    "Aluno    ", end="")
#     for cont in range(0, len(vetorNotas[0])):
#         print("Nota ", cont, "\t", end="")
#     print("Media")
#
#     for i in range(0, len(vetorNotas)):
#         print("Aluno: ", i, "\t", end="")
#         for j in range(0, len(vetorNotas[i])):
#             print(vetorNotas[i][j], "\t", end="")
#         print("{0:7.2f}".format(vetorMedia[i]))
#
# def turma(qtd_alunos, qtd_notas, nomedisc):
#     vetorNotas = []
#     for cont in range(0, qtd_alunos):
#         vetorNotas.append([0]*qtd_notas)
#
#     print("Notas ", vetorNotas)
#
#     """solicitar todas as notas por aluno"""
#     for cont in range(0, len(vetorNotas)):
#         print("Para o aluno {}:".format(cont))
#         for i in range(0, len(vetorNotas[cont])):
#             """vetorNotas[cont][i] = float(input("Informe a nota do {} bimestre: ".format(i)))"""
#             vetorNotas[cont][i] = random.randint(0, 10)
#
#     """calcular a media aritmetica"""
#     """como cada aluno tem N notas, vamos criar um vetor das medias"""
#     vetorMedias = [0]*qtd_alunos
#
#     for cont in range(0, qtd_alunos):
#         soma = 0
#         for j in range(0, len(vetorNotas[cont])):
#             soma = soma + vetorNotas[cont][j]
#         vetorMedias[cont] = soma / qtd_notas
#
#
#     """chamar o procedimento para exibir tudo"""
#     exibirDados(vetorNotas, vetorMedias, nomedisc)
#
# totalalunos = int(input("Digite o total de alunos: "))
# totalNotas = int(input("Digite o total de notas: "))
# disciplina = (input("Digite a disciplina: "))
#
# turma(totalalunos, totalNotas, disciplina)
