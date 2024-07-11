def parOuImpar(num):
    pi = ''

    if num %2 == 0:
        pi = " é par."
    else:
        pi = " é impar."
    
    return pi

numero = int(input(f"\n Informe um número: \n> "))
print(f"O numero {numero}{parOuImpar(numero)}")