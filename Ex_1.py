TAM = 3

candidatos = []

class fichaCandidato:
    def __init__(self, codigo, salario, mail):
        self.codigo = codigo
        self.salario = salario
        self.mail = mail


for i in range(TAM):
    print("\n\n============================")
    print(f"\nInforme o código: {i+1}")
    codigo = int(input("\n> "))

    print(f"\nInforme o salario: {i+1}")
    salario = float(input("\n> "))

    print(f"\nInforme o email: {i+1}")
    email = input("\n> ")

    candidato = fichaCandidato(codigo, salario, email)

    candidatos.append(candidato)

for i, cand in enumerate(candidatos):
    print("\n\n=====================================")
    print(f"\nCandidato {i+1}:")
    print(f"\nCódigo: {candidato.codigo}")
    print(f"Salário: {candidato.salario}")
    print(f"Email: {candidato.mail}")