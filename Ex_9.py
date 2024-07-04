idade = 0

cont_total = 0
cont_IA = 0
cont_IB = 0
contJA = 0
contJB = 0
contADUL = 0

idade = int(input("\n Qual a idade do nadador? Ou digite 0 para sair \n > "))

while idade > 0:
    if idade >- 18:
        contADUL += 1
        cont_total += 1
    
    elif idade >= 5 and idade <= 7:
        cont_IA += 1
        cont_total += 1
        print("Infantil A \n")
    
    elif idade >= 8 and idade <= 10:
        cont_IB += 1
        cont_total += 1
        print("Infantil B \n")

    elif idade>=11 and idade<=13:
        contJA += 1
        cont_total += 1
        print("Juvenil A \n")

    elif(idade>=14 and idade<=17):
        contJB += 1
        cont_total += 1
        print("Juvenil B \n")

    idade = int(input("\n Qual a idade do nadador? Ou digite 0 para sair \n > "))

print(f" Categoria infantil A sao: {cont_IA} \n")
print(f" Categoria infantil B sao: {cont_IB} \n")
print(f" Categoria juvenil A sao: {contJA} \n")
print(f" Categoria juvenil B sao: {contJB} \n")
print(f" Categoria Adultos sao: {contADUL} \n")

print(f"Total: {cont_total} \n")