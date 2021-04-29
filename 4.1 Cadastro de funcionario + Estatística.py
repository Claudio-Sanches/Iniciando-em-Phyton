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
print(" ")
print("Término da entrada de dados")
print("---------------------------")
print(" ")
print("Leitura da matriz e apresentação dos dados")
print(" ")
print("   Nome   --   Função  -- Idade -- Sexo -- Salário --")
for I in range(5):
       print(f'{FUNCIONARIO[I][0]:{10}} -- {FUNCIONARIO[I][1]:{13}} -- {FUNCIONARIO[I][2]:{2}} -- {FUNCIONARIO[I][3]:{2}} -- {FUNCIONARIO[I][4]:{4}} -- ')
print(" ")
Idade_Maior=FUNCIONARIO[0][2]
Nome_Maior=FUNCIONARIO[0][0]
Idade_Menor=FUNCIONARIO[0][2]
Nome_Menor=FUNCIONARIO[0][0]
Total_Sal=Cont_F=Cont_M=0

for I in range(5):
    if Idade_Maior < FUNCIONARIO[I][2]:
        Idade_Maior=FUNCIONARIO[I][2]
        Nome_Maior=FUNCIONARIO[I][0]
    if Idade_Menor > FUNCIONARIO[I][2]:
        Idade_Menor=FUNCIONARIO[I][2]
        None_Menor=FUNCIONARIO[I][0]
    if FUNCIONARIO[I][3] == "F":
        Cont_F=Cont_F+1
    else:
        Cont_M=Cont_M+1
    Total_Sal=Total_Sal+int(FUNCIONARIO[I][4])

print(" ")
print("Dados estatisticos da empresa")
print("-----------------------------")
print("Menor Idade: ",Idade_Menor," - ",Nome_Menor)
print("Maior Idade: ",Idade_Maior," - ",Nome_Maior)
print("Sexo Faminino: ",Cont_F)
print("Sexo Masculino: ",Cont_M)
print("Total dos salários: ",Total_Sal)

print(" ")
print("====")
print("digite enter para finaliza")
input()
