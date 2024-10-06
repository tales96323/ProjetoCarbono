# emissions_calculator.py
import matplotlib.pyplot as plt
import seaborn as sns
import os
from database import save_emission_record

# emissions_calculator.py
class CarbonMonitoringSaaS:
    def __init__(self, energy_consumption, transport_distance, waste_produced):
        self.energy_consumption = energy_consumption
        self.transport_distance = transport_distance
        self.waste_produced = waste_produced

    def calculate_energy_emissions(self):
        return self.energy_consumption * 0.233  # Coeficiente de emissões de energia em kg CO2/kWh

    def calculate_transport_emissions(self):
        return self.transport_distance * 0.146  # Coeficiente de emissões de transporte em kg CO2/km

    def calculate_waste_emissions(self):
        return self.waste_produced * 0.05  # Coeficiente de emissões de resíduos em kg CO2/kg

    def generate_report(self):
        energy_emissions = self.calculate_energy_emissions()
        transport_emissions = self.calculate_transport_emissions()
        waste_emissions = self.calculate_waste_emissions()

        total_emissions = energy_emissions + transport_emissions + waste_emissions

        report_data = {
            'energy_emissions': energy_emissions,
            'transport_emissions': transport_emissions,
            'waste_emissions': waste_emissions,
            'total_emissions': total_emissions,
        }

        return report_data


    def generate_graph(self):
        _, energy_emissions, transport_emissions, waste_emissions = self.calculate_emissions()
        categories = ['Energy', 'Transport', 'Waste']
        emissions = [energy_emissions, transport_emissions, waste_emissions]

        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 6))
        plt.bar(categories, emissions, color=['#2ca02c', '#1f77b4', '#ff7f0e'])
        plt.title('CO₂ Emissions by Category', fontsize=14)
        plt.xlabel('Category', fontsize=12)
        plt.ylabel('Emissions (kg)', fontsize=12)

        output_dir = "src/reports"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, "emission_report.png")
        plt.savefig(output_file)
        plt.close()

        return output_file
