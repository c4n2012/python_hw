from Hierarchy import Department
from Hierarchy import Manager
from Hierarchy import Developer
from Hierarchy import Designer

#name,second_name,salary,expirience_years,main_manager,coefficient
designer1 = Designer('Alex','Petrov',130,2,'manager1',0.5)
designer2 = Designer('Ax','Prov',110,4,'manager1',0.8)
designer3 = Designer('Al','Petr',180,4,'manager1',0.7)
designer4 = Designer('Ale','Petro',150,3,'manager1',0.5)
developer1 = Developer('Vladimir','Kovalev',300,4,'manager1')
developer2 = Developer('Vlad','Koval',300,4,'manager2')
developer3 = Developer('Vadim','Kolev',300,4,'manager2')
developer4 = Developer('Vadmir','Kova',300,4,'manager2')

manager1 = Manager('Anton','Petrosyan',500,4,'top_manager1',[designer1,designer2,developer1,developer2,developer3])
manager2 = Manager('Ann','Petan',500,4,'top_manager1',[designer3,designer4,developer4])
department1 = Department('ITDep1',[manager1,manager2])
department1.give_salary()

developer5 = Developer('Vadr','Kov',340,3,'manager3')
developer6 = Developer('Vadr6','Kov6',346,3,'manager3')
designer5 = Designer('Alexx','Petrov5',130,2,'manager3',0.5)
designer6 = Designer('Axr','Prov6',110,4,'manager3',0.8)

manager3 = Manager('Man3','Manager3',500,4,'top_manager2',[])
department2 = Department('ITDep2',[manager3])
print('----- Error handling part ---------')
department2.give_salary()
manager3.add_team_members([])
manager3.add_team_members([manager2])
print('----- End of Error handling part ---------')
print('----- Use department add team function ---------')
department2.add_team_members(manager3, [developer5,developer6,designer5,designer6])
