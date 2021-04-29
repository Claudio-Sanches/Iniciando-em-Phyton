# Descrição   : Armazenamento do cadastro de funcionários em matriz
# Autor(a)    : Claudio Buzzolini Sanches
# Data atual  : 05/02/2021

print("Infome dados na ordem abaixo dos 5 Funcionário a serem cadastrados: ")
print("")
print("Nome")
print("Função")
print("Idade")
print("Sexo")
print("Salario")
FUNCIONARIO=[]
for i in range(5):
    print("")
    print("Dados do Funcionario ",i+1)
    FUNCIONARIO.append([0]*5)
    for j in range(5):
        FUNCIONARIO[i][j]=input()
print("Término da entrada de dados")
print("---------------------------")
print(" ")
print("Leitura da matriz e apresentação dos dados")
print(" ")
print("   Nome   --   Função  -- Idade -- Sexo -- Salário --")
for I in range(5):
       print(f'{FUNCIONARIO[I][0]:{10}} -- {FUNCIONARIO[I][1]:{13}} -- {FUNCIONARIO[I][2]:{2}} -- {FUNCIONARIO[I][3]:{2}} -- {FUNCIONARIO[I][4]:{4}} -- ')
print(" ")
print("digite enter para finaliza")
input()
