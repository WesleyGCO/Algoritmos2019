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
        print(conteudo[lin], end = "")

# ===============================================

#Exercício 3
def dados(x):
    y = open(x, "a")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    salario = input("Digite seu salário: ")

    # y.write(nome + "\t" + email + "\t" + salario + "\t")
    
    y.close()

# ===============================================

#Exercício 4
def ler_dados(x):
    y = open(x, "r")
    conteudo = y.readlines()
    y.close()

    for lin in range(0, len(conteudo)):
        print("Nome:", conteudo[lin], end = "")
        
