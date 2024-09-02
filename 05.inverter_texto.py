# INVERTER STRING
print("Bem-vindo(a) a sessão de inversão de texto!")

while True:
    try:
        # LER STRING
        texto = str(input("\nDigite um texto para inverter: "))

        # LER DO ULTIMO CARACTER PARA O INICIO
        print("\nTEXTO INVERTIDO: ")
        for i in range(len(texto)):
            print(texto[-(i + 1)], end='')

        print("\n")

    except ValueError:
        print("Texto inválido!")

    while True:
        resposta = input("Deseja continuar? (s/n) ").lower()
        
        if resposta in ['s', 'n']:
            break  # Sai do loop se a resposta for válida
        
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")

    if resposta == "n":
        print("\nSessão encerrada!")
        break
