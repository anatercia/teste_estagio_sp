# FATURAMENTO POR ESTADO
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# TOTAL
total_mensal = sum(faturamento.values())

# Calcular e exibir o percentual de representação para cada estado
print(f"Valor total: R${total_mensal:.2f}")
print("Percentual por estado:")
for estado in faturamento:
    percentual = (faturamento[estado] / total_mensal) * 100
    print(f"{estado}: {percentual:.2f}%")

