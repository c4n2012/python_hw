import unittest
from Hierarchy import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('testName','testSurname',100,1,'manager1')
        self.employee2 = Employee('testName','testSurname',100,3,'manager1')
        self.employee5 = Employee('testName','testSurname',100,5,'manager1')

class TestExpirienceBonus(TestEmployee):
    def test_less_then_2_years_bonus(self):
        self.assertEqual(self.employee.calculate_expirience_bonus(self.employee.salary),0)
    def test_more_then_2_years_bonus(self):
        self.assertEqual(self.employee2.calculate_expirience_bonus(self.employee2.salary),200)
    def test_more_then_5_years_bonus(self):
        self.assertEqual(self.employee5.calculate_expirience_bonus(self.employee5.salary),520)

if __name__ == '__main__':
    unittest.main()