
import os

maior = 0.0
menor = 0.0

total_altura_M = 0.0
media_altura_M = 0.0
qtd_M = 0

total_altura_H = 0.0
media_altura_H = 0.0
qtd_H = 0

for i in range(4):
    os.system('cls')
    print(i)
    gen = int(input("Digite o genero\n0 - Feminino \n1 - Masculino\n> "))
    alt = float(input("Informe a Altura\n"))
    if i == 0:
        menor = alt
        maior = alt
    
    if not gen: qtd_M += 1; total_altura_M += alt
    if gen == 1: qtd_H += 1; total_altura_H += alt
    
    if alt > maior: maior = alt
    elif alt < menor: menor = alt


os.system('cls')
if not qtd_M: print("Nenhuma mulher inserida.\n\n")
else: 
    media_altura_M = total_altura_M/qtd_M
    print(f"Media -> Mulheres: {media_altura_M}")
    print(f"Foram inseridas {qtd_M} mulheres.\n\n")

if not qtd_H: print("Nenhum homem inserido.\n\n")
else: 
    media_altura_H = total_altura_H/qtd_H
    print(f"Media -> Homens: {media_altura_H}")
    print(f"Foram inseridos {qtd_H} homens.\n\n")

print(f"Menor Altura: {menor}\nMaior Altura {maior}")

    