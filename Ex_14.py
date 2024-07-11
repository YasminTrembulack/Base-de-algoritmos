def calcular(a, b):
    soma = a + b
    multi = a * b

    if (soma %2 == 0):
        return 'par', soma, multi
    else:
        return 'impar', soma, multi

num_1 = int(input("\n Digite o primeiro numero \n> "))
num_2 = int(input("\n Digite o segundo numero \n> "))

resp, soma, multi = calcular(num_1, num_2)

print(f"\n A soma dos numeros é {soma}.")
print(f" A multiplicação dos numeros é: {multi}.")
print(f" O numero {soma} é {resp}.")