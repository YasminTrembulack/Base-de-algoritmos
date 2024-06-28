# Base-de-algoritmos-em-C-v3 / EX_02.c

# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# char calcula(int n1, int n2, int *p_soma, int *p_multi);

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int n1 = 0, n2 = 0, soma = 0, multi = 0, resp = 0;

	
# 	printf("DIGITE O PRIMEIRO NÚMERO:");
# 	fflush(stdin);
# 	scanf("%d",&n1);
		
# 	printf("DIGITE O SEGUNDO NÚMERO:");
# 	fflush(stdin);
# 	scanf("%d",&n2);
	
# 	resp = calcula(n1,n2, &soma, &multi);
	
# 	printf("\nA soma dos 2 números informados é = %d.\n", soma);
# 	printf("A multipicação dos 2 números informados é = %d.\n", multi);
# 	printf("%c.\n\n\n",resp);
	
# 	system("pause");
# }
# char calcula(int n1, int n2, int *p_soma, int *p_multi){
	
# 	*p_soma = n1 + n2;
	
	
# 	*p_multi = n1 * n2;
	
	
# 	char pi;
	
# 	if(*p_soma % 2 == 0){
# 		pi = 'P';
# 		return(pi);
# 	}
# 	else{
# 		pi = 'I';
# 		return(pi);
# 	}
	
# }



import os
def calcula( num1, num2):
    global soma, mult
    soma = num1 + num2
    mult = num1 * num2

    if soma % 2 == 0:
        return "P"
    else:
        return "I"

soma = 0
mult = 0

os.system("cls")
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resp = calcula(num1, num2)

    print(f"\nA soma dos 2 números informados é = {soma}")
    print(f"\nA multipicação dos 2 números informados é = {mult}")
    print(f"\n{resp}\n")
except:
    print("\nErro! Número 1 ou 2 invalído.\n")

os.system("pause")