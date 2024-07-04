
import os


def conta(num):
    while num <= 100:
        print(num)
        num += 1

os.system("cls")
try:
    num = int(input("Informe um número pra ir dele até 100: "))
    conta(num)
except:
    print("Erro! Número inválido.")
