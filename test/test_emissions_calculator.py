#test_emissions_calculator.py

import unittest
from emissions_calculator import CarbonMonitoringSaaS

class TestEmissionsCalculator(unittest.TestCase):
    def test_calculate_emissions(self):
        system = CarbonMonitoringSaaS(1200, 800, 150)
        total, energy, transport, waste = system.calculate_emissions()
        self.assertAlmostEqual(total, 874.4, places=1)
        self.assertAlmostEqual(energy, 279.6, places=1)

if __name__ == '__main__':
    unittest.main()