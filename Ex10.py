import os
num_list = []

os.system('cls')
a = int(input("Digite o valor o numero A:"))
b = int(input("Digite o valor o numero B:"))
c = int(input("Digite o valor o numero C:"))
num_list.append(a)
num_list.append(b)
num_list.append(c)

os.system('cls')
organizar = int(input("Em que ordem deseja organizar:\n01 - Crescente\n02 - Decrescente\n03 - Maior no meio"))

os.system('cls')
if organizar == 1:
    print("Números em ordem crescente:")
    num_list.sort()
    for num in num_list:
        print(num, end=' ')
elif organizar == 2:
    print("Números em ordem decrecente:")
    num_list.sort(reverse=True)
    for num in num_list:
        print(num, end=' ')
elif organizar == 3:
    print("Números com o maior no meio:")
    num_list.sort(reverse=True)
    print(num_list[1], end=' ')
    print(num_list[0], end=' ')
    print(num_list[2], end=' ')