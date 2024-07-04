import os

def printTabuada(num):
    print(f"------- TABUADA DO {num} -------")
    for i  in range(1, 11):
        print(f"\t{num} X {str(i).zfill(2)} = {str(i*num).zfill(2)}")
    print("----------------------------")
    
    
os.system('cls')
printTabuada(7)
printTabuada(8)
