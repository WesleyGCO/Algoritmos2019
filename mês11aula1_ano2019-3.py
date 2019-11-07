def exibirAluno(a):
    print("Nome: ", a.nome)
    print("Idade: ", a.idade)

    if (a.status == True):
        print("Status: Regular")
    else:
        print("Status: Não matriculado")
    print("Data de nascimento: {}/{}/{}".format(a.dtNasc.dia, a.dtNasc.mes, a.dtNasc.ano))
    print("Horario de aula: {}hrs {}min {}seg".format(a.dtNasc.hor.horas, a.dtNasc.hor.minutos, a.dtNasc.hor.segundos))

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

def informeData(a):
    a.dia = int(input("Digite o dia do seu aniversário: "))
    a.mes = int(input("Digite agora o mês: "))
    a.ano = int(input("Por último, digite o ano: "))

    # print("Sua data de nascimento é: ", a.dia, "/", a.mes, "/", a.ano)
    print(" {}/{}/{} ".format(a.dia, a.mes, a.ano))
