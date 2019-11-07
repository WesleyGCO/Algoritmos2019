#--------------- Estrutura de dados heterogênea ------------------------------------

# Em uma estrutura de dados heterogênea existem campos (atributos) e não índices;

# Há registros (conteúdo de dados) - Class;

# Nome ---> Atributos ---> *Métodos*;

# O que é? é uma estrutura de dados que pode ter vários valores diferentes,
# não sendo necessariamente do mesmo tipo (integer, float, etc);

# Class é um projeto que constituem em atributos e métodos;

# -----------------------------------------------------------------------------------
import funcoes

from Aluno import Aluno

from Data import Data

# -----------------------------------------------------------------------------------

alu1 = Aluno()

funcoes.exibirAluno(alu1)

alu1.nome = "Flávio"
alu1.idade = 19
alu1.status = True
alu1.dtNasc.dia = 6
alu1.dtNasc.mes = 6
alu1.dtNasc.ano = 2000
alu1.dtNasc.hor.horas = 19
alu1.dtNasc.hor.minutos = 20
alu1.dtNasc.hor.segundos = 00

funcoes.exibirAluno(alu1)

# -----------------------------------------------------------------------------------

# dtNasc = Data()
# funcoes.informeData(dtNasc)

# -----------------------------------------------------------------------------------
