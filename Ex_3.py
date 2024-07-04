cod = 0
dependentes = 0
salarioB = 0.00 
salarioL = 0.00 
salarioIR = 0.00 
valor_inss = 0.00
valor_IR = 0.00
soma_INSS = 0.00
soma_IR = 0.00

cod = int(input("\n Digite o código do funcionário ou 0 para sair: \n > "))

while cod != 0:
    dependentes = int(input("\n Digite o número de dependentes \n > "))

    for i in range(12):
        salarioB = float(input(f"Digite o {i+1}° Salário Bruto: \n > "))

        if salarioB <= 1399.12:
            valor_inss = salarioB * 0.08
            soma_INSS += valor_inss
            salarioL = salarioB - valor_inss

        elif salarioB <= 2331.88:
            valor_inss = salarioB * 0.09
            soma_INSS += valor_inss
            salarioL = salarioB - valor_inss

        elif salarioB <= 4663.75:
            valor_inss = salarioB * 0.11
            soma_INSS += valor_inss
            salarioL = salarioB - valor_inss

        else:
            valor_inss = 513.01
            soma_INSS += valor_inss
            salarioL = salarioB - valor_inss

        if dependentes >= 1:
            salarioIR = salarioL - (dependentes * 189.59)

            if salarioIR <= 1903.98:
                valor_IR = 0
                soma_IR += valor_IR

            elif salarioIR <= 2826.65:
                valor_IR = ((salarioIR * 0.075) - 142.80)
                soma_IR += valor_IR
            
            elif salarioIR <= 3751.05:
                valor_IR = ((salarioIR * 0.15) - 354.80)
                soma_IR += valor_IR

            elif salarioIR <= 4664.68:
                valor_IR = ((salarioIR * 0.225) - 636.13)
                soma_IR += valor_IR
            
            else:
                valor_IR = ((salarioIR * 0.275) - 869.36)
                soma_IR += valor_IR

        else:

            salarioIR = salarioL

            if salarioIR <= 1903.98:
                valor_IR = 0
                soma_IR += valor_IR

            elif salarioIR <= 2826.65:
                valor_IR = ((salarioIR * 0.075) - 142.80)
                soma_IR += valor_IR
            
            elif salarioIR <= 3751.05:
                valor_IR = ((salarioIR * 0.15) - 354.80)
                soma_IR += valor_IR

            elif salarioIR <= 4664.68:
                valor_IR = ((salarioIR * 0.225) - 636.13)
                soma_IR += valor_IR
            
            else:
                valor_IR = ((salarioIR * 0.275) - 869.36)
                soma_IR += valor_IR
        
        salarioL += salarioL - valor_IR
        print(f"\n Salário Líquido: {salarioL}")
        print(f"\n Valor INSS: {valor_inss}")
        print(f"\n Valor IR: {valor_IR}")
    
    print(f"Funcionário: {cod}")
    print(f"Valor no ano a pagar de INSS: {soma_INSS}")
    print(f"Valor no ano a pagar de IR: {soma_IR}")

    cod = int(input("\n Digite o código do funcionário ou 0 para sair: \n > "))