import pandas as pd
import matplotlib.pyplot as plt

# Lista degli anni
anni = ['2017', '2018', '2019', '2020', '2021']

# Inizializza le liste per i valori di Degree Centrality
centrality_value = []

# Loop attraverso gli anni e carica i dati
for anno in anni:
    # Carica il tuo dataset
    baci_data = pd.read_csv(f'measure_centrality_{anno}.csv')

    # Aggiungi i valori ai rispettivi elenchi
    centrality_value.append(baci_data['Degree Centrality'].mean())

# Rappresenta i valori in un grafico
plt.plot(anni, centrality_value, label='Degree Centrality', marker='o')

plt.xlabel('Anno')
plt.ylabel('Media del grado')
plt.title('Variazione di Degree Centrality')
plt.legend()
plt.grid(True)
plt.show()
