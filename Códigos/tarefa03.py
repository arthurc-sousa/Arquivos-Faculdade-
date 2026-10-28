def main():           
    while True:
        try:
            n = int(input("Informe o número total de cavaleiros na mesa (N > 1): "))
            if n > 1:
                break
            else:
                print("Valor inválido! O número de cavaleiros deve ser maior que 1 (N > 1).\n")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.\n")  
    cavaleiros = list(range(1, n + 1))
    pos_espada = 0
    passo = 1
    while len(cavaleiros) > 1:
        autor = cavaleiros[pos_espada]       
        pos_vitima = (pos_espada + 1) % len(cavaleiros)
        vitima = cavaleiros.pop(pos_vitima)   
        pos_espada = pos_vitima % len(cavaleiros)      
        if len(cavaleiros) > 1:
            proximo = cavaleiros[pos_espada]
            print(f"Passo {passo:02d}: Cavaleiro {autor} elimina o Cavaleiro {vitima}. "
                  f"Espada passada para o Cavaleiro {proximo}.")
            print(f"          Cavaleiros ainda vivos: {cavaleiros}")
        else:
            print(f"Passo {passo:02d}: Cavaleiro {autor} elimina o Cavaleiro {vitima}. "
                  f"Não restam outros adversários!")

        passo += 1
    # Sobrevivente final
    sobrevivente = cavaleiros[0]    
    print("                      RITUAL ENCERRADO")
    print(f"       O cavaleiro sobrevivente é o CAVALEIRO {sobrevivente}!")
    
if __name__ == "__main__":
    main()
