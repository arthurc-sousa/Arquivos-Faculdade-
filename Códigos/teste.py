import random 
import sys
aleatorio=random.randint(1,5)
numero=(input("Digite um número de 1 a 5: "))
if not numero.isdigit():
    print("Número inválido")
    sys:exit()
if numero==aleatorio:
    print("Parabens voce acertou o numero")
else:
    print("Você errou o número, o numero correto era: "+str(aleatorio))
    print(f"Você errou o número, o numero correto era: ^{aleatorio}")