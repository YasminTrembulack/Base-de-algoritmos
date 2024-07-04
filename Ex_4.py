i = 0
soma_mulher = 0; soma_turma = 0

genero = []
#----------------------------------------
maior_altura = 0; menor_altura = 999; 
media_alturaM = 0; media_alturaTurma = 0

altura = []
#----------------------------------------

print("\n\n======================================")
print("\n\n          Análise de fichas      ")
print("\n\n======================================")

for i in range(4):
    print("\n\n======================================")
    print(f"{i+1} - Qual seu gênero (1 - Masculino / 2 - Feminino): ")
    genero.append(input("\n > "))

    print(f"\n\n{i+1} - Insira sua altura")
    altura_pessoa = float(input("\n > "))

    altura.append(altura_pessoa)

    soma_turma += altura_pessoa

for gen in genero:
    if gen == '2':
        soma_mulher += 1

media_alturaM = soma_mulher/4


for alt in altura:
    if alt > maior_altura:
        maior_altura = alt


for alt in altura:
    if alt < menor_altura:
        menor_altura = alt

media_alturaTurma = soma_turma/4

#--------------------------------------------------------------------

print("\n\n======================================")
print("\n\n             Resultados      ")
print("\n\n======================================")

print(f"\n A média de altura das mulheres é de: {media_alturaM:.2f}")
print(f"\n A maior altura da turma é: {maior_altura:.2f}")
print(f"\n A menor altura da turma é: {menor_altura:.2f}")
print(f"\n  A média de altura da turma é: {media_alturaTurma:.2f}")