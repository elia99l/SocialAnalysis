import pandas as pd
import matplotlib.pyplot as plt

# Lista degli anni
anni = ['2017', '2018', '2019', '2020', '2021']

# Inizializza la lista per i valori di Closeness Centrality
closeness_centrality_values = []

# Loop attraverso gli anni e carica i dati
for anno in anni:
    # Carica il tuo dataset
    baci_data = pd.read_csv(f'measure_centrality_{anno}.csv')


    # Assicurati che la colonna "Closeness Centrality" esista nel tuo dataset
    if 'Closeness Centrality' in baci_data.columns:
        # Calcola la media della colonna "Closeness Centrality"
        media_closeness_centrality = baci_data['Closeness Centrality'].mean()

        # Aggiungi il valore alla lista
        closeness_centrality_values.append(media_closeness_centrality)
    else:
        # Se la colonna non esiste, aggiungi un valore vuoto
        closeness_centrality_values.append(None)

# Rappresenta i valori in un grafico
plt.figure(figsize=(10, 5))

plt.plot(anni, closeness_centrality_values, marker='o')
plt.xlabel('Anno')
plt.ylabel('Media di Closeness Centrality')
plt.title('Variazione della media di Closeness Centrality nel tempo')

plt.tight_layout()
plt.show()
