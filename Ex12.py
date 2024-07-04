import os

qtd = int(input("De quantas pessoas deseja informar o salário: "))
tota_salario = 0.0

for i in range(qtd):
    salario = float(input("Qual é o salário: "))
    tota_salario += salario
    
os.system('cls')
print(f"Total dos salarios: R${tota_salario:,.2f}")
print(f"Media dos salarios: R${format(tota_salario/qtd, ".2f")}")