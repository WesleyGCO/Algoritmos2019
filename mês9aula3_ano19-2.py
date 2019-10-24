
#Exercício 1


def escrever_nome(nomeArquivo):
    arquivo = open(nomeArquivo, "a")
    arquivo.write(input("Digite um nome: ") + "\n")
    arquivo.close()

# ===============================================

#Exercício 2


def ler_arquivo(arq):
    arquivo = open(arq, "r")
    conteudo = arquivo.readlines()

    arquivo.close()
    for lin in range(0, len(conteudo)):
        print(conteudo[lin], end="")

# ===============================================

#Exercício 3


def dados(x):
    y = open(x, "a")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    salario = input("Digite seu salário: ")

    y.write(nome + "||" + email + "||" + salario + "\n")

    y.close()

# ===============================================

#Exercício 4


def ler_dados(x):
    y = open(x, "r")
    conteudo = y.readlines()
    y.close()

    for t in range(0, len(conteudo)):
        d1 = conteudo[t].split("||")

        print("Nome: ", d1[0], "\n")
        print("Email: ", d1[1], "\n")
        print("Salário: ", d1[2], "\n")

# ===============================================

#Exercício 5 (A)

def ler_num(x):
    y = open(x, "r")
    conteudo = y.readlines()
    y.close()
    maior = float(conteudo[0])

    for t in range(0, len(conteudo)):
        if (maior < float(conteudo[t])):
            maior = float(conteudo[t])
    print("Maior: ", maior)

#Exercício 5 (B)

def num_maior(x):
    y = open(x, "r")
    conteudo = y.readlines()
    y.close()
    maiores = 0

    for i in range(0, len(conteudo)):
        if (float(conteudo[i]) > 0.05):
            maiores = maiores + 1
    print("Maiores que 0.05: ", maiores)

#Exercício 5 (C)

def quant_num(x):
    y = open(x, "r")
    conteudo = y.readlines()
    y.close()

    print("Quantidade de números: ", len(conteudo))

# ===============================================

#Exercício 6 (A)


def ler_num2(x):
    y = open(x, "r")
    conteudo = y.readlines()
    y.close()
    
    maior = float(conteudo[0])

    for i in range()
        
