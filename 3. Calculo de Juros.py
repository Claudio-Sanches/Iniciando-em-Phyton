# Descrição   : Calculo de Juros
# Autor(a)    : Claudio Buzzolini Sanches
# Data atual  : 05/02/2021

print("Calcula juros compostos sobre um valor de principal")
print("")
Valor=float(input("Valor Principal: "))
Taxa=float(input("Taxa % Mensal: "))
Periodo=int(input("Quantidade de meses: "))
print("")

Vpagar=Valor
i=1
for i in range(Periodo):
    Vpagar=Vpagar+Vpagar*(Taxa/100)
    print(f'  {i+1} {Vpagar:.2f}')

print("")
print("-----------------------")
print(f'Valor a pagar com juros de {(Taxa):.2f}% será de {Vpagar:.2f} após {Periodo} meses')

print("")
print("Tecle enter para fechar")
input()
