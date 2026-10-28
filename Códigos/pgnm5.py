frase = input("Digite a palavra ou frase")
frase = frase.replace(" ", "").lower()
fraseaocontrario=frase[::-1]
print("A frase invertida é: "+fraseaocontrario)
if frase==fraseaocontrario:
   print("A frase é um palindromo.")
else:
   print("A frase não é um palindromo.")
   