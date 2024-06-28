id = 1; idade = 0

nota = 0;media = 0; soma_notas = 0

conceito = ''

alunosA = 0; alunosE= 0
alunos = 0

print("Digite sua identificação para informar as notas ou 0 para sair\n\n")
print("Qual seu numero de identificação? ")

id = int(input("\n> "))

while id > 0:

    for i in range(12):
        print(f"\n\nQual sua {i+1}° nota?")
        nota = float(input("\n> "))

        soma_notas += nota

    alunos += 1
    media = soma_notas/ 12

    print(f"ID: {id}")
    print(f"Média: {media}")

    if media >= 90:
        conceito = 'A'
        alunosA += 1
        print(f"Conceito: {conceito}")
    
    
    elif media >= 75 and media < 90:
        conceito = 'B'
        print(f"Conceito: {conceito}")

    elif media >= 60 and media < 75:
        conceito = 'C'
        print(f"Conceito: {conceito}")

    elif media >= 40 and media < 60:
        conceito = 'D'
        print(f"Conceito: {conceito}")
    
    elif media < 40:
        conceito = 'E'
        alunosE += 1
        print(f"Conceito: {conceito}")
    
    print("\n\nDigite sua identificação para informar as notas ou 0 para sair\n\n")
    print("Qual seu numero de identificação? ")

    id = int(input("\n> ")) 

    soma_notas = 0

print(f"{alunos} alunos calculados\n")
print(f"{alunosA} tiraram A\n")
print(f"{alunosE} tiraram E\n")