# AULA DIA 06/11/2019

# Arquivo separado

# Criação da classe Aluno

# class Aluno:
#     nome = ""
#     idade = 0
#     status = False

# -----------------------------------------------------------------------------------

# Juntando as duas classes

from Data import Data

class Aluno:
    # Atributos
    nome = "" # string faz parte
    idade = 0 # int faz parte
    status = False # booleano faz parte

    # Vamos usar um atributo do tipo que nós criamos
    dtNasc = Data() # Data não faz parte

    # Método --> Construtor
    def __init__(self):
        # self busca o que tem dentro dessa classe
        self.dtNasc = Data()
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Arquivo separado

# Criação da classe Data

# class Data:
#     dia = 1
#     mes = 1
#     ano = 0

# -----------------------------------------------------------------------------------

# Juntando as duas classes

from Horario import Horario

class Data:
    dia = 1
    mes = 1
    ano = 0
    hor = Horario()

    def __init__(self):
        self.hor = Horario()
