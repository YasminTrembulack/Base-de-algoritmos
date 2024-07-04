

import os
def calcula( num1, num2):
    global soma, mult
    soma = num1 + num2
    mult = num1 * num2

    if soma % 2 == 0:
        return "P"
    else:
        return "I"

soma = 0
mult = 0

os.system("cls")
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resp = calcula(num1, num2)

    print(f"\nA soma dos 2 números informados é = {soma}")
    print(f"\nA multipicação dos 2 números informados é = {mult}")
    print(f"\n{resp}\n")
except:
    print("\nErro! Número 1 ou 2 invalído.\n")

os.system("pause")