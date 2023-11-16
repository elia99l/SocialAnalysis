import pandas as pd

# Inizializza un DataFrame vuoto
result_table = pd.DataFrame(columns=['Anno', 'Best Exporter Degree', 'Best Importer Degree', 'Best Exporter Eigenvector In', 'Best Exporter Eigenvector Out',
                                      'Best Country Closeness Centrality'])
# Lista degli anni
anni = ['2017', '2018', '2019', '2020', '2021']

# Loop attraverso gli anni e carica i dati
for anno in anni:
    baci_data = pd.read_csv(f'measure_centrality_{anno}.csv')

    # Trova il miglior esportatore in base a ciascuna misura di centralità
    best_exporter_by_degree = baci_data.loc[baci_data['Exporter Degree'].idxmax()]
    best_exporter_by_eigenvector_out = baci_data.loc[baci_data['Eigenvector Centrality Out'].idxmax()]

    # Trova il miglior importatore in base a ciascuna misura di centralità
    best_importer_by_degree = baci_data.loc[baci_data['Importer Degree'].idxmax()]
    best_exporter_by_eigenvector_in = baci_data.loc[baci_data['Eigenvector Centrality In'].idxmax()]

    #Trova il miglior paese con il Closeness centrality maggiore
    best_country_closeness = baci_data.loc[baci_data['Closeness Centrality'].idxmax()]

    result_table = result_table._append({
        'Anno': anno,
        'Best Exporter Degree': best_exporter_by_degree['Country'],
        'Best Importer Degree': best_importer_by_degree['Country'],
        'Best Exporter Eigenvector In': best_exporter_by_eigenvector_in['Country'],
        'Best Exporter Eigenvector Out': best_exporter_by_eigenvector_out['Country'],
        'Best Country Closeness Centrality': best_country_closeness['Country']
    }, ignore_index=True)

# Stampa la tabella risultante
print(result_table)

# Salva la tabella risultante in un file CSV
result_table.to_csv('best_exp_imp.csv', index=False)