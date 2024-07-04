
import os

class dadosImoveis:
    def __init__(self, numero_cadastro, iptu, meses_atraso):
        self.nc = numero_cadastro
        self.iptu = iptu
        self.meses_atraso = meses_atraso
        self.multa = self.calcularMulta()
        
    def calcularMulta(self):
        return 50.00 * self.meses_atraso

    def __str__(self):
        return f"CADASTRO: {self.nc}\nVALOR IPTU: {self.iptu}\nMESES EM ATRASO: {self.meses_atraso}\nMULTA: {self.multa:,.2f}\n"


qtd = int(input("Quantos imoveis deseja cadastar:"))

list_imoveis = []

for i in range(qtd):
    os.system('cls')
    nc = input(f"\nINFOME O {i+1} NUMERO DE CADASTRO: ")
    iptu = input("INFOME O VALOR DO IPTU: ")
    meses = int(input("INFOME QUANTOS MESES ATRASADO: "))
    imovel = dadosImoveis(nc, iptu, meses)
    list_imoveis.append(imovel)

os.system('cls')
for imovel in list_imoveis:
    print(imovel)
    
print(f"No total foram add {qtd} imoveis.")

