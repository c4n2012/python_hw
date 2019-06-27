class Employee(object):
    def __init__(self,name,second_name,salary,expirience_years,main_manager):
        self.name = name
        self.second_name = second_name
        self.salary = salary
        self.expirience_years = expirience_years
        self.main_manager = main_manager

    def calculate_expirience_bonus(self,salary):
        bonus = 0
        if  2 < self.expirience_years < 5:
            bonus = 200
        elif self.expirience_years > 5:
            bonus = 500 + self.salary*0.2
        return bonus

    def got_salary(self):
        bonus = self.calculate_expirience_bonus(self.salary)
        gross_salary = self.salary + bonus
        print (self.name + ' ' +  self.second_name + ' - experience '+ str(self.expirience_years) + ' - got salary ' + str(gross_salary))
