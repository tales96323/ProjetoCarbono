#test_suggestionns.py

import unittest
from emissions_calculator import CarbonMonitoringSaaS
from suggestions import get_suggestions

class TestSuggestions(unittest.TestCase):
    def test_suggestions_high_energy(self):
        system = CarbonMonitoringSaaS(1200, 300, 50)
        suggestions = get_suggestions(system)
        self.assertIn("Considere mudar para fontes de energia renováveis.", suggestions)

    def test_suggestions_high_transport(self):
        system = CarbonMonitoringSaaS(800, 600, 50)
        suggestions = get_suggestions(system)
        self.assertIn("Otimize a logística ou utilize veículos elétricos.", suggestions)

    def test_suggestions_high_waste(self):
        system = CarbonMonitoringSaaS(500, 300, 200)
        suggestions = get_suggestions(system)
        self.assertIn("Implementar programas de reciclagem.", suggestions)

    def test_suggestions_no_issues(self):
        system = CarbonMonitoringSaaS(800, 400, 50)
        suggestions = get_suggestions(system)
        self.assertIn("Suas operações já são eficientes!", suggestions)

if __name__ == '__main__':
    unittest.main()
