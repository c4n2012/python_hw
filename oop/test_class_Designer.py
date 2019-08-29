import unittest
from Hierarchy import Designer

class TestDesigner(unittest.TestCase):

    def setUp(self):
        self.designer = Designer('testName','testSurname',100,1,'manager1',0.5)
        self.designer2 = Designer('testName','testSurname',100,3,'manager1',0.5)
        self.designer5 = Designer('testName','testSurname',100,5,'manager1',0.5)

class TestDesignerSalaryCalculation(TestDesigner):
    def test_less_then_2_years_designer_salary_0_5_coef(self):
        self.assertEqual(self.designer.got_salary(),50)

    def test_more_then_2_years_designer_salary_0_5_coef(self):
        self.assertEqual(self.designer2.got_salary(),250)

    def test_more_then_5_years_designer_salary_0_5_coef(self):
        self.assertEqual(self.designer5.got_salary(),570)

if __name__ == '__main__':
    unittest.main()