# plotter.py
import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_emissions_over_time(emission_records, output_dir='outputs'):
    # Cria um DataFrame a partir dos registros de emissões
    data = {
        'date_recorded': [record.date_recorded for record in emission_records],
        'company': [record.company for record in emission_records],
        'total_emissions': [record.total_emissions for record in emission_records],
    }
    df = pd.DataFrame(data)

    # Agrupa as emissões por data e empresa
    df_grouped = df.groupby(['date_recorded', 'company']).sum().reset_index()

    # Certifica-se de que o diretório de saída existe
    os.makedirs(output_dir, exist_ok=True)

    # Cria o gráfico de linha
    plt.figure(figsize=(12, 6))
    for company in df_grouped['company'].unique():
        company_data = df_grouped[df_grouped['company'] == company]
        plt.plot(company_data['date_recorded'], company_data['total_emissions'], marker='o', label=company)

    plt.title('Evolução das Emissões de CO₂ ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Emissões Totais de CO₂ (kg)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Salva o gráfico
    output_path = os.path.join(output_dir, 'emissions_over_time.png')
    plt.savefig(output_path)
    plt.close()

    print(f'Gráfico de emissões ao longo do tempo salvo em: {output_path}')
