import os, time

categorias = {
    "Infantil A": 0, "Infantil B": 0, "Juvenil A": 0,
    "Juvenil B": 0, "Adultos": 0
}

idade = 1 
total = 0
while idade > 0:
    os.system('cls')
    print("Digite 0 para sair!")
    idade = int(input("Qual a idade do nadador? \n"))
    os.system('cls')
    if idade > 17:  categorias["Adultos"] += 1;     print("Adulto")
    elif idade > 13:categorias["Juvenil B"] += 1;   print("Juvenil B")
    elif idade > 10:categorias["Juvenil A"] += 1;   print("Juvenil A")
    elif idade > 7: categorias["Infantil B"] += 1;  print("Infantil B")
    elif idade > 4: categorias["Infantil A"] += 1;  print("Infantil A")
    elif idade < 5 and idade != 0: print("Crianças com menos de 5 anos não podem nadar ainda.")
    time.sleep(1.5)
    if idade != 0: total += 1

os.system('cls')
for categoria in categorias:
    print(f"{categoria} : {categorias[categoria]}")
print(f"No total foram adicionados {total} nadadores.")
    
    