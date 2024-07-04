import os

v_inicial = float(input("QUAL O VALOR INICIAL: "))
debito = float(input("QUAL OS DÉBITOS: "))
credito = float(input("QUAL OS CRÉDITOS: "))

resp = (v_inicial + credito) - debito
os.system('cls')
if resp > 0 : print(f"Saldo Positivo em R${resp:,.2f}.")
elif resp < 0 : print(f"Saldo Negativo em R$ R${resp:,.2f}.")
else: print("Saldo Zero .")