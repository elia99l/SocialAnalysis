import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista degli anni
anni = ['2017', '2018', '2019', '2020', '2021']

# Inizializza le liste per i valori di Eigenvector Centrality In e Eigenvector Centrality Out
eigenvector_centrality_in_values = []
eigenvector_centrality_out_values = []

# Loop attraverso gli anni e carica i dati
for anno in anni:
    # Carica dataset
    baci_data = pd.read_csv(f'measure_centrality_{anno}.csv')

    # Calcola la media delle colonne Eigenvector Centrality In e Eigenvector Centrality Out
    media_eigenvector_centrality_in = baci_data['Eigenvector Centrality In'].mean()
    media_eigenvector_centrality_out = baci_data['Eigenvector Centrality Out'].mean()

    # Aggiungi i valori alle rispettive liste
    eigenvector_centrality_in_values.append(media_eigenvector_centrality_in)
    eigenvector_centrality_out_values.append(media_eigenvector_centrality_out)

# Rappresenta i valori in un grafico lineare con scala logaritmica sull'asse y
plt.figure(figsize=(10, 5))

plt.plot(anni, eigenvector_centrality_in_values, label='Eigenvector Centrality In', marker='o')
plt.plot(anni, eigenvector_centrality_out_values, label='Eigenvector Centrality Out', marker='o')

plt.xlabel('Anno')
plt.ylabel('Media di Eigenvector Centrality (scala logaritmica)')
plt.yscale('log')  # Applica una scala logaritmica sull'asse y
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.10f'))  # Aumenta la precisione delle cifre decimali
plt.title('Variazione della media di Eigenvector Centrality nel tempo (Valori Originali)')
plt.legend()

plt.tight_layout()
plt.show()
plt.savefig('eigenvector_centrality_variance.jpg')

