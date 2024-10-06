#suggestions.py
def get_suggestions(monitoring_system):
    suggestions = y
    if monitoring_system.energy_consumption > 1000:
        suggestions.append("Considere mudar para fontes de energia renováveis.")
    if monitoring_system.transport_distance > 500:
        suggestions.append("Otimize a logística ou utilize veículos elétricos.")
    if monitoring_system.waste_produced > 100:
        suggestions.append("Implementar programas de reciclagem.")
    if not suggestions:
        suggestions.append("Suas operações já são eficientes!")
    return suggestions
