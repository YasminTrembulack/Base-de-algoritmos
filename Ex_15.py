def contagem(num):
    while num <= 100:
        print(num, end=' \n')
        num += 1

numero = int(input("Digite um numero para a contagem \n> "))
contagem(numero)