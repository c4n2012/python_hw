from Hierarchy.department import Department
from Hierarchy.manager import Manager
from Hierarchy.developer import Developer
from Hierarchy.designer import Designer

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