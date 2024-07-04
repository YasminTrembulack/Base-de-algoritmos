import os
m1 = input("Qual a matricula da 1 pessoa:")
idade1 = int(input("Qual a idade:"))

m2 = input("\nQual a matricula da 2 pessoa:")
idade2 = int(input("Qual a idade:"))

os.system('cls')
if idade1 > idade2: print(f"A pessoa 1 é a mais velha. Idade: {idade1}")
else: print(f"A pessoa 2 é a mais velha. Idade: {idade2}")