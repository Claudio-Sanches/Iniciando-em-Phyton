# Descrição   : Pedido de compras
# Autor(a)    : Claudio Buzzolini Sanches
# Data atual  : 05/02/2021

Total_Pedido=0

print("Calcula o valor total do pedido, somando itens digitados")
print(" ")
print("Digite as informações dos itens a serem comprados:")
print(" ")
while True:
    print("------------------------")
    Produto=input("O nome do produto: ")
    Preco_Unit=float(input("Preço Unitário: "))
    Qtde=float(input("A quantidade de compra: "))
    print("------------------------")
    print(" ")
    Total_Pedido=Total_Pedido+Preco_Unit*Qtde
    Resp=input("Deseja Continuar s/n: ")
    print(" ")
    if Resp == 'n' :
        break

print("-----------------------")
print("Total Pedido : ",Total_Pedido)

print("")
print("Tecle enter para fechar")
input()
