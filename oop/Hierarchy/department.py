class Department(object):
    def __init__(self,label,managers):
        self.label = label
        self.managers = managers

    def give_salary(self):
        for manager in self.managers:
            manager.got_salary()
            for employee in manager.team_members:
                employee.got_salary()