class Estagiarios:
    def __init__(self, codigo, nome, ano, salarios, salario_anual):
        self.codigo = codigo
        self.nome = nome
        self.ano = ano
        self.salarios = salarios
        self.salario_anual = salario_anual

qtos = 0
fichas = []

for i in range(2):
    codigo = int(input("\n Qual o código do estágiário? \n > "))
    nome = input("\n Qual o nome do estagiário? \n > ")
    ano = int(input("\n Qual o ano de nascimento do estagiário? \n > "))

    salarios = []
    salario_anual = 0

    for j in range(12):
        
        salario = float(input(f"\n Qual o {j+1}° salario do estágiário: \n > "))

        salarios.append(salario)
        salario_anual += salario

    qtos += 1
    print(f"\n\n {qtos}° estagiário adicionado.")

    ficha = Estagiarios(codigo, nome, ano, salarios, salario_anual)
    fichas.append(ficha)

for idx, ficha in enumerate(fichas):
    print("\n\n -----------------------------------------------")
    print(f"\n Código: {ficha.codigo}")
    print(f"\n Nome: {ficha.nome}")
    print(f"\n Ano de nascimento: {ficha.ano}")
    print(f"\n Salários mensais: {ficha.salarios}")
    print(f"\n Salário anual: {ficha.salario_anual}")
    print("\n\n -----------------------------------------------")