# Descrição   : Aprovação de crédito
# Autor(a)    : Claudio Buzzolini Sanches
# Data atual  : 05/02/2021

print("    === Calculo para aprovação de crédito ===")
print(" ")
Cliente = input("Informe o nome do Cliente: ")
Renda = float(input("Informe a renda do cliente: "))
print("")

if Renda <= 999.99:
    print(f'Sr.(a) {Cliente} não se encaixa na faixa de compras')
elif 1000 <= Renda <= 2999.99:
    print(f'Sr.(a) {Cliente} está na faixa 1 e tem R$ {Renda * 0.3:.2f} de limite aprovado para compras')
elif 3000 <= Renda <= 4999.99:
    print(f'Sr.(a) {Cliente} está na faixa 2 e tem R$ {Renda * 0.35:.2f} de limite aprovado para compras')
elif Renda >= 5000:
    print(f'Sr.(a) {Cliente} deve ser encaminhada a Gerencia de Atendimento, grato')

print("")
print("Tecle enter para fechar")
input()
