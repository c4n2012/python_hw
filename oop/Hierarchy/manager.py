from .employee import Employee
from .developer import Developer
class Manager(Employee):
    def __init__(self, name, second_name, salary, expirience_years, main_manager, team_members):
        super().__init__(name, second_name, salary, expirience_years, main_manager)
        self.team_members = team_members

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
            developer_bonus =  self.salary * 0.1
#experience bonus
        expirience_bonus = super().calculate_expirience_bonus(self.salary)
# team members quantity bonus
        if len(self.team_members) > 5:
            team_bonus = 200
        elif len(self.team_members) > 10:
            team_bonus = 300
        gross_salary = self.salary + expirience_bonus + team_bonus + developer_bonus
        print ('--TEAMLEAD-- '+self.name + ' ' +  self.second_name + ' - experience '+ str(self.expirience_years) + ' - got salary ' + str(gross_salary))
