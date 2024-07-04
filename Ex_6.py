sx = 0
homens = 0
mulheres = 0.00

alt = 0; maior = 0; menor = 0

i = 1
media_mulher = 0.00; alt_mulheres = 0.00

for i in range(5):
    sx = int(input("\n\nDigite o genero\n (0) Feminino \n (1) Masculino \n > "))

    alt = float(input("\nInforme a altura \n > "))

    if i == 1:
        maior = alt
        menor = alt
    
    if alt > maior: maior = alt
    if alt < menor: menor = alt
    
    if not sx:
        alt_mulheres += alt
        mulheres += 1
    
    else: homens += 1

if mulheres:
    media_mulher = alt_mulheres / mulheres
    print(f"\nMedia de altura das mulheres: {media_mulher}")

else: print("\nNenhuma mulher inserida.")

print(f"\n Quantidade de homens: {homens}")
print(f"\n Menor altura: {menor} \n Maior altura: {maior}")