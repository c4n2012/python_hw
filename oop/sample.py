#Each employee has: first name, second name, salary, experience (years)
class Department(object):
    def __init__(self,label,managers):
        self.label = label
        self.managers = managers

    def give_salary(self):


class Employee(object):
    def __init__(self,name,second_name,salary,expirience_years,main_manager):
        self.name = name
        self.second_name = second_name
        self.salary = salary
        self.expirience_years = expirience_years
        self.main_manager = main_manager

    def got_salary(self):
        bonus = 0
        if  2 < self.expirience_years < 5:
            bonus = 200
        elif self.expirience_years > 5:
            bonus = 500 + self.salary*0.2
        print (self.name + ' ' +  self.second_name + ' got salary ' + (self.salary + bonus))

class Designer(Employee):
    def __init__(self,name,second_name,salary,expirience_years,main_manager,coefficient):
        super.__init__(name,second_name,salary,expirience_years,main_manager)
        self.coefficient = coefficient

    def got_salary(self):
        bonus = 0
        fact_salary = self.salary*self.coefficient
        if  2 < self.expirience_years < 5:
            bonus = 200
        elif self.expirience_years > 5:
            bonus = 500 + fact_salary*0.2
        print (self.name + ' ' +  self.second_name + ' got salary ' + (fact_salary + bonus))

class Developer(Employee):
    pass

class Manager(Employee):
    def __init__(self, name, second_name, salary, expirience_years, main_manager,team_members):
        super.__init__(name, second_name, salary, expirience_years, main_manager)

    def got_salary(self):
        bonus = 0
        team_bonus = 0
        developer_bonus = 0
        developer_counter = 0
# team developers quantity bonus
        for team_member in self.team_members:
            if isinstance(team_member,Developer):
                developer_counter += 1
        if developer_counter > len(self.team_members) % 2:
            fact_salary =  self.salary * 0.1
#experience bonus
        if  2 < self.expirience_years < 5:
            bonus = 200
        elif self.expirience_years > 5:
            bonus = 500 + self.salary*0.2
# team members quantity bonus
        if self.len(self.team_members) > 5:
            team_bonus = 200
        elif self.len(self.team_members) > 10:
            team_bonus = 300
        print (self.name + ' ' +  self.second_name + ' got salary ' + (fact_salary + bonus + team_bonus + developer_bonus))
