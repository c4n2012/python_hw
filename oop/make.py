import worker_classes
#name,second_name,salary,expirience_years,main_manager,coefficient
designer1 = worker_classes.Designer('Alex','Petrov',130,2,'manager1',0.5)
designer2 = worker_classes.Designer('Ax','Prov',110,4,'manager1',0.8)
designer3 = worker_classes.Designer('Al','Petr',180,4,'manager1',0.7)
designer4 = worker_classes.Designer('Ale','Petro',150,3,'manager1',0.5)
developer1 = worker_classes.Developer('Vladimir','Kovalev',300,4,'manager1')
developer2 = worker_classes.Developer('Vlad','Koval',300,4,'manager2')
developer3 = worker_classes.Developer('Vadim','Kolev',300,4,'manager2')
developer4 = worker_classes.Developer('Vadmir','Kova',300,4,'manager2')
manager1 = worker_classes.Manager('Anton','Petrosyan',500,4,'top_manager1',[designer1,designer2,developer1,developer2,developer3])
manager2 = worker_classes.Manager('Ann','Petan',500,4,'top_manager1',[designer3,designer4,developer4])
department1 = worker_classes.Department('ITDep1',[manager1,manager2])
department1.give_salary()