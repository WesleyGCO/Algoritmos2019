"""

ARQUIVOS: conjunto de dados armazenados em disco.
Ações:
- Abrir arquivo
    open("nomearquivo.txt", modoAbertura)
        modos:  "r" - read (apenas lê dados do arquivo)
                "w" - write (sempre "cria" um arquivo novo. Se já existir, ele é "zerado")
                "a" - append (escreve no final de arquivo já existente)
- Fechar arquivo
- Gravar dados no arquivo
"""

# arquivo = open("nomes.txt", "w")
# nome = input("Digite o nome: ")
# arquivo.write(nome)
# arquivo.write("\n")
# arquivo.close()

# ==============================================

import arquivo


#Exercício 1
# arquivo.escrever_nome("nomes1.txt")

#Exercício 2
# arquivo.ler_arquivo("nomes1.txt")

#Exercício 3
# arquivo.dados("dados4.txt")

#Exercício 4
#arquivo.ler_dados("dados4.txt")

#Exercício 5 (A)
# arquivo.ler_num("num.txt")
#Exercício 5 (B)
# arquivo.num_maior("num.txt")
#Exercício 5 (C)
# arquivo.quant_num("num.txt")

#Exercício 6
arquivo.ler_num2("num2.txt")
