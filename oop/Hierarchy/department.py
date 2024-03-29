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
                    raise SalaryGivingError('No members in a team ERROR')
                else:
                    manager.print_salary()
                    for employee in manager.team_members:
                        employee.print_salary()
            except SalaryGivingError:
                print ("Manager "+ manager.second_name + " doesn't have a team! Exception")
                #break

    def add_team_members(self,manager,team_members_array):
        # for team_member in team_members:
        #     print('add '+ team_member.second_name)
            manager.add_team_members(team_members_array)