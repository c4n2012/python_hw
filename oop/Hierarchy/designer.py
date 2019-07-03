from .employee import Employee
class Designer(Employee):
    def __init__(self,name,second_name,salary,expirience_years,main_manager,coefficient):
        super().__init__(name,second_name,salary,expirience_years,main_manager)
        self.coefficient = coefficient

    def got_salary(self):
        expirience_bonus = super().calculate_expirience_bonus(self.salary)
        fact_salary = self.salary* self.coefficient
        gross_salary = fact_salary + expirience_bonus
        # print(self.name + ' ' + self.second_name + ' - experience ' + str(self.expirience_years) + ' - got salary ' + str(gross_salary))
        return gross_salary

    def print_salary(self):
        gross_salary = self.got_salary()
        print(self.name + ' ' + self.second_name + ' - experience ' + str(self.expirience_years) + ' - got salary ' + str(gross_salary))