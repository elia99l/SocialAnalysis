import pandas as pd
import numpy as np
import networkx as nx

# Carica i dati
baci_data = pd.read_csv('BACI_HS17_Y2020_V202301.csv')
coordinates_data = pd.read_csv('country_code_and_coordinates_merged.csv', sep=";")

# Raggruppa i dati BACI per esportatori e importatori
exporter_degree = baci_data.groupby('i').size().reset_index(name='exporter_degree')
importer_degree = baci_data.groupby('j').size().reset_index(name='importer_degree')

# Unisci i dati con i country_code
exporter_degree = pd.merge(exporter_degree, coordinates_data, left_on='i', right_on='country_code', how='left')
importer_degree = pd.merge(importer_degree, coordinates_data, left_on='j', right_on='country_code', how='left')

# Seleziona solo le colonne necessarie
exporter_degree = exporter_degree[['country_name_full', 'country_code', 'exporter_degree']]
importer_degree = importer_degree[['country_name_full', 'country_code', 'importer_degree']]

# Visualizza la tabella risultante
result_table = pd.merge(exporter_degree, importer_degree, on=['country_name_full', 'country_code'], how='outer').fillna(0)
result_table.columns = ['Country', 'Country Code', 'Exporter Degree', 'Importer Degree']

# Costruisci il grafo diretto da BACI_data
G = nx.from_pandas_edgelist(baci_data, 'i', 'j', create_using=nx.DiGraph())

# Calcola l'eigenvector centrality per i nodi in entrata senza pesi aggiuntivi
A = nx.adjacency_matrix(G).todense()  # Matrice di adiacenza
eigenvalue, eigenvector = np.linalg.eigh(A.T)  # Utilizza eigh per matrici simmetriche
dominant_eigenvector_in = eigenvector[:, np.argmax(eigenvalue)]
dominant_eigenvector_in = np.abs(dominant_eigenvector_in)
dominant_eigenvector_in /= np.sum(dominant_eigenvector_in)  # Normalizza gli autovettori

# Calcola l'eigenvector centrality per i nodi in uscita senza pesi aggiuntivi
A_out = nx.adjacency_matrix(G).todense()  # Matrice di adiacenza
eigenvalue_out, eigenvector_out = np.linalg.eigh(A_out)  # Utilizza eigh per matrici simmetriche
dominant_eigenvector_out = eigenvector_out[:, np.argmax(eigenvalue_out)]
dominant_eigenvector_out = np.abs(dominant_eigenvector_out)
dominant_eigenvector_out /= np.sum(dominant_eigenvector_out)  # Normalizza gli autovettori

# Calcola la closeness centrality
closeness_centrality = nx.closeness_centrality(G)

# Converte i risultati in un DataFrame
result_df_in = pd.DataFrame({'Country': list(G.nodes()), 'Eigenvector Centrality In': dominant_eigenvector_in})
result_df_out = pd.DataFrame({'Country': list(G.nodes()), 'Eigenvector Centrality Out': dominant_eigenvector_out})
result_closeness = pd.DataFrame({'Country': list(G.nodes()), 'Closeness Centrality': list(closeness_centrality.values())})

# Sostituisci i valori nella colonna 'Country' con quelli da 'country_name_full'
result_df_in['Country'] = result_df_in['Country'].map(coordinates_data.set_index('country_code')['country_name_full'])
result_df_out['Country'] = result_df_out['Country'].map(coordinates_data.set_index('country_code')['country_name_full'])
result_closeness['Country'] = result_closeness['Country'].map(coordinates_data.set_index('country_code')['country_name_full'])

# Assicurati che 'Country' sia di tipo stringa
result_df_in['Country'] = result_df_in['Country'].astype(str)
result_df_out['Country'] = result_df_out['Country'].astype(str)
result_closeness['Country'] = result_closeness['Country'].astype(str)

# Unisci i risultati con la tabella principale
result_table = pd.merge(result_table, result_df_in, on='Country', how='left')
result_table = pd.merge(result_table, result_df_out, on='Country', how='left')
result_table = pd.merge(result_table, result_closeness, on='Country', how='left')

# Riempie i valori mancanti con zero
result_table[['Eigenvector Centrality In', 'Eigenvector Centrality Out', 'Closeness Centrality']] = result_table[['Eigenvector Centrality In', 'Eigenvector Centrality Out', 'Closeness Centrality']].fillna(0)

# Calcola la misura di centralità di grado
result_table['Degree Centrality'] = result_table['Exporter Degree'] + result_table['Importer Degree']

# Ordina la tabella in base alla centralità più alta
result_table = result_table.sort_values(by='Degree Centrality', ascending=False)

# Resetta gli indici
result_table = result_table.reset_index(drop=True)

# Visualizza la tabella risultante con la misura di centralità di grado, eigenvector centrality e closeness centrality
print(result_table[['Country', 'Country Code', 'Exporter Degree', 'Importer Degree', 'Degree Centrality', 'Eigenvector Centrality In', 'Eigenvector Centrality Out', 'Closeness Centrality']])

# Salva la tabella risultante in un file CSV
result_table.to_csv('measure_centrality_2020.csv', index=False)
