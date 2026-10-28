#programa que mostra a tabela ASCII
#Claudia Jacy Barenco Abbas
#31.08.2026
#Caracteres de controle (0-31 e 127): Eles não são imprimíveis e são usados ​​para gerenciar dispositivos e controlar o fluxo de dados. 
#Eles incluem comandos como avanço de linha e retorno de carro de impressora.
#Caracteres imprimíveis (32-126): Eles incluem letras (maiúsculas e minúsculas), números, símbolos matemáticos e sinais de pontuação.
#ASCII estendido (128-255): Caracteres de outros idiomas são incluídos, como a letra ñ, acentos e símbolos especiais.
import time
for i in range(1,256):
    if i < 32 or i > 126:
        char = repr(chr(i))
    else:
        char = chr(i) 
    print(f"{char} => {i}\n")
    time.sleep(0.1)  # Pausa de 0.1 segundos entre cada caractere
while True :
    i=int(input("Digite um numero de 1 a 255 para ver o caractere correspondente na tabela ASCII e 0 para sair\n"))
    if i < 0 or i > 255:
        print("Numero invalido")
        continue
    if i == 0:
        break
    if i < 32 or i > 126:
        char = repr(chr(i))
    else:
        char = chr(i) 
    print(f"{char} => {i}\n")