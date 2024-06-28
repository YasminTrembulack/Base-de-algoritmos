# Base-de-algoritmos-em-C-v3 / EX_04.c


# #include <stdio.h>
# #include <stdlib.h>
# #include <locale.h>

# void conta (int x);

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
# 	int num;
	
# 	printf("Informe um número pra ir dele até 100:");
# 	scanf("%d", &num);
# 	conta(num);
	
# 	system("pause");
# 	return 0;
	
# }

# void conta (int x){
		
# 	if( x <= 100) {
# 		printf("%d \n", x);
# 		conta(x + 1);
		
# 	}
# }

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
