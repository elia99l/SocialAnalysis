import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

# Lista degli anni
anni = ['2017','2018', '2019', '2020', '2021']

# Inizializza le liste per i valori delle densità
densità_del_commercio = []

for anno in anni:
    # Carica i dati dell'anno corrente
    baci_data = pd.read_csv(f'BACI_HS17_Y{anno}_V202301.csv')

    # Ottieni tutte le combinazioni uniche di esportatori e importatori
    combinazioni = list(combinations(set(baci_data['i']).union(set(baci_data['j'])), 2))

    # Conta le combinazioni uniche
    numero_coppie = len(combinazioni)
    #print(numero_coppie)

    # Calcola la densità
    densità = (numero_coppie / 50850) * 100  # 50850 è il numero massimo di combinazioni possibili per 226 paesi

    densità_del_commercio.append(densità)

# Rappresenta i valori di densità in un grafico cartesiano
plt.plot(anni, densità_del_commercio, marker='o', linestyle='-')
plt.xlabel('Anno')
plt.ylabel('Densità del flusso di commercio (%)')
plt.title('Variazione della densità del flusso di commercio per gli anni 2017-2021')
plt.grid(True)
plt.show()



