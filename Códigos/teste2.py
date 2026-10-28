import random 
import sys
alfabeto="abcdefghijklmnopqrstuvwxyz"
frase=input("Digite uma palavra de 5 letras apra criptografar: ")
frase=frase.lower()
if not frase.isalpha():
       print("A palavra deve conter apenas letras")
       sys.exit()
deslocamento=int(input("Digite o deslocamento de 05 ate 25: "))
cifra=""
aleatorio=random.randint(0,25)
aleatorio=(aleatorio+deslocamento)
if aleatorio+deslocamento>25:
    deslocamento=deslocamento-26    
cifra=cifra+alfabeto[aleatorio+deslocamento]
aleatorio=random.randint(0,25) 
if aleatorio+deslocamento>25:   
    deslocamento=deslocamento-26    
cifra=cifra+alfabeto[aleatorio+deslocamento]
aleatorio=random.randint(0,25) 
if aleatorio+deslocamento>25:
    deslocamento=deslocamento-26    
cifra=cifra+alfabeto[aleatorio+deslocamento]
aleatorio=random.randint(0,25) 
if aleatorio+deslocamento>25:
    deslocamento=deslocamento-26    
cifra=cifra+alfabeto[aleatorio+deslocamento]
aleatorio=random.randint(0,25) 
if aleatorio+deslocamento>25:
    deslocamento=deslocamento-26    
cifra=cifra+alfabeto[aleatorio+deslocamento]
print(f"A palavra criptografada é: {cifra}")