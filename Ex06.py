salario = float(input("Digite o salário: "))

resp1 = (salario*0.15) + salario
resp2 = resp1 - (salario*0.08) 

print(f"O SALÁRIO INICIAL É: R${salario:,.2f}.\nO SALÁRIO COM AUMENTO É: R${resp1:,.2f}.\nE O SALÁRIO FINAL COM DESCONTO É: R${resp2:,.2f}.\n")