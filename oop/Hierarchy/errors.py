class softwareErrors(Exception):
    def __init__(self,manager):
        self.manager = manager

class SalaryGivingError(softwareErrors):
    '''Raises if manager doesn't have a team'''
    pass

class NotEmployeeException(softwareErrors):
    '''Raises when trying to add empty list to teammembers'''
    pass
class WrongEmployeeRoleError(softwareErrors):
    '''Raises when member is manager'''
    pass