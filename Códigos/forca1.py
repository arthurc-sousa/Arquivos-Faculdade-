import os
palavra=str(input("Digite a palavra a ser advinhada."))
palavra=palavra.lower()
os.system("cis")
advinha="_"+len(palavra)
print(advinha)
while true:
    letra=str(input("Digite uma letra")) 
    letra=letra.lower()
    for i in range(0,len(palavra)):
        if letra==palavra[i]:
           advinha=advinha[::i]+letra+advinha[i+1::]
        if (palavra==advinha):
            print("Parabens voce acertou!")
            sys.exit()


