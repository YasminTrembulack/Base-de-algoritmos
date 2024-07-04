



import os
os.system("cls")
def calcPesoIdeal(sexo, altura):
    if sexo.lower() == 'm':
        return (72.7 * altura) - 58
    elif sexo.lower() == 'f':
        return (62.1 * altura) - 44.7
    else:
        print("\nErro! Sexo não reconhecido pelo sistema.")
        return 0


sexo = input("\nInforme seu sexo((M) Masculino e (F) Feminino):")
print("_________________________________________________\n")
try:
    altura = float(input("Informe sua altura: "))
    print("_________________________________________________\n")
except:
    print("\nErro! Altura inválida.\n")
    os.system("pause")
    exit()

pesoIdeal = calcPesoIdeal(sexo, altura)
if pesoIdeal:
    print(f"Seu peso ideal é: {pesoIdeal:,.2f}\n")
os.system("pause")