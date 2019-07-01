from .manager import Manager
from .employee import Employee
from .errors import SalaryGivingError

class Department(object):
    def __init__(self,label,managers):
        self.label = label
        self.managers = managers

    def give_salary(self):
        for manager in self.managers:
            try:
                if len(manager.team_members) == 0:
                    raise SalaryGivingError
                else:
                    manager.got_salary()
                    for employee in manager.team_members:
                        employee.got_salary()
            except SalaryGivingError:
                print ("Manager "+ manager.second_name + " doesn't have a team")
                break
    def add_team_members(self,manager: Manager ,team_members: Employee):
        for team_member in team_members:
            manager.add_team_member(team_member)