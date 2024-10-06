#config.py
# Configurações de parâmetros do SaaS de Monitoramento de Carbono

# Fatores de emissão (em kg de CO₂)
ENERGY_EMISSION_FACTOR = 0.233    # kg CO₂ por kWh de energia elétrica
TRANSPORT_EMISSION_FACTOR = 0.271  # kg CO₂ por km rodado com veículos convencionais
WASTE_EMISSION_FACTOR = 2.52      # kg CO₂ por kg de resíduos

# Limites para sugestões de melhorias
ENERGY_CONSUMPTION_THRESHOLD = 1000  # kWh
TRANSPORT_DISTANCE_THRESHOLD = 500   # km
WASTE_PRODUCED_THRESHOLD = 100       # kgy
