# src/main.py
from emissions_calculator import CarbonMonitoringSaaS
from database import get_all_records, save_emission_record
from plotter import plot_emissions, plot_emissions_over_time
import random
from datetime import datetime, timedelta

# Lista de empresas
companies = ["Empresa A", "Empresa B", "Empresa C"]

# Função para gerar uma data aleatória entre duas datas
def generate_random_date(start_date, end_date):
    """Gera uma data aleatória entre start_date e end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date

# Função para gerar dados simulados e salvar no banco de dados
def generate_simulated_data():
    start_date = datetime(2023, 1, 1)  # Data inicial para simulação
    end_date = datetime(2023, 12, 31)  # Data final para simulação
    
    for company in companies:
        for _ in range(100):  # Gerar 100 entradas por empresa
            # Simular consumo de energia (kWh), distância de transporte (km) e produção de resíduos (kg)
            energy_consumption = random.uniform(500, 5000)  # Entre 500 e 5000 kWh
            transport_distance = random.uniform(50, 2000)   # Entre 50 e 2000 km
            waste_produced = random.uniform(50, 1000)       # Entre 50 e 1000 kg

            # Instanciar o sistema para calcular as emissões
            monitoring_system = CarbonMonitoringSaaS(energy_consumption, transport_distance, waste_produced)

            # Gerar o relatório de emissões
            emission_report = monitoring_system.generate_report()

            # Adicionar o nome da empresa no relatório
            emission_report['company'] = company

            # Gerar uma data aleatória
            random_date = generate_random_date(start_date, end_date)

            # Salvar o registro no banco de dados com a data simulada
            save_emission_record(emission_report, date_recorded=random_date)

# Gerar os dados simulados
generate_simulated_data()

print("300 registros de emissões simulados foram salvos no banco de dados.")

# Consultar todos os registros salvos no banco de dados
all_records = get_all_records()

# Exibir registros organizados por empresa
print("\nHistórico de emissões armazenado por empresa:")
for company in companies:
    print(f"\nRegistros da {company}:")
    for record in all_records:
        if record.company == company:
            print(f"ID: {record.id} | Empresa: {record.company} | Energia: {record.energy_emissions} kg | Transporte: {record.transport_emissions} kg | Resíduos: {record.waste_emissions} kg | Total: {record.total_emissions} kg | Data de registro: {record.date_recorded}")

# Plotar as emissões ao longo do tempo
plot_emissions_over_time(all_records)
