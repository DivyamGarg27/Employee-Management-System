class EMS:
    ems_dict={}
    def __init__(self,emp_id,name,age,dept,sal):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.dept = dept
        self.sal = sal
        EMS.ems_dict[self.emp_id] = {"Name":self.name, "Age":self.age, "Department":self.dept, "Salary":self.sal}

    def print_dict(self):
        print(self.ems_dict,end="\n")
        
    def add_employee(emp_id,name,age,dept,sal):
        if(emp_id not in EMS.ems_dict):
            EMS.ems_dict[emp_id] = {"Name":name, "Age":age, "Department":dept, "Salary":sal}
            print("Employee was successfully added\n")
            return True
        else:
            print("Employee ID already exists\n")
            return False
        
    def main_menu(self):
        x = int(input("Choose any one of the following\n1. Add Employee\n2. View All Employees\n3. Search for Employee\n4. Exit\n"))
        if x==1:
            temp = True
            while temp:
                emp = int(input("Enter Employee ID: "))
                if emp in EMS.ems_dict:
                    print("Employee ID already exists! Re-enter Employee ID\n")
                else:
                    n = input("Enter Employee Name: ")
                    a = int(input("Enter Employee Age: "))
                    d = input("Enter Employee Department: ")
                    s = int(input("Enter Employee Salary: "))
                    EMS.add_employee(emp, n, a, d, s)
                    temp = False
            return True
        elif x==2:
            if bool(EMS.ems_dict)==False:
                print("No employees available")
            else:
                print("ID\t","Name\t","Age\t","Department\t","Salary\n")
                for i in EMS.ems_dict:
                    print(i,"\t", end=" ")
                    for j in EMS.ems_dict[i]:
                        print(EMS.ems_dict[i][j],"\t",end=" ")
                    print("\n")
            return True
        elif x==3:
            id = int(input("Enter Employee ID: "))
            
            if id in EMS.ems_dict:
                print(EMS.ems_dict.get(id),"\n")
            else:
                print("Employee ID didn't match\n")
            return True
        else:
            return False
  
e = EMS(1234,"ABC",23,"HR",80000)
print("Welcome to Employee Management System\n")
while(True):
    t = e.main_menu()
    if t==False:
        print("Thank you!")
        break


