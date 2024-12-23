class EmployeeDatabase :
    def __init__(self):
        self.emp_list=[]

    def add_emp(self,emp):
        self.emp_list.append(emp)

    def payroll(self):
        for emp in self.emp_list:
            emp.emp_details()
            emp.calc_salary()


class Employee:

    def __init__(self,name,empid):
        self.name=name
        self.empid=empid

    def emp_details(self):
        print('Employee ID: ',self.empid)
        print('Name of Employee: ',self.name)




class SalariedEmployee(Employee):

    def __init__(self,name,empid,fixed_salary):
        super().__init__(name,empid)
        self.fixed_salary=fixed_salary

    def calc_salary(self):
        print("Salary for Employee ID (Fixed Salaried Employee) ",self.empid," is ",self.fixed_salary)

    def emp_details(self):
        return super().emp_details()
    


class CommissionEmployee(Employee):

    def __init__(self, name, empid,c_rate,total_sales):
        super().__init__(name, empid)
        self.c_rate=c_rate
        self.total_sales=total_sales
        self.salary=0

    def calc_salary(self):
        # Assuming Sales per product is 100
        self.salary= self.total_sales * self.c_rate
        print("Salary for Employee (Commission @",self.c_rate, ") Emp ID : ",self.empid," is ",self.salary)
    
    def emp_details(self):
        return super().emp_details()



class HourlyEmployee(Employee):

    def __init__(self, name, empid, hourly_wage, total_hours_worked):
        super().__init__(name, empid)
        self.hourly_wage = hourly_wage
        self.total_hours_worked = total_hours_worked
        self.salary=0

    def calc_salary(self):
        self.salary = self.total_hours_worked * self. hourly_wage
        print("Salary for Employee (Hourly @",self.hourly_wage,") Emp ID : ",self.empid," is ",self.salary)

    def emp_details(self):
        return super().emp_details()


h_emp=HourlyEmployee('Akash',101,250,10)
s_emp=SalariedEmployee('Tarun',155,25000)
c_emp=CommissionEmployee('Ajay',123,50,10)

db = EmployeeDatabase()

db.add_emp(h_emp)
db.add_emp(s_emp)
db.add_emp(c_emp)

db.payroll()

print()
print()

h_emp.emp_details()

print()

h_emp.calc_salary()
