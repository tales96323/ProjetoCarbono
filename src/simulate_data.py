#simulate_data.py
import random
from emissions_calculator import CarbonMonitoringSaaS
from database import save_emission_record

# Lista de empresas
companies = ["Empresa A", "Empresa B", "Empresa C"]

# Função para gerar dados simulados e salvar no banco de dados
def generate_simulated_data():
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
            emission_report['company'] = company  # Corrigir aqui

            # Salvar o registro no banco de dados
            save_emission_record(emission_report)

# Chamar a função para gerar os dados simulados
generate_simulated_data()

print("300 registros de emissões simulados foram salvos no banco de dados.")
