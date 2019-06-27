from .employee import Employee
class Designer(Employee):
    def __init__(self,name,second_name,salary,expirience_years,main_manager,coefficient):
        super().__init__(name,second_name,salary,expirience_years,main_manager)
        self.coefficient = coefficient

    def got_salary_designer(self):
        expirience_bonus = super().calculate_expirience_bonus(self.salary)
        fact_salary = super().salary* self.coefficient
        gross_salary = fact_salary + expirience_bonus
        print(self.name + ' ' + self.second_name + ' - experience ' + str(self.expirience_years) + ' - got salary ' + str(gross_salary))