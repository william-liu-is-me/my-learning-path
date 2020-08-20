'''
'M', '曹操'
'P', '荀彧', 120
'P', '郭嘉', 85
'S', '典韦', 123000
'''
from abc import ABCMeta, abstractmethod

class Employee(object):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    
    def Get_salary(self):
        pass

class Manager(Employee):
    #super().__init__(name) #也可以不用写，因为子类没有额外的初始化类，直接继承
    @property
    def Get_salary(self):
        return 15000
class Programmer(Employee):
    def __init__(self,name,working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour
    @property
    def Get_salary(self):
        return 200*self.working_hour
class Sales(Employee):
    def __init__(self,name,sales=0):
        super().__init__(name)
        self.sales = sales
    @property
    def Get_salary(self):
        return 1800 + self.sales * 0.05
class EmployeeFac(object):
    @staticmethod
    def Creat(emp_type,*args,**kwargs):
        all_type = {'M':Manager,'P':Programmer,'S':Sales}
        cls = all_type[emp_type.upper()]
        return cls(*args,**kwargs)

def main():
    emps= [ EmployeeFac.Creat('m','曹操'),
            EmployeeFac.Creat('P','狗货',120),
            EmployeeFac.Creat('s','郭嘉',300000)]
    for emp in emps:
        print(f'{emp.name}的工资是{emp.Get_salary}元')
main()
    

