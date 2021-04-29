# Descrição   : Cadastro de usuários
# Autor(a)    : Claudio Buzzolini Sanches
# Data atual  : 26/02/2021

def Buscar(Nome):
    """
   ===> Pesquisa no vetor o Nome informado
   :param Nome: O nome a ser procurado
   :return: Se encontrado na matriz informa o Nome, sua posição e idade ou caso não encontado também informa. 
   """
    Retorno = f'-1 O nome {Procura} não está cadastrado'
    for i in range(5):
        if Dados[i][0] == Procura:
            Retorno = f'O nome {Procura} está na posição {i + 1} e sua idade é {Dados[i][1]}'
    return Retorno


def Apaga(Nome):
    Retorno = f'\n ==== O nome {Procura} não está cadastrado ==== '
    for i in range(5):
        if Dados[i][0] == Nome:
            print(f'\nO nome {Procura} está na posição {i + 1} e sua idade é {Dados[i][1]}\n')
            print(' ESSE USUÁRIO SERÁ APAGADO \n')
            print('Está certo que deseja APAGAR esse USUÁRIO (S)/(N): ')
            Confirma = str(input("Digite aqui => "))
            if Confirma == "S":
                Dados[i][0] = " "
                Dados[i][1] = " "
                Retorno = f'\nO nome {Procura} foi apagado com sucesso'
            else:
                Retorno = f'\nO nome {Procura} NÃO FOI APAGADO'
    return Retorno


Dados = []
i = 0
for i in range(5):
    Dados.append([" "] * 2)
i = 0
Achei = 0
Repete = "N"

while Repete == "N":
    print("Digite a opção desejada:")
    print(" ")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários cadastrados")
    print("3 - Buscar por Nome")
    print("4 - Buscar por nome para apagar")
    print("5 - Sair do sistema")
    print(" ")
    Opcao = float(input("Digite a Opção: "))
    if Opcao == 1:
        print("\n === Cadastro para 5 usuários === ")
        print(" ")
        for i in range(5):
            if Dados[i][0] == " ":
                print("Informações do Usuário", i + 1)
                Dados[i][0] = input("Digite o Nome: ")
                Dados[i][1] = input("Digite a Idade: ")
                print(" ")
                Achei = Achei + 1
    if Opcao == 2:
        print("\n === Relação de usuários Cadastrados ===")
        print(" ")
        for i in range(5):
            print("Cadastro ", i + 1, " === ", Dados[i][0], " com ", Dados[i][1], " anos.")
        input("\nPara Continuar <ENTER>")
    if Opcao == 3:
        print("\n === Opção Localizar Usuário === \n")
        Procura = input("Digite o nome: ")
        print(" ")
        print(f'{Buscar(Procura)}')
        input("\nPara Continuar <ENTER>")
    if Opcao == 4:
        Achou = 0
        print("\n === Opção APAGAR Usuário === \n")
        Procura = input("Digite o nome: ")
        print(Apaga(Procura))
        input("\nPara Continuar <ENTER>")
    if Opcao == 5:
        Repete = "S"
