import os

def calculo_gasolina(preco_litro, valot_pagamento):
    return valot_pagamento // preco_litro

os.system('cls')
nome = input("Informe seu nome: ")
v_litro_gasolina = float(input("Informe o valor do litro de gasolina: "))
v_pagamento = float(input("Informe o valor de pagamento: "))

print(f"\n{nome} você vai abastecer aproximadamente {calculo_gasolina(v_litro_gasolina, v_pagamento)} litros de gasolina.")