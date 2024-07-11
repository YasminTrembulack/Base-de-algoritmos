import os
alunos = {}

os.system('cls')
qnt_alunos = int(input("Qual a quantidade de notas que deseja analisar? "))

for i in range(qnt_alunos):
    nome_aluno = input("Qual o nome do aluno? ")
    nota_aluno = float(input("Qual é a nota? "))
    alunos[nome_aluno] = nota_aluno

os.system('cls')
print("--------- NOTAS ACIMA DE 7.5 ---------")
qtd_notas_maior_sete = 0

for aluno in alunos:
    if alunos[aluno] >= 7.5:
        print(f"\tAluno(a): {aluno}, Nota: {alunos[aluno]}")
        qtd_notas_maior_sete += 1
print(f"\n{qtd_notas_maior_sete} alunos tiraram acima de 7.5")
        

