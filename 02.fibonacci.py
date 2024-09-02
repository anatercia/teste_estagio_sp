# Função para calcular Fibonacci
def fibonacci(n):
    inicial = [0, 1]

    # Verifica se n é 0 ou 1
    if n == 0 or n == 1:
        return f"O {n} pertence à sequência de Fibonacci."

    else:
        # Gera a sequência de Fibonacci até que o último elemento seja maior que n
        while inicial[-1] < n:
            proximo = inicial[-1] + inicial[-2]
            inicial.append(proximo)

        # Verifica se n está na lista de Fibonacci gerada
        if n in inicial:
            return f"O {n} pertence à sequência de Fibonacci."
        else:
            return f"O {n} não pertence à sequência de Fibonacci."

# Código para entrada e verificação de um número na lista Fibonacci
print("Bem-vindo(a) a sessão de verificação do número fibonacci!")

while True:
    try:
        n = int(input("\nDigite um número inteiro: "))
        print(fibonacci(n))
        
    except ValueError:
        print("Número inválido!")

    while True:
        resposta = input("\nDeseja continuar? (s/n) ").lower()
        
        if resposta in ['s', 'n']:
            break  # Sai do loop se a resposta for válida
        
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")

    if resposta == "n":
        print("\nSessão encerrada!")
        break


