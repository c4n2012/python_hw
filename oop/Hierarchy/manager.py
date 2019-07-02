from .employee import Employee
from .developer import Developer
from .errors import NotEmployeeException,WrongEmployeeRoleError
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

    def add_team_member(self,*args):
        print(args.__class__.__name__)
        try:
            if len(args) == 0:
                raise NotEmployeeException ('Empty employee!!!')
            elif isinstance(args,Manager):
                raise WrongEmployeeRoleError ('Employee' + new_team_member.second_name + ' is a manager!!!')
            else:
                self.team_members.append(args)
                print('Successfully added new team member to ' + self.second_name +'\'s team.')
        except NotEmployeeException:
            print('You are trying to add an empty employee.-- from print --')

        except WrongEmployeeRoleError:
            print ('Employee' + args.second_name + ' has unexpected role!-- From print --')


