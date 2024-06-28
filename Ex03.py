
# Base-de-algoritmos-em-C-v3 / exer19funcoes.c

# #include<stdio.h>
# #include<locale.h>

# float ideal_homem ( float p_altH);
# float ideal_mulher ( float p_altF);

# void main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	float alt = 0,resh = 0,resf = 0;
# 	char sexo;
	
# 	printf("Informe seu sexo((M) Masculino e (F) Feminino):\n");
# 	fflush(stdin);
# 	scanf("%c",&sexo);
	
# 	printf("_________________________________________________\n");
	
# 	printf("Informe sua altura (com (,) separando metros de centimetros):\n");
# 	fflush(stdin);
# 	scanf("%f",&alt);
	
# 	printf("_________________________________________________\n");
	
# 	if(sexo =='M' || sexo =='m'){
# 		resh = ideal_homem(alt);
# 		printf("RESPOSTA");
# 		printf("\nSeu peso ideal é:%.2f kilos.\n",resh);
# 		printf("_________________________________________________\n");
# 	}
# 	else{
# 		resf = ideal_mulher(alt);
# 		printf("RESPOSTA");
# 		printf("\nSeu peso ideal é:%.2f kilos.\n",resf);
# 		printf("\n\n_________________________________________________\n");
# 	}

	
# 	system("pause");

# }


# float ideal_homem ( float p_altH){
# 	float valorH;
	
# 	valorH = (72.7 * p_altH) - 58;
# 	return valorH;
# }

# float ideal_mulher ( float p_altF){
# 	float valorF;
	
# 	valorF = (62.1 * p_altF) - 44.7;
# 	return valorF;
# }




import os
os.system("cls")
def calcPesoIdeal(sexo, altura):
    if sexo.lower() == 'm':
        return (72.7 * altura) - 58
    elif sexo.lower() == 'f':
        return (62.1 * altura) - 44.7
    else:
        print("\nErro! Sexo não reconhecido pelo sistema.")
        return 0


sexo = input("\nInforme seu sexo((M) Masculino e (F) Feminino):")
print("_________________________________________________\n")
try:
    altura = float(input("Informe sua altura: "))
    print("_________________________________________________\n")
except:
    print("\nErro! Altura inválida.\n")
    os.system("pause")
    exit()

pesoIdeal = calcPesoIdeal(sexo, altura)
if pesoIdeal:
    print(f"Seu peso ideal é: {pesoIdeal:,.2f}\n")
os.system("pause")