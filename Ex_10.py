valores = []
busca = 0
achou = 0

for i in range(10):
    valor = int(input(f"Informe o {i+1}° valor: \n> "))
    valores.append(valor)

busca = int(input("\n Informe um valor a ser procurado \n > "))

for i in range(len(valores)):
    if busca == valores[i]:
        achou += 1

print(f"O número {busca} foi achado {achou} vezes.")