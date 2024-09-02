import pandas as pd 
import numpy as np 
from datetime import datetime

# CRIAÇÃO DE ARQUIVO PARA SIMULAR FATURAMENTO
ano = 2024
datas = pd.date_range(start=f'01/01/{ano}', end=f'31/12/{ano}')

# VALORES ALEATORIOS DE FATURAMENTO
np.random.seed(12)  # para resultados consistentes
faturamento = np.round(np.random.uniform(0, 100000, size=len(datas)), 2)

# FINAIS DE SEMANA (SABADOS E DOMINGOS)
finais_de_semana = datas.weekday >= 5

# LISTA DE FERIADOS
feriados = pd.to_datetime([
    f'{ano}-01-01',  # Ano Novo
    f'{ano}-02-12',  # Carnaval
    f'{ano}-03-29',  # Sexta-feira Santa
    f'{ano}-04-21',  # Tiradentes
    f'{ano}-05-01',  # Dia do Trabalhador
    f'{ano}-06-15',  # Corpus Christi
    f'{ano}-09-07',  # Independência do Brasil
    f'{ano}-10-12',  # Nossa Senhora Aparecida
    f'{ano}-11-02',  # Finados
    f'{ano}-11-15',  # Proclamação da República
    f'{ano}-12-25'   # Natal
])

feriados_boolean = datas.isin(feriados)

# MARCAR FINAIS DE SEMANA E FERIADOS COM O NULO
dias_nulos = finais_de_semana | feriados_boolean
faturamento[dias_nulos] = np.nan

# DATAFRAME DO FATURAMENTO ANUAL
faturamento_anual = pd.DataFrame({
    'Data': datas,
    'Faturamento': faturamento
})

# SALVAR COMO ARQUIVO XML
faturamento_anual.to_xml("C:/Users/anate/OneDrive/Documentos/faturamento.xml", index=False)

#-----------------------------------------------------------------------------------------------------
# AQUI SE INICIA A SIMULACAO PARA VERIFICAR OS RESULTADOS SOBRE OS DADOS GERADOS

# IMPORTAR ARQUIVO XML
dados = pd.read_xml("C:/Users/anate/OneDrive/Documentos/faturamento.xml", parser='etree')

# COLUNA DATA PARA DATATIME
dados['Data'] = pd.to_datetime(dados['Data'])

while True:
    try:
        # SOLICITAR MES AO USUARIO
        mes = int(input("\nSelecione um mês entre 1 e 12: "))
        
        if mes < 1 or mes > 12:
            raise ValueError  # erro se o mes estiver fora do intervalo

        # MES SELECIONADO
        dados_mes = dados[dados['Data'].dt.month == mes]

        if dados_mes.empty:
            print("Não há dados para o mês selecionado.")
            continue

        # NOME DO MES
        nome_mes = dados_mes['Data'].dt.strftime('%B').iloc[0].upper()

        # MEDIA/MINIMO/MAXIMO DE FATURAMENTO NO MES
        media = dados_mes['Faturamento'].mean()
        minimo = dados_mes['Faturamento'].min()
        maximo = dados_mes['Faturamento'].max()

        # DIAS ACIMA DA MEDIA
        acima_media = dados_mes[dados_mes['Faturamento'] > media].shape[0]

        # RESULTADO
        print(f"\n{nome_mes}: \n Saldo Mínimo: R${minimo:.2f}\n Saldo Máximo: R${maximo:.2f} \n Saldo Médio: R${media:.2f}")
        print(f" Quantidade de dias acima da média: {acima_media}")

    except ValueError:
        print("Mês inválido!")

    while True:
        resposta = input("\nDeseja continuar (s/n)? ").lower()
        
        if resposta in ['s', 'n']:
            break  # Sai do loop se a resposta for válida
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")

    if resposta == "n":
        print("\nSessão encerrada!\n")
        break

    



