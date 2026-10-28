#Claudia J. Barenco Abbas
#02.09.2026

import sys
num=int(input("Digite um número de 6 algarismos: "))
if (num < 99999 or num > 999999):
    print("Número inválido! Digite um número de 6 algarismos.")
    sys.exit()
#Separa 1o digito
d1=num//100000 
print(d1)
#Guarda resto da divisão
r1=num%100000
#Separa 2o digito
d2=r1//10000
print(d2)
#Guarda resto da divisão
r2=r1%10000
#Separa 3o digito
d3=r2//1000
print(d3)
#Guarda resto da divisão
r3=r2%1000
#Separa 4o digito
d4=r3//100
print(d4)
#Guarda resto da divisão
r4=r3%100
#Separa 5o digito
d5=r4//10
print(d5)
#Guarda resto da divisão
r5=r4%10
print(r5)



