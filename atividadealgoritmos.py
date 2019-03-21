print("  ")
print("""\t\t\tCADASTRO DE ALUNOS!


1) Cadastrar
2) Alterar
3) Excluir
4) Consultar
5) Imprimir
""")

num = int(input("Digite o número da opção: "))
print("  ")

if ( num == 1):
    print("Você escolheu a opção Cadastrar!")
elif ( num == 2):
    print("Você escolheu a opção Alterar!")
elif ( num == 3):
    print("Você escolheu a opção Excluir!")
elif ( num == 4):
    print("Você escolheu a opção Consultar!")
elif ( num == 5):
    print("Você escolheu a opção Imprimir!")
else:
    print("Opção inválida!")
